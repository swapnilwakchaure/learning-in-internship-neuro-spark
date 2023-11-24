f1 = open('fileone.txt', 'w+')
f1.write('this is a first text file for learn that, how to zip files in python?')
f1.close()

f2 = open('filetwo.txt', 'w+')
f2.write('this is a second text file for learn that, how to zip files in python?')
f2.close()


import zipfile

comp_file = zipfile.ZipFile('comp_file.zip', 'w')
comp_file.write('fileone.txt', compress_type=zipfile.ZIP_DEFLATED)
comp_file.write('filetwo.txt', compress_type=zipfile.ZIP_DEFLATED)
comp_file.close()


zip_obj = zipfile.ZipFile('comp_file.zip', 'r')
zip_obj.extractall('extracted_content')



import os

file_path = os.getcwd()
# print('path: ', file_path)



import shutil 

# zip the folder
output_filename = 'example'
shutil.make_archive(output_filename, 'zip', file_path)

# unzip the folder
shutil.unpack_archive('example.zip', 'final_unzip', 'zip')