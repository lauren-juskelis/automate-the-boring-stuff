# Saves a copy of the current folder with the updated date each time a new .zip file is saved. 

import zipfile, os, re, datetime

original_folder = 'C:/Users/ljuskelis/Desktop/LaurenJuskelis/Cursos/IDLE/dates'

original_files = os.listdir(original_folder)

# Find the date to name the next .zip file. 

day = str(datetime.date.today().day)
month = str(datetime.date.today().month)
year = str(datetime.date.today().year)

# Open, append, and close the zip file:

new_zip = zipfile.ZipFile(original_folder + '/backup_files_' + month + '-' + day + '-' + year + '.zip', 'a')

for i in range(len(original_files)):
    if original_files[i][-4:] != '.zip':
        new_zip.write(original_folder + '/' + original_files[i], compress_type = zipfile.ZIP_DEFLATED)
        print('File ' + str(i) + ' zipped.')

new_zip.close()
