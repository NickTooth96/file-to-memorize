import src.create as create
import src.parse as parse
import src.retrieve as retrieve


def fancy():
    pdfpath = "/mnt/c/Users/nickt/OneDrive/~School/cpre_339/slides/SE 339 - Lecture 1 - Aug 22- Course Overview.pdf"

    pages = retrieve.from_pdf(pdfpath)
    average_page_number_location = parse.find_page_num_trend(pages)
    for page in pages:
        pages[page] = parse.remove_page_number(pages[page],page,average_page_number_location)   
    text_file = create.make_txt(pages)
    final = create.memorization(text_file)

def lecture2():
    pdfpath = "/mnt/c/Users/nickt/OneDrive/~School/cpre_339/slides/SE 339 - Lecture 2 - Aug 29- Introduction.pdf"

    pages = retrieve.from_pdf(pdfpath)
    average_page_number_location = parse.find_page_num_trend(pages)
    for page in pages:
        pages[page] = parse.remove_page_number(pages[page],page,average_page_number_location)   
    text_file = create.make_txt(pages)
    shorter_pages = parse.remove_small_pages(pages)
    pages = parse.remove_pages(pages,shorter_pages)
    final = create.memorization_from_dict(pages)

lecture2()