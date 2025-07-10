def convert(text: str) -> str:
    text = text.replace(":)", "\U0001f642")
    text = text.replace(":(", "\U0001f641")
    return text


def main():
    text = input("")
    text_converted = convert(text)

    print(text_converted)


main()
