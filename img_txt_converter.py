from PIL import Image
import os


def text_to_image(text_file, output_image, width=100):
    # Read the text file
    with open(text_file, "r", encoding="utf-8") as f:
        text = f.read()

    # Convert each character into a color
    pixels = [(ord(c) >> 16 & 0xFF, ord(c) >> 8 & 0xFF, ord(c) & 0xFF) for c in text]

    # Calculate image dimensions
    height = (len(pixels) + width - 1) // width  # Round up
    pixels += [(0, 0, 0)] * (width * height - len(pixels))  # Padding to fill image

    # Create the image
    img = Image.new("RGB", (width, height))
    img.putdata(pixels)
    img.save(output_image)
    print(f"Text successfully converted to image: {output_image}")


def image_to_text(image_file, output_text_file):
    # Open the image
    img = Image.open(image_file)
    pixels = list(img.getdata())

    # Convert each pixel back to a character
    chars = [chr((r << 16) | (g << 8) | b) for r, g, b in pixels if r != 0 or g != 0 or b != 0]

    # Save to a text file
    with open(output_text_file, "w", encoding="utf-8") as f:
        f.write("".join(chars))
    print(f"Image successfully converted to text: {output_text_file}")


def main():
    print("Choose an option:")
    print("1. Convert text to image")
    print("2. Convert image to text")
    choice = input("Enter 1 or 2: ").strip()

    if choice == "1":
        text_file = input("Enter the path to the text file: ").strip()
        output_image = input("Enter the output image file name: ").strip()
        width = int(input("Enter the image width (default 100): ") or 100)

        if os.path.exists(text_file):
            text_to_image(text_file, output_image, width)
        else:
            print("Error: Text file not found.")
    elif choice == "2":
        image_file = input("Enter the path to the image file: ").strip()
        output_text_file = input("Enter the output text file name: ").strip()

        if os.path.exists(image_file):
            image_to_text(image_file, output_text_file)
        else:
            print("Error: Image file not found.")
    else:
        print("Invalid choice. Exiting.")


if __name__ == "__main__":
    main()
