import fitz


def extract_pdf_text(file_path):
    """
    Extract complete text from a PDF file.
    """

    pdf = fitz.open(file_path)

    text = ""

    for page in pdf:
        text += page.get_text()

    pdf.close()

    return text