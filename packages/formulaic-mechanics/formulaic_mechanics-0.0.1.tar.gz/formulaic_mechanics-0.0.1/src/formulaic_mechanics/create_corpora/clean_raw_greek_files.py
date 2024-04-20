# Raw files are found in the folder data/raw_files.
# Raw files have a _raw suffix.
# Book numbers are always two digits, ranging from 01 to 24. 
# Clean files contain accents and breathing marks, but no editorial punctuation.
# Clean files hae a _clean suffix.
# Clean editorial files contain accents, breathing marks, and editorial punctuation.
# Clean editorial files have an _editorial suffix

### AUTHOR: Annie K. Lamar
### DATE: May 8, 2023

import os
import re


def clean_raw_greek_files():
    # directories for all file types
    raw_files = 'data/raw_files'
    clean_files = 'data/clean_files'
    editorial_files = 'data/editorial_files'
    re_num_pattern = r'[0-9]'
    punctuation_to_remove = [',', '᾽', '.', ';', ':', ',']
    # loop through each file in the raw_files directory
    for filename in os.listdir(raw_files):

        # get and create file names
        raw_file_name = os.path.join(raw_files, filename)
        clean_file_name = ((raw_file_name[:-7]) + 'clean.txt').replace('raw_files', 'clean_files')
        editorial_file_name = ((raw_file_name[:-7]) + 'editorial.txt').replace('raw_files', 'editorial_files')
        print(clean_file_name)
        # open or create raw, clean, and editorial file
        raw_file = open(raw_file_name, 'r', encoding='utf8')
        clean_file = open(clean_file_name, 'w+', encoding='utf8')
        editorial_file = open(editorial_file_name, 'w+', encoding='utf8')

        # read and clean lines in raw_file
        raw_lines = raw_file.readlines()
        for raw_line in raw_lines:
            if len(raw_line) > 10:
                editorial_line = re.sub(re_num_pattern, '', raw_line)
                editorial_file.write(editorial_line)
                clean_line = editorial_line
                for item in punctuation_to_remove:
                    if item in clean_line:
                        clean_line = clean_line.replace(item, "")
                clean_file.write(clean_line)

        raw_file.close()
        clean_file.close()
        editorial_file.close()
