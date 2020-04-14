import os
from os.path import isfile, join

def get_files(ext, path=os.getcwd()):
    content = os.listdir(path)
    files = []
    for item in content:
        path_to_item = join(path, item)
        if isfile(path_to_item):
            if path_to_item.endswith(ext):
                files.append(path_to_item)
        else:
            files.extend(get_files(ext, path_to_item))
    return files

def write_in_file(file, content):
    with open(file, 'a+') as wf:
        wf.write('\n'+'\n'.join(content))

ext = input('Extensions: ')
ext = '.'+ext
result_file = input('Result file name:  ')

files = get_files(ext)
write_in_file(result_file, files)
