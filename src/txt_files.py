import os

def combine(dir_path):    
    dir_name = os.path.basename(dir_path).split('.')[0]
    files = os.listdir(dir_path)
    filenames = []
    for file in files:
        filenames.append(os.path.join(dir_path,file))
    # print(filenames)
    # print(dir_name)
    with open(f'{dir_path}.txt','w') as outfile:
        for fname in filenames:
            outfile.write("\n")
            with open(fname) as infile:
                outfile.write(infile.read())