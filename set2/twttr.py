VOWELS = ["a", "e", "i", "o", "u"]


def get_twttrzd(text: str) -> str:
    text_twttrzd_list = [char for char in text if char.lower() not in VOWELS]
    return "".join(text_twttrzd_list)


def main():
    text = input("Input: ")
    output_text = get_twttrzd(text)
    print(f"Output: {output_text}")


main()
