import string
import re


### Parse String


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


### Parse Dictionary


def find_page_num_trend(pages):
    page_number_location = []
    for page in pages:
        if type(page) != str:
            matches = [m.start() for m in re.finditer(str(page),pages[page])]
            average_match = sum(matches) / len(matches)
            page_number_location.append(average_match / len(pages[page]))
    average_location = sum(page_number_location) / len(page_number_location)
    return average_location

def remove_small_pages(dictionary):
    short_lines = []
    for entry in dictionary:        
        line = dictionary[entry].split("\n")
        if len(line) <= 3:
            print("Page " + str(entry) + ":",len(line),"lines")
            print(dictionary[entry])
            short_lines.append(entry)
    return short_lines

def remove_pages(dictionary,pages_to_remove):
    output = {}
    for entry in dictionary:
        if entry not in pages_to_remove:
            output[entry] = dictionary[entry]
    return output

