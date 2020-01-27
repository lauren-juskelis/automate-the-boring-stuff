# Saves a copy of the current folder.

import zipfile, os

original_folder = 'C:/Users/ljuskelis/Desktop/LaurenJuskelis/Cursos/IDLE/dates'

original_files = os.listdir(original_folder)

for i in range(len(original_files)):
    new_zip = zipfile.ZipFile(original_folder + '/backup_files_0.zip', 'a')
    new_zip.write(original_folder + '/' + original_files[i], compress_type = zipfile.ZIP_DEFLATED)
    print('File ' + str(i) + ' zipped.')
    new_zip.close()
