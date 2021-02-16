import argparse
from week2 import print_file_content, write_list_to_file, read_csv, write_lines_to_file

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='A program that read, writes and or stores it locally')
    parser.add_argument('file', help='The path to the file to process')
    parser.add_argument('outfile', help='The name of the file to output to')

    args = parser.parse_args()
    print('File:', args.file)
    print('Outfile:', args.outfile)

    file = args.file
    outfile = args.outfile

    output_list = read_csv(file)

    if outfile != None:
        write_lines_to_file(outfile, output_list)
    else:
        print(output_list)