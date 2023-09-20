import os
import datetime
import string
import src.parse as parse
from io import StringIO 

def txt(pages: dict):
    """ Creates a single text file containing text from input dictionary. 
    Args:
        pages (dict): input dictionary  

    Returns:
        str: path to txt file created by function
    """
    file_path = os.path.join(pages['directory'], pages['name'] + ".txt")
    file = open(file_path,'w')
    text_string = StringIO()
    for page in pages:
        if type(page) != str:
            text_string.write(f"Page {page}")
            text_string.write("\n\n")
            text_string.write(pages[page])
            text_string.write("\n\n")
    file.write(text_string.getvalue())
    return file_path

def txts(pages: dict):
    os.mkdir(os.path.join(pages['directory'],pages['name']))
    for page in pages:
        name = str(page).rjust(2,"0")
        file_path = os.path.join(pages['directory'], pages['name'], name + ".txt") 
        file = open(file_path,'w')
        text_string = StringIO()
        text_string.write(f"Page {page}")
        text_string.write("\n\n")
        text_string.write(pages[page])
        text_string.write("\n\n")
        file.write(text_string.getvalue())
    return file_path

def memorization_from_txt(source_filepath):
    source = open(source_filepath,'r').readlines()
    new_text = StringIO()
    for line in source:
        for word in line.split():
            line = line.replace(word,parse.word(word))
        new_text.write(line)
    source = open(source_filepath,'a')
    source.write(new_text.getvalue())

def has_name(dictionary):
    try:
        return dictionary['name']
    except:
        name = str(datetime.datetime.now()).replace(' ','_').split('.')[0]
        return name

    