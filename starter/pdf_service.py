def extract_text_from_pdf(file_path: str) -> str:
    """Extract plain text from a PDF file, page by page."""
    # TODO: open the PDF with pdfplumber, loop pages, concatenate extract_text()
    raise NotImplementedError


def chunk_text(text: str, chunk_size: int = 1000) -> list[str]:
    """Split text into ~chunk_size-character chunks, breaking on paragraph
    boundaries so a chunk never cuts a paragraph in half. Notes with several
    topics/sections end up as several chunks, which is what lets question
    generation spread across the whole document instead of just the start."""
    # TODO: split text on "\n\n" into paragraphs, then pack paragraphs into
    # a list of chunks, starting a new chunk whenever adding the next
    # paragraph would exceed chunk_size
    raise NotImplementedError
