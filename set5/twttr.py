VOWELS = ["a", "e", "i", "o", "u"]


def shorten(text: str) -> str:
    text_twttrzd_list = [char for char in text if char.lower() not in VOWELS]
    return "".join(text_twttrzd_list)


def main():
    text = input("Input: ")
    output_text = shorten(text)
    print(f"Output: {output_text}")


if __name__ == "__main__":
    main()
