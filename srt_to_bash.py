import re
import sys

def parse_srt_time(srt_time):
    """Convert SRT timestamp to seconds."""
    h, m, s, ms = map(float, re.split('[:.,]', srt_time))
    return h * 3600 + m * 60 + s + ms / 1000

def convert_srt_to_bash(srt_file, output_file):
    with open(srt_file, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    bash_script = "#!/bin/bash\n\n"
    previous_time = 0

    i = 0
    while i < len(lines):
        if re.match(r"^\d+$", lines[i].strip()):  # Subtitle index
            time_range = lines[i + 1].strip()
            start_time, _ = time_range.split(" --> ")
            start_seconds = parse_srt_time(start_time)

            # Add delay based on the difference between current and previous times
            delay = max(0, start_seconds - previous_time)
            bash_script += f"sleep {delay:.3f}\n"

            # Add the subtitle text
            text = ""
            j = i + 2
            while j < len(lines) and lines[j].strip():
                text += lines[j]
                j += 1
            bash_script += f'echo "{text.strip()}"\n'

            previous_time = start_seconds
            i = j  # Move to the next subtitle block
        else:
            i += 1

    # Write the bash script to the output file
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(bash_script)

    print(f"Bash script written to {output_file}")

# Example usage
if len(sys.argv) != 3:
    print("Usage: python convert_srt_to_bash.py input.srt output.sh")
else:
    convert_srt_to_bash(sys.argv[1], sys.argv[2])
