import os
import random
import tempfile
import shutil
import cv2
import moviepy.editor as mp
import numpy as np
from pydub import AudioSegment

def shuffle_video(input_file, output_file):
    # Create a unique temporary directory
    temp_dir = tempfile.mkdtemp()
    
    try:
        # Temporary directories for frames and audio snippets
        frames_dir = os.path.join(temp_dir, "frames")
        audio_dir = os.path.join(temp_dir, "audio")
        os.makedirs(frames_dir)
        os.makedirs(audio_dir)

        # Extract frames from the video
        video_cap = cv2.VideoCapture(input_file)
        fps = video_cap.get(cv2.CAP_PROP_FPS)
        frame_count = int(video_cap.get(cv2.CAP_PROP_FRAME_COUNT))

        print("Extracting frames...")
        frame_paths = []
        for i in range(frame_count):
            ret, frame = video_cap.read()
            if not ret:
                break
            frame_path = os.path.join(frames_dir, f"frame_{i:04d}.png")
            cv2.imwrite(frame_path, frame)
            frame_paths.append(frame_path)

        video_cap.release()

        # Extract audio
        print("Extracting audio...")
        video = mp.VideoFileClip(input_file)
        audio = AudioSegment.from_file(input_file)
        duration = len(audio)  # duration in milliseconds
        audio_snippets = []
        snippet_duration = int(duration / frame_count)
        
        for i in range(frame_count):
            start = i * snippet_duration
            end = start + snippet_duration
            snippet = audio[start:end]
            snippet_path = os.path.join(audio_dir, f"audio_{i:04d}.wav")
            snippet.export(snippet_path, format="wav")
            audio_snippets.append(snippet_path)

        # Shuffle frames and audio together
        print("Shuffling frames and audio...")
        indices = list(range(frame_count))
        random.shuffle(indices)

        shuffled_frames = [frame_paths[i] for i in indices]
        shuffled_audio = [audio_snippets[i] for i in indices]

        # Reassemble shuffled frames into a video
        print("Creating shuffled video...")
        height, width, _ = cv2.imread(shuffled_frames[0]).shape
        fourcc = cv2.VideoWriter_fourcc(*"mp4v")
        shuffled_video_path = os.path.join(temp_dir, "shuffled_video.mp4")
        video_writer = cv2.VideoWriter(shuffled_video_path, fourcc, fps, (width, height))

        for frame_path in shuffled_frames:
            frame = cv2.imread(frame_path)
            video_writer.write(frame)

        video_writer.release()

        # Reassemble shuffled audio
        print("Creating shuffled audio...")
        shuffled_audio_combined = AudioSegment.empty()
        for snippet_path in shuffled_audio:
            snippet = AudioSegment.from_file(snippet_path)
            shuffled_audio_combined += snippet

        shuffled_audio_path = os.path.join(temp_dir, "shuffled_audio.wav")
        shuffled_audio_combined.export(shuffled_audio_path, format="wav")

        # Combine shuffled video and audio
        print("Combining shuffled video and audio...")
        shuffled_video = mp.VideoFileClip(shuffled_video_path)
        shuffled_video = shuffled_video.set_audio(mp.AudioFileClip(shuffled_audio_path))
        shuffled_video.write_videofile(output_file, codec="libx264", audio_codec="aac")

        print(f"Shuffled video saved as: {output_file}")
    finally:
        # Cleanup temporary directory
        shutil.rmtree(temp_dir)
        print("Temporary files cleaned up.")

# Example usage
if __name__ == "__main__":
    input_path = input("Enter the path to the input video file: ").strip()
    output_path = input("Enter the desired name for the output video file: ").strip()
    shuffle_video(input_path, output_path)
