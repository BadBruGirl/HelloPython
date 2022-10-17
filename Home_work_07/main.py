from os.path import exists
from creating_csv import creating
from prog_for_writing_in_file import writing_scv
from prog_for_writing_in_file import writing_txt


path = 'Phonebook.csv'
valid = exists(path)
if not valid:
    creating()

writing_scv()
writing_txt()