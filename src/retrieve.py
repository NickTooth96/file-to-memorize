import os
import pathlib
import src.parse as parse
from io import StringIO 
from PyPDF2 import PdfReader


def retrieve(filepath: str):
    file_ex = pathlib.Path(filepath).suffix
    if file_ex == ".pdf":
        return from_pdf(filepath)
    elif file_ex == ".txt":
        return from_txt(filepath)
    elif file_ex == ".md":
        return from_md(filepath)
    elif file_ex == ".docx":
        return from_docx(filepath)

def from_pdf(filepath):
    """Pulls text from PDF file and returns it in dictionary form 

    Args:
        filepath (string): path to PDF file to retrieve text from

    Returns:
        dictionary: output dictionary with pages as entries and page numbers as keys
    """
    dst = filepath.split(".")[0]
    text = {'name': os.path.basename(filepath).split('.')[0], 'path': filepath, 'directory': os.path.dirname(filepath)}
    print(text['name'])
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