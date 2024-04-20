"""Main class for all Corpus functions."""
import glob
import os
from collections import defaultdict
import pandas as pd
# package files
from . import helpers
from . import line_sets as ls
from . import meter_mechanics
from . import mutual_expectancy as me
from . import n_grams
from . import vocabulary

class Corpus:

    def __init__(self, quiet=True):

        path = os.getcwd() + '\data' + '\corpora' + '\clean_files'
        text_files = glob.glob(os.path.join(path, "*.txt"))
        corpus_header = ['text', 'book', 'line', 'string']
        all_lines = []
        for file in text_files:
            if not quiet:
                print('File Name:', file.split("\\")[-1])

            # setting up text and book for each file

            text = ""
            if 'iliad' in file:
                text = 'iliad'
            elif 'odyssey' in file:
                text = 'odyssey'
            book = file[-12:-10]
            if str(book).startswith('0'):
                book = book[-1]

            # open and read file

            open_file = open(file, 'r', encoding='utf8')
            file_lines = open_file.readlines()
            line_number = 1
            for line in file_lines:
                line = line.strip()
                line = line.replace("’ ", "")
                line = line.replace("’", "")
                line = line.replace("‘ ", "")
                line = line.replace("‘", "")
                line = helpers.standardize_accents(line)
                all_lines.append([text, int(book), int(line_number), line.strip()])
                line_number += 1

        self.corpus = pd.DataFrame(all_lines, columns=corpus_header)

        # N-gram Variables

        self.bigrams = n_grams.count_bigrams(self.corpus, quiet=True)

        if not os.path.isfile('data/bigram_frequencies.csv'):
            self.frequencies = n_grams.filemaker_bigram_frequency(self.bigrams)
        else:
            self.frequencies = pd.read_csv('data/bigram_frequencies.csv')
        if not quiet:
            print("Bigram frequencies loaded.")

        if not os.path.isfile('data/bigram_expectancies.csv'):
            self.expectancies = n_grams.filemaker_bigram_expectancy(self.frequencies)
        else:
            self.expectancies = pd.read_csv('data/bigram_expectancies.csv')
        if not quiet:
            print("Bigram expectancies loaded.")

        if not os.path.isfile('data/trigram_expectancies.csv'):
            self.trigrams = n_grams.count_trigrams(self.corpus, self.expectancies)
        else:
            self.trigrams = pd.read_csv('data/trigram_expectancies.csv', index_col=0)
        if not quiet:
            print("Trigram expectancies loaded.")

        if not os.path.isfile('data/quadgram_expectancies.csv'):
            self.quadgrams = n_grams.count_quadgrams(self.corpus, self.expectancies)
        else:
            self.quadgrams = pd.read_csv('data/quadgram_expectancies.csv', index_col=0)
        if not quiet:
            print("Quadgram expectancies loaded.")

        # Mutual Expectancy

        if not os.path.isfile('data/me_by_book_geometric.csv'):
            self.me_by_book_geometric = me.me_by_book_geometric(self.corpus, self.expectancies)
        else:
            self.me_by_book_geometric = pd.read_csv('data/me_by_book_geometric.csv')
        if not quiet:
            print("Mutual expectancies by book (geometric, not recommended) loaded.")

        if not os.path.isfile('data/me_by_book_arithmetic.csv'):
            self.me_by_book = me.me_by_book_arithmetic(self.corpus, self.expectancies)
        else:
            self.me_by_book = pd.read_csv('data/me_by_book_arithmetic.csv')
        if not quiet:
            print("Mutual expectancies by book (arithmetic, recommended) loaded.")

        if not os.path.isfile('data/me_by_line.csv'):
            self.full_corpus = me.me_by_line(self.corpus, self.expectancies)
        else:
            self.full_corpus = pd.read_csv('data/me_by_line.csv')
        if not quiet:
            print("Mutual expectancies by line loaded.")

        if not os.path.isfile('data/me_by_meter.csv'):
            self.me_by_meter = me.me_by_meter(self.full_corpus)
        else:
            self.me_by_meter = pd.read_csv('data/me_by_meter.csv')
        if not quiet:
            print("Mutual expectancies by meter (arithmetic) loaded.")

        # Vocabulary

        if not os.path.isfile('data/counted_words.csv'):
            self.counted_words = vocabulary.count_words(self.corpus)
        else:
            self.counted_words = pd.read_csv('data/counted_words.csv')
        if not quiet:
            print("Word frequencies for corpus loaded.")

        if not os.path.isfile('data/book_counts.csv'):
            self.book_counts = vocabulary.corpus_book_counts(self.corpus)
        self.book_counts = pd.read_csv('data/book_counts.csv')
        if not quiet:
            print("Word frequencies by book loaded.")

        if not os.path.isfile('data/vocab_overlaps.csv'):
            self.vocabulary_overlaps = vocabulary.vocabulary_overlaps(self.corpus)
        else:
            self.vocabulary_overlaps = pd.read_csv('data/vocab_overlaps.csv')
        if not quiet:
            print("Vocabulary overlaps loaded.")

        if not os.path.isfile('data/iliad_lexical_diversity.csv'):
            vocabulary.calculate_lexical_diversity(self.corpus)
        self.iliad_lexical_diversity = pd.read_csv('data/iliad_lexical_diversity.csv')
        self.odyssey_lexical_diversity = pd.read_csv('data/odyssey_lexical_diversity.csv')
        if not quiet:
            print("Lexical diversity measures loaded.")

        if not os.path.isfile('data/word_counts.csv'):
            self.word_counts = vocabulary.count_hapax(self.corpus)
        else:
            self.word_counts = pd.read_csv('data/word_counts.csv')
        if not quiet:
            print("Word counts loaded.")

        if not os.path.isfile('data/hapax_locations.csv'):
            self.hapax_locations = vocabulary.hapax_distribution(self.corpus)
        else:
            self.hapax_locations = pd.read_csv('data/hapax_locations.csv')
        if not quiet:
            print("Hapax locations loaded.")

        if not os.path.isfile('data/proper_nouns_by_me.csv'):
            vocabulary.proper_noun_stats(self.full_corpus)
        self.proper_nouns = pd.read_csv('data/proper_nouns_by_me.csv')
        self.proper_noun_lines = pd.read_csv('data/proper_lines_by_me.csv')
        if not quiet:
            print("Proper noun statistics loaded.")

        # Line Sets

        if not os.path.isfile('data/repeated_line_sets.csv'):
            self.repeated_line_sets = ls.find_repeated_line_sets(self.full_corpus, self.expectancies)
        else:
            self.repeated_line_sets = pd.read_csv('data/repeated_line_sets.csv')
        if not quiet:
            print("Repeated line sets loaded.")

        # Meter

        if not os.path.isfile('data/metrical_pattern_counts.csv'):
            self.metrical_pattern_counts = meter_mechanics.full_metrical_distribution(self.full_corpus)
        else:
            self.metrical_pattern_counts = pd.read_csv('data/metrical_pattern_counts.csv')
        if not quiet:
            print("Counts of metrical patterns loaded.")

        if not os.path.isfile('data/hemistiches.csv'):
            self.hemistiches = meter_mechanics.get_hemistiches()
        else:
            self.hemistiches = pd.read_csv('data/hemistiches.csv')
        if not quiet:
            print("Hemistiches loaded.")
        print("All datasets loaded.")

        # Special DataFrames

        self.iliad2 = self.full_corpus[(self.full_corpus['book'] == 2) & (self.full_corpus['text'] == 'iliad')]
        self.iliad2_catalogue = self.iliad2[(self.iliad2.line >= 494) & (self.iliad2.line <= 759)]
        self.iliad2_not_catalogue = self.iliad2[(self.iliad2.line < 494) | (self.iliad2.line > 759)]

    # Corpus support methods

    def count_phrase_occurrences(self, phrase):
        """
        Counts how many times a phrase appears in the corpus.

        Parameters
        ----------
        phrase : String
            phrase to search for

        Returns
        -------
        int
            number of times phrase appears in corpus
        """
        occurrences = 0
        for line in self.corpus['string'].to_list():
            if phrase in line:
                occurrences += 1
        return occurrences

    def find_occurrences(self, phrase, print_lines=False):
        """
        Finds occurrences of a phrase  in the corpus.

        Parameters
        ----------
        phrase : String
            phrase to search for
        print_lines : Boolean (False)
            if True, print out list of occurrences

        Returns
        -------
        DataFrame
            contains locations of each occurrence of target phrase
        """
        rows = []
        header = ['text', 'book', 'line', 'string']
        phrase = helpers.clean_line(phrase)
        for index, row, in self.corpus.iterrows():
            if phrase in row['string']:
                rows.append([row['text'], row['book'], row['line'], row['string']])
        if print_lines:
            for row in rows:
                print(row[3])
        return pd.DataFrame(rows, columns=header)

    ### ???
    def count_previous_meters(self, target_meter):
        prevs = defaultdict(int)
        for index, row in self.full_corpus.iterrows():
            if row['meter'] == target_meter:
                if row['line'] == 1:
                    prevs['NONE'] += 1
                else:
                    previous_meter_df = self.full_corpus[(self.full_corpus.text == row['text']) &
                                                         (self.full_corpus.book == row['book']) &
                                                         (self.full_corpus.line == (row['line'] - 1))]
                    previous_meter = previous_meter_df['meter'].values[0]
                    prevs[previous_meter] += 1
        rows = []
        for key in prevs.keys():
            rows.append([key, prevs[key]])
        df = pd.DataFrame(rows, columns=[['meter', 'count']])
        total_prevs = df['count'].sum()
        df['percent'] = (df['count'] / total_prevs)
        new_df = df.merge(self.meter_distribution, how='left')
        # new_df = new_df.reset_index()
        # new_df['difference'] = new_df['Full_percent']-new_df['percent']
        # df = df.difference.abs()
        return new_df
