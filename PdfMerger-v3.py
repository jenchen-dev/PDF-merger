import PyPDF2
import os
import re


while True:
    folder = input('combined pdf folder: ')
    all_file_list = []
    if os.path.exists(folder): # check if this folder exists
        for filename in os.listdir(folder):
            if os.path.splitext(filename)[1] == '.pdf':
                all_file_list.append(filename) # grab each pdf file name in a folder and add it to a list
        break
    else:
        print('folder not exist in this directory. please try again.')

def pdf_combiner(pdf_list):
    merger = PyPDF2.PdfFileMerger()
    
    for files in pdf_list: # merge each file from the list
        merger.append(files)
    
    while True:
        name = input('your new file name: ') # customize your merged file name
        check_vaild = re.compile(r'^[^\\/:"*?<>|]+$')
        new_file = f'{name}.pdf'
        if check_vaild.fullmatch(name) and not os.path.exists(new_file): # check if it's valid and if the same file name exsits
            merger.write(new_file)
            print('file created!')
            break
        elif os.path.exists(new_file):
            print('file name already exists, please rename your new file.')
        else:
            print('please enter a valid file name.')

if bool(all_file_list): # check if any pdf files in this folder
    pdf_combiner(all_file_list)
else:
    print('no pdf file in this folder.')
