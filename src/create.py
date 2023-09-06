import os
import datetime
import src.parse as parse
from io import StringIO 

def make_txt(pages):
    name = has_name(pages)
    file_path = os.path.join(os.path.abspath(__file__)[:-14],f'output/{name}.txt')
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

def make_txts(pages):
    name = has_name(pages)
    os.system(f'mkdir output/{name}/')
    for page in pages:
        file_path = os.path.join(os.path.abspath(__file__)[:-14],f'output/{name}/{page}.txt')
        file = open(file_path,'w')
        text_string = StringIO()
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

def dir_of_txt(source_dir):
    dir_list = os.listdir(source_dir)
    dir_name = parse.get_name(source_dir)
    file = open(f'output/{dir_name}.txt','w')
    for name in dir_list:
        file = os.path.join(source_dir,name)
        memorization_from_txt(file)

def memorization_from_txt(source_filepath):
    source = open(source_filepath,'r').readlines()
    new_text = StringIO()
    for line in source:
        for word in line.split():
            line = line.replace(word, word[0])
        new_text.write(line)
    source = open(source_filepath,'a')
    source.write(new_text.getvalue())

def has_name(dictionary):
    try:
        return dictionary['name']
    except:
        name = str(datetime.datetime.now()).replace(' ','_').split('.')[0]
        return name

    