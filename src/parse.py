import string
import re

def get_page_number(text,number_of_pages):
    page_num_string = ""
    page_number = 0
    previous = ""
    for current in text:
        if previous.isnumeric() and current.isnumeric():
            page_num_string += str(previous) + str(current)
        previous = current

    if page_num_string != "" and int(page_num_string) < number_of_pages:
        page_number = int(page_num_string)
        print(page_num_string,page_number)

    return page_number

def remove_page_number(text,number,location):
    length = len(str(number))
    location = int(location * len(text))
    matches = [m.start() for m in re.finditer(str(number),text)]
    smallest = location
    closest = location
    for x in matches:
        if abs(x-location) < smallest:
            closest = x
            smallest = abs(x-location)
    new_text = [x for x in text]
    for i in range(length):
        new_text[closest + i] = "*"
        new_text = new_text
    return''.join(new_text).replace('*', '')



def remove_nonalphanumeric(text):
    for x in text:
        if not x.isnumeric() and not x.isalpha() and x not in string.punctuation and not x.isspace():
            text = text.replace(x, '')
    return text

def find_page_num_trend(pages):
    page_number_location = []
    for page in pages:
        matches = [m.start() for m in re.finditer(str(page),pages[page])]
        average_match = sum(matches) / len(matches)
        page_number_location.append(average_match / len(pages[page]))
    average_lacation = sum(page_number_location) / len(page_number_location)
    return average_lacation
