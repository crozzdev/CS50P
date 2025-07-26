import sys
from random import choice

from pyfiglet import Figlet


def parse_args(figlet: Figlet) -> str | None:
    """
    Returns a font name if provided/valid, None if no args.
    Exits with 'Invalid usage' otherwise.
    """
    args = sys.argv
    if len(args) == 1:
        return None
    if len(args) == 3 and args[1] in ("-f", "--font") and args[2] in figlet.getFonts():
        return args[2]
    sys.exit("Invalid usage")


def main() -> None:
    f = Figlet()
    font = parse_args(f)
    text = input("Input: ")
    if font is None:
        font = choice(f.getFonts())
    f.setFont(font=font)
    print(f.renderText(text))


if __name__ == "__main__":
    main()
