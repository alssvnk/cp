import os
from os.path import isfile, join

def get_files(path=os.getcwd()):
    content = os.listdir(path)
    files = []
    for item in content:
        path_to_item = join(path, item)
        if isfile(path_to_item):
            files.append(path_to_item)
        else:
            files.extend(get_files(path_to_item))
    return files

files = get_files()

biggerSize = 0
biggerFile = None
for fileStr in files:
    st = os.stat(fileStr)
    if st.st_size > biggerSize:
        biggerSize = st.st_size
        biggerFile = fileStr

print('biggest is {}'.format(biggerFile))