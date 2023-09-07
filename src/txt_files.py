import os
import parse

def combine(dir_path):    
    dir_name = parse.get_name(dir_path)
    files = os.listdir(dir_path)
    filenames = []
    for file in files:
        filenames.append(os.path.join(dir_path,file))
    print(filenames)
    print(dir_name)
    with open(f'{dir_path}.txt','w') as outfile:
        for fname in filenames:
            with open(fname) as infile:
                outfile.write(infile.read())
    
    
main_path = os.path.expanduser(__file__)[:-49]
print(main_path)
path = os.path.join(main_path,"OneDrive","School","cpre_339","quizzes","quiz_1","lecture_2") ## windows path
print(path)
combine(path)