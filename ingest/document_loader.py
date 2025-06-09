def load_pdf(path):
    import fitz
    doc = fitz.open(path)
    return '\n'.join([page.get_text() for page in doc])