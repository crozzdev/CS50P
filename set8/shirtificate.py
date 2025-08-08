import re

from fpdf import FPDF

SHIRT_IMAGE_PATH = "shirtificate.png"
SHIRT_IMAGE_Y = 60  # tweak as needed for your template
TEXT_Y = 120  # chest area; tweak if your template differs


class Shirtificate(FPDF):
    def header(self) -> None:
        self.set_font("helvetica", size=40)
        self.cell(w=0, h=40, text="CS50 Shirtificate", border=0, align="C")


def safe_filename(s: str) -> str:
    s = s.strip()
    s = re.sub(r"[^\w\s.-]", "_", s)
    s = re.sub(r"\s+", "_", s)
    return s or "anonymous"


def create_shirtificate(name: str) -> None:
    pdf = Shirtificate(orientation="P", unit="mm", format="A4")
    pdf.set_auto_page_break(False)
    pdf.add_page()

    # Make the shirt image span the page width (within margins)
    img_w = pdf.epw  # effective page width (page width minus margins)
    # center horizontally by computing x
    x = (pdf.w - img_w) / 2
    pdf.image(SHIRT_IMAGE_PATH, x=x, y=SHIRT_IMAGE_Y, w=img_w)

    # Overlay text
    pdf.set_font("helvetica", style="B", size=28)
    pdf.set_text_color(255, 255, 255)
    pdf.set_y(TEXT_Y)
    pdf.cell(w=0, h=10, text=f"{name} took CS50", border=0, align="C")

    pdf.output(f"shirtificate_{safe_filename(name)}.pdf")


if __name__ == "__main__":
    name_input = input("Name: ")
    create_shirtificate(name_input)
