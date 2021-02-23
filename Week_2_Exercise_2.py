import modules.utils as util

if __name__ == '__main__':
    util.get_file_names("/home/jovyan/python_handin_template")
    util.get_all_file_names("/home/jovyan/python_handin_template")
    file_list = ["output1.txt", "output.txt", "python_handin_template/textfiles/pythonfile.csv"]
    util.print_line_one(file_list)
    email_list = ["readtest.txt", "output1.txt", "python_handin_template/textfiles/emails.txt"]
    util.print_emails(email_list)
    util.write_headlines("python_handin_template/textfiles/headlines.md")