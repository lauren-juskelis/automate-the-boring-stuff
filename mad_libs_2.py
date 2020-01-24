# This program lets the user play Mad Libs, using a .txt file as the
# source data, and saves the output back to a different .txt file.

import re, os, pathlib

# Create a function to replace buzz words:

def mad_libs_function(our_file):
    tester = 1
    mad_libs_re = re.compile(r'ADJECTIVE|NOUN|ADVERB|VERB')
    while tester == 1:
        try: 
            our_re = mad_libs_re.search(our_file)
            our_re.group()
            print('Enter a word that is a/an ' + str(our_re.group()))
            word = input()
            our_file = mad_libs_re.sub(word, our_file, 1)
        except AttributeError:
            tester = 0
    return our_file

# Use the function on a .txt file and save to another .txt file:

my_file = pathlib.Path('mad_libs.txt').read_text()

new_file = open('mad_libs_new.txt', 'w')

new_file.write(mad_libs_function(my_file))

new_file.close()
