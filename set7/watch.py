import re


def main():
    print(parse(input("HTML: ")))


def parse(s):
    """
    Extracts the Youtube URL from a HTML iframe block such as:
    <iframe src="https://www.youtube.com/embed/xvFZjo5PgG0"></iframe> and returns the shareable URL in the form of:
    https://youtu.be/URL
    """

    pattern = (
        r"<iframe.*src=\"https?://(?:www\.)?youtube\.com/embed/(.+?)\".*></iframe>"
    )

    if matches := re.search(pattern, s, re.IGNORECASE):
        return "https://youtu.be/" + matches.group(1)

    return None


if __name__ == "__main__":
    main()
