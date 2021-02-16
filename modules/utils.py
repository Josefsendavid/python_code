import os
import csv

def get_file_names(folderpath,out="output.txt"):
    file_list = os.listdir(folderpath)
    with open(out, 'w') as file_object:
        for file in file_list:
            file_object.write(file + '\n')

get_file_names("/home/jovyan/python_handin_template")

##    """takes a path to a folder and write all filenames recursively (files of all sub folders to)"""
def get_all_file_names(folderpath,out="output1.txt"):
    for root, dirs, files in os.walk(folderpath):
        for file in files:
            with open(out, "a") as file_object:
                file_object.write(file + '\n')

get_all_file_names("/home/jovyan/python_handin_template")

def print_line_one(file_names):
    for file_name in file_names:
        with open(file_name) as file_object:
            print(file_object.readline())

file_list = ["output1.txt", "output.txt"]
print_line_one(file_list)
##    """takes a list of filenames and print the first line of each"""

##    """takes a list of filenames and print each line that contains an email (just look for @)"""
def print_emails(file_names):
    for file_name in file_names:
        with open(file_name, "r") as file_object:
            for line in file_object:
                if '@' in line:
                    print(line)

file_list = ["readtest.txt", "output1.txt"]
print_emails(file_list)

##    """takes a list of md files and writes all headlines (lines starting with #) to a file"""
def write_headlines(md_files, out="python_handin_template/textfiles/headlines.txt"):
    md_list = []
    with open(md_files, "r") as file_object:
        for line in file_object:
            if '# ' in line:
                md_list.append(line)
                with open(out, "w") as file:
                    for ele in md_list:
                        file.write(ele + "\n")

write_headlines("python_handin_template/textfiles/headlines.md")