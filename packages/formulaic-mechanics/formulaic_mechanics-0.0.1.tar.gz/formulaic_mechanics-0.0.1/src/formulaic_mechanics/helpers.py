import pandas as pd
import numpy as np
import math
import glob
import os
import re


def meter_files_to_df():
    """Reads all csv files in data/meter_files to a pandas dataframe."""
    path = os.getcwd() + '\data' + '\meter_files'
    print(path)
    csv_files = glob.glob(os.path.join(path, "*.csv"))
    all_files = []
    for file in csv_files:
        df = pd.read_csv(file)
        # df = df.drop_duplicates(subset=['book', 'line'])
        all_files.append(df)
        print('File Name:', file.split("\\")[-1])
    meter_files = pd.concat(all_files, axis=0, ignore_index=True)
    return meter_files


def get_vocab_overlap(vocab_lists, text1, book1, text2, book2):
    """Calculates the vocabulary overlap between two books in the Homeric corpus."""
    vocab1 = set()
    vocab2 = set()
    for l in vocab_lists:
        if l[0] == text1 and l[1] == book1:
            vocab1 = set(l[2])
        if l[0] == text2 and l[1] == book2:
            vocab2 = set(l[2])
    return [text1, book1, text2, book2, len(vocab1.intersection(vocab2)),
            round((len(vocab1.intersection(vocab2))) / (len((vocab1.union(vocab2)))) * 100, 4)]


def calculate_LR_MSTTR(text, subset_size=100):
    """Calculates the LR-MSTTR of the provided string.
    Original code from https://github.com/kristopherkyle/lexical_diversity/tree/master."""
    all_tokens = text.split(" ")
    arrays = np.array_split(all_tokens, math.ceil(len(all_tokens) / 100))
    all_scores = []
    for array in arrays:
        set_array = set(array)
        TTR = len(set_array) / len(array)
        all_scores.append(TTR)
    all_sum = 0
    for score in all_scores:
        all_sum += score
    return round(all_sum / len(all_scores), 4)


def list_to_string(listed_elements):
    """Returns a list of words as a space-separated string."""
    s = ""
    for list_item in listed_elements:
        tokens = list_item.split(" ")
        for token in tokens:
            s = s + " " + token
    return s


def list_to_set(listed_elements):
    """Removes duplicates from the provided list."""
    s = set()
    for l in listed_elements:
        tokens = l.split(" ")
        for token in tokens:
            s.add(token)
    return s


def list_to_list(listed_elements):
    """Returns a list of sentences as a list of words in those sentences."""
    s = []
    for l in listed_elements:
        tokens = l.split(" ")
        for token in tokens:
            s.append(token)
    return s


def clean_line(line):
    """Cleans the provided line."""
    re_num_pattern = r'[0-9]'
    punctuation_to_remove = [',', '᾽', '.', ';', ':', ',']
    new_line = re.sub(re_num_pattern, '', line)
    for item in punctuation_to_remove:
        if item in new_line:
            new_line = new_line.replace(item, "")
    return new_line


def book_statistics(target_text, target_book, lines_df):
    """Returns a list of statistics about a particular book in the Homeric corpus."""
    df = lines_df[(lines_df.text == target_text) & (lines_df.book == target_book)]
    book_words = set()
    all_words = []
    for ind, row in df.iterrows():
        tokens = row.string.split()
        for token in tokens:
            book_words.add(token)
            all_words.append(token)
    book_lines = len(df)
    unique_book_lines = len(pd.unique(df['string']))
    unique_book_lines_percent = round((len(pd.unique(df['string'])) / len(df)) * 100, 4)
    total_words = len(all_words)
    unique_words = len(book_words)
    unique_words_percent = round((len(book_words) / len(all_words)) * 100, 4)
    return [target_text, target_book, book_lines, unique_book_lines, unique_book_lines_percent, total_words,
            unique_words, unique_words_percent]


def standardize_accents(target_token):
    """Standardize all grave accents to acute accents."""
    token = target_token.replace('ὰ', 'ά')
    token = token.replace('ἂ', 'ἄ')
    token = token.replace('ἃ', 'ἅ')
    token = token.replace('ὲ', 'έ')
    token = token.replace('ἒ', 'ἔ')
    token = token.replace('ἓ', 'ἕ')
    token = token.replace('ὴ', 'ή')
    token = token.replace('ἢ', 'ἤ')
    token = token.replace('ἣ', 'ἥ')
    token = token.replace('ὶ', 'ί')
    token = token.replace('ἲ', 'ἴ')
    token = token.replace('ἳ', 'ἵ')
    token = token.replace('ῒ', 'ΐ')
    token = token.replace('ὸ', 'ό')
    token = token.replace('ὂ', 'ὄ')
    token = token.replace('ὃ', 'ὅ')
    token = token.replace('ὺ', 'ύ')
    token = token.replace('ὒ', 'ὔ')
    token = token.replace('ὓ', 'ὕ')
    token = token.replace('ῢ', 'ΰ')
    token = token.replace('ὼ', 'ώ')
    token = token.replace('ὢ', 'ὤ')
    token = token.replace('ὣ', 'ὥ')
    token = token.replace('ᾲ', 'ᾴ')
    token = token.replace('ᾂ', 'ᾄ')
    token = token.replace('ᾃ', 'ᾅ')
    token = token.replace('ῂ', 'ῄ')
    token = token.replace('ᾒ', 'ᾔ')
    token = token.replace('ᾓ', 'ᾕ')
    token = token.replace('ῲ', 'ῴ')
    token = token.replace('ᾢ', 'ᾤ')
    token = token.replace('ᾣ', 'ᾥ')
    token = token.replace('Ὰ', 'Ά')
    token = token.replace('Ἂ', 'Ἄ')
    token = token.replace('Ἃ', 'Ἅ')
    token = token.replace('Ὲ', 'Έ')
    token = token.replace('Ἒ', 'Ἔ')
    token = token.replace('Ἓ', 'Ἕ')
    token = token.replace('Ὴ', 'Ή')
    token = token.replace('Ἢ', 'Ἤ')
    token = token.replace('Ἣ', 'Ἥ')
    token = token.replace('Ὶ', 'Ί')
    token = token.replace('Ἲ', 'Ἴ')
    token = token.replace('Ἳ', 'Ἵ')
    token = token.replace('Ὸ', 'Ό')
    token = token.replace('Ὂ', 'Ὄ')
    token = token.replace('Ὃ', 'Ὅ')
    token = token.replace('Ὺ', 'Ύ')
    token = token.replace('Ὓ', 'Ὕ')
    token = token.replace('Ὼ', 'Ώ')
    token = token.replace('Ὢ', 'Ὤ')
    token = token.replace('Ὣ', 'Ὥ')
    token = token.replace('ᾊ', 'ᾌ')
    token = token.replace('ᾋ', 'ᾍ')
    token = token.replace('ᾚ', 'ᾜ')
    token = token.replace('ᾛ', 'ᾝ')
    token = token.replace('ᾪ', 'ᾬ')
    token = token.replace('ᾫ', 'ᾭ')
    return token
