import csv

def print_file_content(file):
    with open(file, 'r') as file_object:
        data1 = file_object.read()
        print(data1)

def write_list_to_file(output_file, a1, a2, a3):
    with open(output_file, 'a') as file_object:
        lst = (a1, a2, a3)
        file_object.write('\n' + str(lst))
        
def read_csv(input_file):
    with open(input_file) as file_object:
        lines = file_object.readlines()
        lines = [l.strip() for l in lines]
        ## file_write = 'pythonfile.csv'
        ## write_list_to_file(file_write, lines)
        print(lines)

def write_lines_to_file(output_file, lst):
    print(lst)
    with open (output_file, "w") as file_object:
        for element in lst:
            for ele in element:
                file_object.write(element + "\n")