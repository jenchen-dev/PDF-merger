import PyPDF2
import os
import re
import pathlib

current_folder = pathlib.Path().absolute()
all_file_list = []
for filename in os.listdir(current_folder):
    if os.path.splitext(filename)[1] == '.pdf':
        all_file_list.append(filename)

def pdf_combiner(pdf_list):
    merger = PyPDF2.PdfFileMerger()

    for pdf in pdf_list:
        merger.append(pdf)

    while True:
        name = input('your new file name: ')
        check_vaild = re.compile(r'^[^\\/:"*?<>|]+$')
        new_file = f'{name}.pdf'
        if check_vaild.fullmatch(name) and not os.path.exists(new_file):
            merger.write(new_file)
            print('file created!')
            break
        elif os.path.exists(new_file):
                print('file name already exists, please rename your new file.')
        else:
            print('please enter a valid file name.')

if bool(all_file_list) != False:
    pdf_combiner(all_file_list)
else:
    print('no pdf files in this folder. please check again!')
