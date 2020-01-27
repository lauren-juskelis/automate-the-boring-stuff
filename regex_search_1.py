# Prompts the user for the search word or phrase. 

import os, pathlib, re

print('What word or phrase do you want to search for?')

search_word = input()

# Get list of all folders in file and store as list.

big_list = os.listdir(pathlib.Path.cwd())

# Keep only .txt files.

little_list = []

for i in range(len(big_list)):
    if big_list[i][-4:] == '.txt':
        little_list.append(big_list[i])

# Loop to open each .txt file, search for phrase, if found print
# the entire line.

for i in range(len(little_list)):
    current_file = open(pathlib.Path.cwd() / little_list[i])
    split_ll = current_file.read().split('\n')
    for x in range(len(split_ll)):
        my_regex = re.compile(search_word)
        if my_regex.search(split_ll[x]) != None:
            print(split_ll[x])
    current_file.close()        
