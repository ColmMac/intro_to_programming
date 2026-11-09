from pathlib import Path
import textwrap


PAGE_WIDTH = 595
PAGE_HEIGHT = 842
MARGIN = 50
FONT_SIZE = 12
LINE_HEIGHT = 16
MAX_LINES_PER_PAGE = (PAGE_HEIGHT - 2 * MARGIN) // LINE_HEIGHT
MAX_CHARACTERS_PER_LINE = (PAGE_WIDTH - 2 * MARGIN) // (FONT_SIZE // 2)


def escape_pdf_text(text: str) -> bytes:
    encoded = text.encode("cp1252", errors="replace")
    escaped = bytearray()
    for character in encoded:
        if character in (ord("("), ord(")"), ord("\\")):
            escaped.append(ord("\\"))
            escaped.append(character)
        elif character < 32 or character > 126:
            escaped.extend(f"\\{character:03o}".encode("ascii"))
        else:
            escaped.append(character)
    return bytes(escaped)


def create_pdf(text: str) -> bytes:
    lines: list[str] = []
    for line in text.split("\n"):
        line = line.replace("\t", "    ")
        if line:
            lines.extend(
                textwrap.wrap(
                    line,
                    width=MAX_CHARACTERS_PER_LINE,
                    break_long_words=True,
                    break_on_hyphens=False,
                )
            )
        else:
            lines.append("")

    pages = [
        lines[index : index + MAX_LINES_PER_PAGE]
        for index in range(0, len(lines), MAX_LINES_PER_PAGE)
    ] or [[""]]
    page_ids = [5 + 2 * index for index in range(len(pages))]
    objects = [
        b"<< /Type /Catalog /Pages 2 0 R >>",
        b"<< /Type /Pages /Kids ["
        + b" ".join(f"{page_id} 0 R".encode("ascii") for page_id in page_ids)
        + f"] /Count {len(pages)} >>".encode("ascii"),
        b"<< /Type /Font /Subtype /Type1 /BaseFont /Times-Roman "
        b"/Encoding /WinAnsiEncoding >>",
    ]

    for index, page_lines in enumerate(pages):
        content = bytearray(
            f"BT\n/F1 {FONT_SIZE} Tf\n{MARGIN} "
            f"{PAGE_HEIGHT - MARGIN - FONT_SIZE} Td\n{LINE_HEIGHT} TL\n".encode(
                "ascii"
            )
        )
        for line in page_lines:
            content.extend(b"(")
            content.extend(escape_pdf_text(line))
            content.extend(b") Tj\nT*\n")
        content.extend(b"ET")

        content_id = 4 + 2 * index
        page_id = content_id + 1
        objects.extend(
            [
                b"<< /Length "
                + str(len(content)).encode("ascii")
                + b" >>\nstream\n"
                + bytes(content)
                + b"\nendstream",
                f"<< /Type /Page /Parent 2 0 R /MediaBox "
                f"[0 0 {PAGE_WIDTH} {PAGE_HEIGHT}] "
                f"/Resources << /Font << /F1 3 0 R >> >> "
                f"/Contents {content_id} 0 R >>".encode("ascii"),
            ]
        )

    pdf = bytearray(b"%PDF-1.4\n%\xe2\xe3\xcf\xd3\n")
    offsets = [0]
    for object_id, pdf_object in enumerate(objects, start=1):
        offsets.append(len(pdf))
        pdf.extend(f"{object_id} 0 obj\n".encode("ascii"))
        pdf.extend(pdf_object)
        pdf.extend(b"\nendobj\n")

    xref_offset = len(pdf)
    pdf.extend(f"xref\n0 {len(offsets)}\n".encode("ascii"))
    pdf.extend(b"0000000000 65535 f \n")
    for offset in offsets[1:]:
        pdf.extend(f"{offset:010} 00000 n \n".encode("ascii"))
    pdf.extend(
        f"trailer\n<< /Size {len(offsets)} /Root 1 0 R >>\n"
        f"startxref\n{xref_offset}\n%%EOF\n".encode("ascii")
    )
    return bytes(pdf)


def main() -> None:
    try:
        file_name = input("PDF file name (default: output.pdf): ").strip()
        if not file_name:
            file_name = "output.pdf"

        print("Enter your text below. Type END on its own line when finished:")
        text_lines = []
        while True:
            line = input("Text> ")
            if line == "END":
                break
            text_lines.append(line)
    except EOFError:
        print("\nInput ended before the text was complete; no PDF was created.")
        return

    text = "\n".join(text_lines)
    if not text.strip():
        print("No text entered; no PDF was created.")
        return

    output_path = Path(file_name)
    if output_path.suffix.lower() != ".pdf":
        output_path = output_path.with_suffix(".pdf")

    if output_path.exists():
        try:
            overwrite = input(f"{output_path} already exists. Overwrite it? [y/N]: ")
        except EOFError:
            print("\nNo PDF was created.")
            return
        if overwrite.strip().lower() not in ("y", "yes"):
            print("No PDF was created.")
            return

    try:
        output_path.write_bytes(create_pdf(text))
    except OSError as error:
        print(f"Could not save the PDF: {error}")
        return

    print(f"PDF saved to {output_path}")


if __name__ == "__main__":
    main()
