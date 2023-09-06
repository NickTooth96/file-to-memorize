import os
import src.create as create
import src.parse as parse
import src.retrieve as retrieve


def fancy():
    textfile = make_textfile("/mnt/c/Users/nickt/OneDrive/`School/cpre_339/slides/SE 339 - Lecture 1 - Aug 22- Course Overview.pdf")
    final = create.memorization(textfile)

def lecture2():
    textfile = make_textfile("/mnt/c/Users/nickt/OneDrive/`School/cpre_339/slides/SE 339 - Lecture 2 - Aug 29- Introduction.pdf")
    final = create.memorization_from_txt(textfile)

def lectures_to_files():
    lecture_2 = make_textfiles("/mnt/c/Users/nickt/OneDrive/`School/cpre_339/slides/SE 339 - Lecture 2 - Aug 29- Introduction.pdf")
    lecture_3 = make_textfiles("/mnt/c/Users/nickt/OneDrive/`School/cpre_339/slides/SE 339 - Lecture 3 - Aug 31- Introduction.pdf")

def lecture3():
    textfile = make_textfile("/mnt/c/Users/nickt/OneDrive/`School/cpre_339/slides/SE 339 - Lecture 3 - Aug 31- Introduction.pdf")

def make_textfile(pdfpath):
    pages = retrieve.from_pdf(pdfpath)
    average_page_number_location = parse.find_page_num_trend(pages)
    for page in pages:
        pages[page] = parse.remove_page_number(pages[page],page,average_page_number_location)   
    text_file = create.make_txt(pages)
    return text_file

def make_textfiles(pdfpath):
    pages = retrieve.from_pdf(pdfpath)
    average_page_number_location = parse.find_page_num_trend(pages)
    for page in pages:
        pages[page] = parse.remove_page_number(pages[page],page,average_page_number_location)   
    text_file = create.make_txts(pages)
    return text_file

### main 
open('output/test.txt','w')
os.system('rm -r output/*')
# create.dir_of_txt('/mnt/c/Users/nickt/OneDrive/School/cpre_339/quizzes/quiz_1/lecture_3/')