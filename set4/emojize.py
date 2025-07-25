import emoji


def lets_emojinize(emoji_str: str) -> str:
    try:
        emoji_unicode = emoji.emojize(emoji_str)
        return emoji_unicode
    except TypeError:
        print("Invalid input")
        return ""


def main():
    emoji_str = input("Input: ")
    print(lets_emojinize(emoji_str))


main()
