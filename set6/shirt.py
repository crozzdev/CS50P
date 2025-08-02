import os
import sys

from PIL import Image, ImageOps

SUPPORTED_EXT = (".png", ".jpg", ".jpeg")


def check_arguments():
    if len(sys.argv) != 3:
        sys.exit(
            "Too few command-line arguments"
            if len(sys.argv) < 3
            else "Too many command-line arguments"
        )

    first_ext = os.path.splitext(sys.argv[1])[1].lower()
    second_ext = os.path.splitext(sys.argv[2])[1].lower()

    if first_ext not in SUPPORTED_EXT or second_ext not in SUPPORTED_EXT:
        sys.exit("Invalid input")

    if first_ext != second_ext:
        sys.exit("Input and output have different extensions")


def process_image(input_img_path: str, output_img_path: str):
    try:
        with Image.open(input_img_path) as input_im, Image.open("shirt.png") as shirt:
            shirt_size = shirt.size
            cropped_input_im = ImageOps.fit(input_im, shirt_size)
            cropped_input_im.paste(shirt, shirt)
            cropped_input_im.save(output_img_path)

    except FileNotFoundError:
        sys.exit("Input does not exist")


def main():
    check_arguments()
    process_image(sys.argv[1], sys.argv[2])


if __name__ == "__main__":
    main()
