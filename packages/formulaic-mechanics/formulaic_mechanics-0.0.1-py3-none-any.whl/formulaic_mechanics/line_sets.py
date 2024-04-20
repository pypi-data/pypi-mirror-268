from collections import defaultdict
import pandas as pd
from . import mutual_expectancy as me


def find_repeated_line_sets(corpus, bigram_expectancies, to_file=True):
    """
    Finds sets of repeated lines in the Homeric corpus.
    Stores this information in a .csv file for easy data loading.
    CSV File location: data/repeated_line_sets.csv

    Parameters
    ----------
    corpus : DataFrame
        contains text of Homeric corpus
    bigram_expectancies : DataFrame
        contains all bigrams and their expectancies
    to_file : Boolean
        if True, save DataFrame to .csv

    Returns
    -------
    DataFrame
        contains all sets of repeated lines in the Homeric corpus and their expectancies
    """
    repeated = []
    header = ['set_size', 'lines', 'times_repeated', 'text', 'book', 'line', 'passage_ME']
    print("Building dataset of repeated line sets...")
    for i in range(2, 16):
        line_sets = []
        corpus_rows_count = 0
        print("Working on line sets of size ", i)
        line_dict = defaultdict(int)
        for index, row in corpus.iterrows():
            corpus_rows_count += 1
            if corpus_rows_count % 5000 == 0:
                print("Building line sets: ", str(corpus_rows_count))
            line = row['string']
            add_line = True
            for next_line in range(1, i):
                if index + next_line < 27789:
                    line = line + "/" + corpus.iloc[index + next_line]['string']
                else:
                    add_line = False
            if add_line:
                line_dict[line] += 1
                line_sets.append([line, row['text'], row['book'], row['line']])

        key_rows_count = 0
        for key in line_dict.keys():
            key_rows_count += 1
            if key_rows_count % 5000 == 0:
                print("Checking for non-zero keys: " + str(key_rows_count))
            if line_dict[key] > 1:
                for row in line_sets:
                    if key == row[0]:
                        mex = me.arithmetic_passage_expectancy(key, bigram_expectancies, split_on='/')
                        repeated.append([i, key, line_dict[key], row[1], row[2], row[3], mex])

    repeated_df = pd.DataFrame(repeated, columns=header)
    if to_file:
        repeated_df.to_csv('data/repeated_line_sets.csv')
    return repeated_df


def get_repeated_lines_in_book(corpus, text, book):
    """
    Finds repeated lines in a given book.
    Stores this information in a .csv file for easy data loading.
    CSV File location: data/repeated_lines_[text][book].csv

    Parameters
    ----------
    corpus : DataFrame
        contains text of Homeric corpus (use corpus.me_by_line_df)
    text : String
        name of the text (Iliad or Odyssey)
    book : int
        book number in text

    Returns
    -------
    DataFrame
        contains all repeated lines in the specified book
    """
    text = text.lower()
    target = corpus[(corpus.full_corpus.text == text) & (corpus.full_corpus.book == book)]
    target['repeated'] = target.duplicated(keep=False, subset='string')
    filename = 'data/repeated_lines_' + text + str(book) + '.csv'
    target.to_csv(filename)