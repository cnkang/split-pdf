import sys
from PyPDF2 import PdfReader, PdfWriter

def split_pdf(input_pdf):
    reader = PdfReader(input_pdf)
    for i, page in enumerate(reader.pages, start=1):
        writer = PdfWriter()
        writer.add_page(page)
        output_filename = f"{input_pdf[:-4]}_page_{i}.pdf"
        with open(output_filename, "wb") as out_f:
            writer.write(out_f)
        print(f"Saved: {output_filename}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python split_pdf_by_page.py filename.pdf")
        sys.exit(1)
    split_pdf(sys.argv[1])