import os
from . import scan
import csv

def make_unformatted_meter_files():
    """Uses scan.py to scan all lines in clean_files."""
    for filename in os.listdir('../data/corpora/clean_files'):
        filepath = os.path.join('../data/corpora/clean_files', filename)
        file = open(filepath, 'r', encoding='utf8')
        contents = file.readlines()
        meter_file_name = ((filepath[:-9]) + 'unformatted_meter.txt').replace('clean_files', 'meter_unformatted_files')
        #open and create new file here
        new_file = open(meter_file_name, 'w+', encoding='utf8')
        for line in contents:
            meter_list = scan.analyze_line(line)
            new_file.write(str(meter_list))  
        new_file.close()
        file.close()
    # [('++|++|++|+--|+--|++', ('πολλὰς δ ἰφθίμους ', 'ψυχὰς ἄϊδι προΐαψεν\n')), ('++|++|+--|++|+--|++', ('πολλὰς δ ἰφθίμους ', 'ψυχὰς ἄϊδι προΐαψεν\n'))

def convert_dashed_meter(dashed_meter):
    """Converts all dashed metrical patterns to letter-based patterns"""
    meter_pattern = ''
    dashed_meter = dashed_meter.replace(".", "")
    feet = dashed_meter.split("|")
    foot_num = 1
    for foot in feet:
        if foot_num == 6:
            meter_pattern = meter_pattern + 'A'
        elif foot == '++':
            meter_pattern = meter_pattern + 'S'
        elif foot == '+--':
            meter_pattern = meter_pattern + 'D'
        else:
            meter_pattern = meter_pattern + "?"
        foot_num += 1
    return meter_pattern

def format_meter_files():
    """Formats meter files into readable, useful format."""
    meter_options_file = open('data/meter_options.csv', 'w+', encoding='utf8', newline='')
    options_csv_writer = csv.writer(meter_options_file)
    options_fields = ['index', 'text', 'book', 'line', 'dashed_meter', 'meter', 'first_hemistich', 'second_hemistich', 'caesura']
    options_csv_writer.writerow(options_fields)
    
    options_line_index = 0
    for filename in os.listdir('../data/meter/meter_unformatted_files'):
        
        #open unformatted file
        filepath = os.path.join('../data/meter/meter_unformatted_files', filename)
        file = open(filepath, 'r', encoding='utf8')
        contents = file.readlines()
        contents = contents[0].split(']')
        
        #open up new file for formatted contents
        meter_file_name = ((filepath[:-23]) + '_meter.csv').replace('meter_unformatted_files', 'meter_files')
        meter_file = open(meter_file_name, 'w+', encoding='utf8', newline='')
        meter_csv_writer = csv.writer(meter_file)
        meter_fields = ['text', 'book', 'line', 'dashed_meter', 'meter', 'first_hemistich', 'second_hemistich', 'caesura']
        meter_csv_writer.writerow(meter_fields)
        
        if 'iliad' in filepath:
            text = 'iliad'
            book = filepath[40:-23]            
        if 'odyssey' in filepath:
            text = 'odyssey'
            book = filepath[42:-23]
            
        remove = ['[','(', '\'', ')', '\n']
        
        #loop for lines with multiple options
        line_index = 0
        for line in contents:
            if '),' in line: 
                options = line.split('),')
                for option in options:
                    components = option.split(",")
                    #components[0] = meter
                    messy_meter = components[0]
                    meter = ''.join(x for x in messy_meter if not x in remove)
                    #components[1] = first half of line
                    messy_first_hemi = components[1]
                    first_hemi = ''.join(x for x in messy_first_hemi if not x in remove)
                    #components[2] = second half of line
                    if len(components) > 2:
                        messy_second_hemi = components[2]
                        second_hemi = ''.join(x for x in messy_second_hemi if not x in remove)
                        if '\\n' in second_hemi:
                            second_hemi = second_hemi[:-2]
                    else:
                        second_hemi = 'NA'
                        
                    letter_meter = convert_dashed_meter(meter)
                    full_line = first_hemi.strip() + " C " + second_hemi.strip()
                    
                    to_write = [str(options_line_index), text, str(book), str(line_index), meter, letter_meter, first_hemi.strip(), second_hemi.strip(), full_line]
                    options_csv_writer.writerow(to_write)
                    options_line_index += 1
                line_index += 1
                    
        #loop for first option only
        line_index = 0
        for line in contents:
            if '),' in line: 
                options = line.split('),')
                messy_data = options[0]
            else:
                messy_data = line
            if len(messy_data) > 10:
                components = messy_data.split(",")
                #components[0] = meter
                messy_meter = components[0]
                meter = ''.join(x for x in messy_meter if not x in remove)
                #components[1] = first half of line
                messy_first_hemi = components[1]
                first_hemi = ''.join(x for x in messy_first_hemi if not x in remove)
                #components[2] = second half of line
                if len(components) > 2:
                    messy_second_hemi = components[2]
                    second_hemi = ''.join(x for x in messy_second_hemi if not x in remove)
                    if '\\n' in second_hemi:
                        second_hemi = second_hemi[:-2]
                else:
                    second_hemi = 'NA'
                letter_meter = convert_dashed_meter(meter)
                full_line = first_hemi.strip() + " C " + second_hemi.strip()

                to_write = [text, str(book), str(line_index), meter, letter_meter, first_hemi.strip(), second_hemi.strip(), full_line]
                line_index += 1
                meter_csv_writer.writerow(to_write)
        
        file.close()
        meter_file.close()
    meter_options_file.close()