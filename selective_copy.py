# Walks through a given folder's tree and copies all .txt files to a different
# folder.

import os, shutil

# Create a new folder to store the copied files.

destination = 'C:\\Users\\ljuskelis\\Desktop\\destination'
os.makedirs(destination)

# Walk the tree to copy the files.

for folder_name, subfolders, filenames in os.walk('C:\\Users\\ljuskelis\\Desktop\\LaurenJuskelis'):
    # print('The current folder is ' + folder_name)
    for filename in filenames:
        if filename[-4:] == '.txt':
            shutil.copy(folder_name + '\\' + filename, destination)

