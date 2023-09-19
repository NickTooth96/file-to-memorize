import src.parse as parse
from io import StringIO 
from PyPDF2 import PdfReader


def from_pdf(filepath):
    """Pulls text from PDF file and returns it in dictionary form 

    Args:
        filepath (string): path to PDF file to retrieve text from

    Returns:
        dictionary: output dictionary with pages as entries and page numbers as keys
    """
    text = {'name': parse.get_name(filepath)}
    reader = PdfReader(filepath)
    page_number = 0

    for page in reader.pages:
        page_number += 1
        page_text = page.extract_text()
        page_text = parse.remove_nonalphanumeric(page_text) 
        text[page_number] = page_text
    return text

def from_txt(filepath):
    pass

def from_md(filepath):
    pass

def from_docx(filepath):
    pass