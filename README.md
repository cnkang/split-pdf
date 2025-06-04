# PDF Splitter

This project provides a simple Python script to split a PDF file into multiple single-page PDF files.

## Files

- `split_pdf_by_page.py.py`: The main script for splitting PDFs by page.
- `requirements.txt`: Lists the required Python packages.

## Installation

Install the necessary dependencies using pip:

```bash
pip install -r requirements.txt
```

## Usage

1. Place the PDF file you want to split in the same directory as `split_pdf_by_page.py.py`.
2. Run the following command in your terminal (replace `filename.pdf` with your PDF file name):

   ```bash
   python split_pdf_by_page.py.py filename.pdf
   ```

3. The script will generate separate files like `filename_page_1.pdf`, `filename_page_2.pdf`, etc., in the same directory.

## Notes

- Make sure your PDF file name ends with `.pdf`.
- Python 3 is required.

## Dependencies

- PyPDF2

See `requirements.txt` for details.

---