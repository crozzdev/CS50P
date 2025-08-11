import emoji


def lets_emojinize(emoji_str: str) -> str:
    try:
        emoji_unicode = emoji.emojize(emoji_str, language="alias")
        return emoji_unicode
    except TypeError:
        print("Invalid input")
        return ""


def main():
    emoji_str = input("Input: ").strip()
    print(lets_emojinize(emoji_str))


main()
