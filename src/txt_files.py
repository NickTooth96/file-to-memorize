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
    with open(f'output/{dir_name}.txt','w') as outfile:
        for fname in filenames:
            with open(fname) as infile:
                outfile.write(infile.read())
    
    

        
combine('/mnt/c/Users/nickt/OneDrive/School/cpre_339/quizzes/quiz_1/lecture_3/')