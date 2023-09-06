import os
from io import StringIO 

def make_txt(pages):
    file_path = os.path.join(os.path.abspath(__file__)[:-14],'output/pdf_to_text.txt')
    file = open(file_path,'w')
    text_string = StringIO()
    for page in pages:
        text_string.write(f"Page {page}")
        text_string.write("\n\n")
        text_string.write(pages[page])
        text_string.write("\n\n")
    file.write(text_string.getvalue())
    return file_path

def memorization_from_dict(pages):
    file_path = os.path.join(os.path.abspath(__file__)[:-14],'output/memorization.txt')
    for page in pages:
        line = pages[page].split(" ")
        print(line)
        for word in line:
            print(word)

def memorization_from_txt(source_filepath):
    file_path = os.path.join(os.path.abspath(__file__)[:-14],'output/memorization.txt')
    