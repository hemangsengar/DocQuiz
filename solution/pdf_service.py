import pdfplumber


def extract_text_from_pdf(file_path: str) -> str:
    """Extract plain text from a PDF file, page by page."""
    text = ""
    with pdfplumber.open(file_path) as pdf:
        for page in pdf.pages:
            page_text = page.extract_text()
            if page_text:
                text += page_text + "\n\n"
    return text.strip()
