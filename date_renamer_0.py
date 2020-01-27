# Renames files with American-style dates in the name to files
# with European-style dates in the name.

import shutil, pathlib, os, re

my_dir = 'C:/Users/ljuskelis/Desktop/LaurenJuskelis/Cursos/IDLE/dates'

my_list = os.listdir(my_dir)

for i in range(len(my_list)):
    my_regex = re.compile(r'(\d\d)-(\d\d)-(\d\d\d\d)')
    mo = my_regex.search(my_list[i])
    new_date = mo.group(2) + '-' + mo.group(1) + '-' + mo.group(3)
    shutil.move(my_dir + '/' + my_list[i], my_dir + '/' + new_date)

print('Done.')
