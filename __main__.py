import os
import sys
import toml
import src.create as create
import src.parse as parse
import src.retrieve as retrieve
import src.txt_files as txt_files


def from_config():
    idx = sys.argv.index("--config") + 1
    config = toml.load(sys.argv[idx])
    print(config)
    for step in config['operation']:
        print(config['operation'][step])


if "--dir" in sys.argv:
    for path in os.listdir(os.getcwd()):
        if not os.path.isdir(path):
            text = retrieve.retrieve(path)
            # text = parse.clean(text) #TODO parse for combined words and stuff 
            create.txts(text)
if "--mem" in sys.argv:
    for path in os.listdir(os.getcwd()):
        if os.path.isdir(path):
            for file in os.listdir(os.path.join(os.getcwd(),path)):
                fpath = os.path.join(path,file)
                create.memorization_from_txt(fpath)
        else: 
            create.memorization_from_txt(path)
if "--combine" in sys.argv:
    for path in os.listdir(os.getcwd()):
        if os.path.isdir(path):
            txt_files.combine(os.path.join(os.getcwd(),path))
        else:
            txt_files.combine(os.path.join(os.getcwd()))
elif "--config" in sys.argv:
    from_config()