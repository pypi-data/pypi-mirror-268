from . import helpers
import pandas as pd
import math
from lexical_diversity import lex_div as ld
from collections import defaultdict
from sklearn.feature_extraction.text import TfidfVectorizer


def count_words(corpus, to_file=True):
    """
    Counts all words in the Homeric corpus.

    Parameters
    ----------
    corpus : DataFrame
        contains text of Homeric corpus
    to_file: Boolean
        if True, save DataFrame to .csv

    Returns
    -------
    DataFrame
        contains statistics about words counts in the Homeric corpus
    """
    words = set()
    all_words = []
    iliad_words = set()
    iliad_all_words = []
    odyssey_words = set()
    odyssey_all_words = []
    for ind, row in corpus.iterrows():
        tokens = row.string.split()
        for token in tokens:
            token = helpers.standardize_accents(token)
            words.add(token)
            all_words.append(token)
            if row.text == 'iliad':
                iliad_words.add(token)
                iliad_all_words.append(token)
            if row.text == 'odyssey':
                odyssey_words.add(token)
                odyssey_all_words.append(token)
    counted_words = pd.DataFrame({'total_words': [len(all_words)],
                                  'unique_words': [len(words)],
                                  'iliad_total_words': [len(iliad_all_words)],
                                  'iliad_unique_words': [len(iliad_words)],
                                  'odyssey_total_words': [len(odyssey_all_words)],
                                  'odyssey_unique_words': [len(odyssey_words)]})
    if to_file:
        counted_words.to_csv('data/counted_words.csv')
    return counted_words


def corpus_book_counts(corpus, to_file=True):
    """
    Counts all words in the Homeric corpus.

    Parameters
    ----------
    corpus : DataFrame
        contains text of Homeric corpus
    to_file: Boolean
        if True, save DataFrame to .csv

    Returns
    -------
    DataFrame
        contains statistics about words counts in the Homeric corpus, by book
    """
    all_books = []
    for i in range(1, 25):
        all_books.append(helpers.book_statistics('iliad', i, corpus))
        all_books.append(helpers.book_statistics('odyssey', i, corpus))
    header = ['text',  # iliad or odyssey
              'book',  # book number
              'total_lines',  # total number of lines in book
              'unique_lines',  # total number of unique lines in book
              'per_unique_lines',  # unique lines / total lines
              'total_words',  # total number of words in book
              'unique_words',  # total number of unique lines in book
              'per_unique_words']  # unique words / total words
    book_stats = pd.DataFrame(all_books, columns=header)
    if to_file:
        book_stats.to_csv('data/book_counts.csv')
    return book_stats


def vocabulary_overlaps(corpus, to_file=True):
    """
    Compares vocabularies of each book in the Homeric corpus.

    Parameters
    ----------
    corpus : DataFrame
        contains text of Homeric corpus
    to_file: Boolean
        if True, save DataFrame to .csv

    Returns
    -------
    DataFrame
        statistics about vocabulary overlap for each pair of books in the Homeric corpus
    """
    vocab_lists = []

    for i in range(1, 25):
        iliad_book_df = corpus[(corpus.text == 'iliad') & (corpus.book == i)]
        odyssey_book_df = corpus[(corpus.text == 'odyssey') & (corpus.book == i)]
        iliad_book_vocab = set()
        odyssey_book_vocab = set()

        for ind, row in iliad_book_df.iterrows():
            tokens = row.string.split()
            for token in tokens:
                iliad_book_vocab.add(token)
        vocab_lists.append(['iliad', i, list(iliad_book_vocab)])

        for ind, row in odyssey_book_df.iterrows():
            tokens = row.string.split()
            for token in tokens:
                odyssey_book_vocab.add(token)
        vocab_lists.append(['odyssey', i, list(odyssey_book_vocab)])

    all_overlaps = []
    for i in range(1, 25):
        for k in range(1, 25):
            all_overlaps.append(helpers.get_vocab_overlap(vocab_lists, 'iliad', i, 'iliad', k))
            all_overlaps.append(helpers.get_vocab_overlap(vocab_lists, 'odyssey', i, 'odyssey', k))
            all_overlaps.append(helpers.get_vocab_overlap(vocab_lists, 'iliad', i, 'odyssey', k))
    edited_all_overlaps = []
    for item in all_overlaps:
        add_me = True
        for added in edited_all_overlaps:
            if item[0] == added[2] and item[1] == added[3] and item[2] == added[0] and item[3] == added[1]:
                add_me = False
        if add_me:
            edited_all_overlaps.append(item)
    overlap_header = ['text1', 'book1', 'text2', 'book2', 'words_in_common', 'perc_in_common']
    overlaps = pd.DataFrame(edited_all_overlaps, columns=overlap_header)
    if to_file:
        overlaps.to_csv('data/vocab_overlaps.csv')
    return overlaps


def calculate_lexical_diversity(corpus, to_file=True):
    """
    Computes lexical diversity statistics for each book in the Homeric canon.

    Parameters
    ----------
    corpus : DataFrame
        contains text of Homeric corpus
    to_file: Boolean
        if True, save DataFrame to .csv

    Returns
    -------
    DataFrame
        statistics about lexical diversity for each book in the Homeric corpus
    """
    header = ['text', 'book', 'TTR', 'RTTR', 'CTTR', 'LR-MSTTR', 'MSTTR', 'MTLD', 'HDD']
    iliad_rows = []
    odyssey_rows = []
    for book in range(1, 25):
        iliad = corpus[(corpus.text == 'iliad') & (corpus.book == book)]['string'].tolist()
        odyssey = corpus[(corpus.text == 'odyssey') & (corpus.book == book)]['string'].tolist()

        iliad_full_text = helpers.list_to_string(iliad)
        iliad_total_words = len(helpers.list_to_list(iliad))
        iliad_unique_words = len(helpers.list_to_set(iliad))

        odyssey_full_text = helpers.list_to_string(odyssey)
        odyssey_total_words = len(helpers.list_to_list(odyssey))
        odyssey_unique_words = len(helpers.list_to_set(odyssey))

        iliad_LR_MSTTR = helpers.calculate_LR_MSTTR(iliad_full_text)
        iliad_MSTTR = round(ld.msttr(iliad_full_text, window_length=100), 4)
        iliad_HDD = round(ld.hdd(iliad_full_text), 4)
        iliad_MTLD = round(ld.mtld(iliad_full_text), 4)
        iliad_TTR = round((iliad_unique_words / iliad_total_words) * 100, 2)
        iliad_RTTR = round((iliad_unique_words / math.sqrt(iliad_total_words)), 2)
        iliad_CTTR = round((iliad_unique_words / math.sqrt(iliad_total_words * 2)), 2)

        odyssey_LR_MSTTR = helpers.calculate_LR_MSTTR(odyssey_full_text)
        odyssey_MSTTR = round(ld.msttr(odyssey_full_text, window_length=100), 4)
        odyssey_HDD = round(ld.hdd(odyssey_full_text), 4)
        odyssey_MTLD = round(ld.mtld(odyssey_full_text), 4)
        odyssey_TTR = round((odyssey_unique_words / odyssey_total_words) * 100, 2)
        odyssey_RTTR = round((odyssey_unique_words / math.sqrt(odyssey_total_words)), 2)
        odyssey_CTTR = round((odyssey_unique_words / math.sqrt(odyssey_total_words * 2)), 2)
        iliad_rows.append(
            ['iliad', book, iliad_TTR, iliad_RTTR, iliad_CTTR, iliad_LR_MSTTR, iliad_MSTTR, iliad_MTLD, iliad_HDD])
        odyssey_rows.append(
            ['odyssey', book, odyssey_TTR, odyssey_RTTR, odyssey_CTTR, odyssey_LR_MSTTR, odyssey_MSTTR,
             odyssey_MTLD, odyssey_HDD])

    iliad_lexical_diversity = pd.DataFrame(iliad_rows, columns=header)
    odyssey_lexical_diversity = pd.DataFrame(odyssey_rows, columns=header)
    if to_file:
        iliad_lexical_diversity.to_csv('data/iliad_lexical_diversity.csv')
        odyssey_lexical_diversity.to_csv('data/odyssey_lexical_diversity.csv')
    return [iliad_lexical_diversity, odyssey_lexical_diversity]


def count_hapax(corpus, to_file=True):
    """
    Counts hapax legomena (forms) for the Iliad and the Odyssey.

    Parameters
    ----------
    corpus : DataFrame
        contains text of Homeric corpus
    to_file: Boolean
        if True, save DataFrame to .csv

    Returns
    -------
    DataFrame
        statistics about hapax legomena (forms) for the Iliad and the Odyssey
    """
    iliad_vocab = defaultdict(int)
    odyssey_vocab = defaultdict(int)
    total_vocab = defaultdict(int)

    for ind, row in corpus.iterrows():
        tokens = row.string.split(" ")
        for token in tokens:
            if row['text'] == 'iliad':
                iliad_vocab[token] += 1
            else:
                odyssey_vocab[token] += 1
            total_vocab[token] += 1

    report = []
    header = ['word', 'corpus', 'iliad', 'odyssey']

    for word in total_vocab.keys():
        report.append([word, total_vocab[word], iliad_vocab[word], odyssey_vocab[word]])
    df = pd.DataFrame(report, columns=header)
    if to_file:
        df.to_csv('data/hapax.csv')
    return df


def hapax_distribution(corpus, to_file=True):
    """
    Find locations of hapax legomena within text.

    Parameters
    ----------
    corpus : DataFrame
        contains text of Homeric corpus
    to_file: Boolean
        if True, save DataFrame to .csv

    Returns
    -------
    DataFrame
        Locations of corpus-level hapax legomena within the Homeric corpus
    """
    all_counts = count_hapax(corpus)
    # get words that appear once in the corpus
    hapaxes = all_counts[all_counts.corpus == 1]
    locations = []
    header = ['word', 'text', 'book', 'line']
    print("Total hapaxes: ", len(hapaxes))
    num = 0
    for index, row in hapaxes.iterrows():
        num += 1
        if num % 100 == 0:
            print("still looking for hapax locations ", num, "/", len(hapaxes))
        for i, r in corpus.iterrows():
            tokens = r.string.split()
            if row['word'] in tokens:
                locations.append([row['word'],
                                  r['text'],
                                  r['book'],
                                  r['line']])
                break
    df = pd.DataFrame(locations, columns=header)
    if to_file:
        df.to_csv('data/hapax_locations.csv')
    return df


def proper_noun_stats(corpus, to_file=True):
    """
    Find locations of proper nouns within text.

    Parameters
    ----------
    corpus : DataFrame
        contains text of Homeric corpus and mutual expectancies
    to_file: Boolean
        if True, save DataFrame to .csv

    Returns
    -------
    DataFrame
        Locations of proper nouns within the Homeric corpus
    """
    print("Finding proper nouns within corpus...")
    # one dataframe with proper nouns and average ME of lines they appear in
    proper_nouns = []
    header1 = ['word', 'line_me']
    # one dataframe with number of proper nouns in line and line ME
    lines_with_proper_nouns = []
    header2 = ['text', 'book', 'line', 'string', 'me', 'num_proper_nouns', 'total_words', 'meter']
    # find lines with proper nouns
    for idx, row in corpus.iterrows():
        tokens = row['string'].split(" ")
        num_nouns = 0
        for tok in tokens:
            if tok[0].isupper():
                proper_nouns.append([tok, row['me']])
                num_nouns += 1
        if num_nouns > 0:
            lines_with_proper_nouns.append([row['text'], row['book'], row['line'], row['string'], row['me'],
                                            num_nouns, len(tokens), row['meter']])
    # save results to appropriate dataframes and return
    proper_nouns_df = pd.DataFrame(proper_nouns, columns=header1)
    proper_lines_df = pd.DataFrame(lines_with_proper_nouns, columns=header2)
    if to_file:
        proper_nouns_df.to_csv('data/proper_nouns_by_me.csv')
        proper_lines_df.to_csv('data/proper_lines_by_me.csv')
    return proper_nouns_df, proper_lines_df


def corpus_word_counts(corpus):
    all_words = defaultdict(int)
    for index,row in corpus.iterrows():
        tokens = row['string'].split(" ")
        for token in tokens:
            all_words[token] += 1
    return all_words


def compare_vocab_books(corpus, text1, book1, text2, book2):
    """
    Compares the vocabulary of two specific books in the Homeric corpus.
    Stores this information in a .csv file for easy data loading.
    CSV File location: data/compare_vocab_[text1][book1]_[text2][book2].csv

    Parameters
    ----------
    corpus : DataFrame
        contains text of Homeric corpus and mutual expectancies
    text1 : String
        name of the first text (Iliad or Odyssey)
    book1 : int
        book number of first text
    text2 : String
        name of the second text (Iliad or Odyssey)
    book2 : int
        book number of the second text

    Returns
    -------
    DataFrame
        contains all words in each book and their counts
    """
    text1 = text1.lower()
    text2 = text2.lower()

    lines1 = corpus[(corpus.text == text1) & (corpus.book == book1)]
    lines2 = corpus[(corpus.text == text2) & (corpus.book == book2)]

    vocab1 = defaultdict(int)
    vocab2 = defaultdict(int)

    for index, row in lines1.iterrows():
        tokens = row.string.split()
        for token in tokens:
            vocab1[token] += 1
    for index, row in lines2.iterrows():
        tokens = row.string.split()
        for token in tokens:
            vocab2[token] += 1

    all_vocab = set()
    all_rows = []

    for token in vocab1.keys():
        all_vocab.add(token)
    for token in vocab2.keys():
        all_vocab.add(token)
    corpus_counts = corpus_word_counts(corpus)
    for vocab in all_vocab:
        one = 0
        two = 0
        if vocab in vocab1.keys():
            one = vocab1[vocab]
        if vocab in vocab2.keys():
            two = vocab2[vocab]
        all_rows.append([vocab, one, two, corpus_counts[vocab]])
    header = ['word', text1 + "_" + str(book1), text2 + "_" + str(book2), 'corpus']
    df = pd.DataFrame(all_rows, columns=header)
    filename = 'data/compare_vocab_' + text1 + str(book1) + "_" + text2 + str(book2) + '.csv'
    df.to_csv(filename)


def cs_preprocess(corpus, target_text, target_book):
    """Returns text of book as a space-separated string.
    Used a preprocessing step for cosine similarity computation.

    Parameters
    ----------
    corpus : DataFrame
        contains text of Homeric corpus (recommend full_corpus)
    target_text : String
        name of the target text (Iliad or Odyssey)
    target_book : int
        book number of target book

    Returns
    -------
    string
        space-separated string of target book
    """
    target = corpus[(corpus['text'] == target_text) & (corpus['book'] == int(target_book))]
    word_list = []
    for index, row in target.iterrows():
        tokens = row['string'].split(" ")
        for token in tokens:
            word_list.append(token)
    return " ".join(word_list)


def cosine_similarity(corpus, text1, book1, text2, book2):
    """
    Compute the cosine similarity of two specific books in the Homeric corpus.

    Parameters
    ----------
    corpus : DataFrame
        contains text of Homeric corpus (recommend full_corpus)
    text1 : String
        name of the first text (Iliad or Odyssey)
    book1 : int
        book number of first text
    text2 : String
        name of the second text (Iliad or Odyssey)
    book2 : int
        book number of the second text

    Returns
    -------
    float
        cosine similarity of two specific books in the Homeric corpus
    """
    vectorized = TfidfVectorizer()
    matrix = vectorized.fit_transform([cs_preprocess(corpus, text1, book1), cs_preprocess(corpus, text2, book2)])
    return matrix[0].dot(matrix[1].T).toarray()[0][0]


def all_cosine_sims(corpus, to_file=True):
    """
    Computes cosine similarity for each pair of books in the corpus.

    Parameters
    ----------
    corpus : DataFrame
        contains text of Homeric corpus
    to_file: Boolean
        if True, save DataFrame to .csv

    Returns
    -------
    DataFrame
        cosine similarity for each pair of books in the Homeric corpus
    """
    all_sims = []
    for i in range(1, 25):
        for k in range(1, 25):
            all_sims.append(['iliad', i, 'iliad', k, cosine_similarity(corpus, 'iliad', i, 'iliad', k)])
            all_sims.append(['odyssey', i, 'odyssey', k, cosine_similarity(corpus, 'odyssey', i, 'odyssey', k)])
            all_sims.append(['iliad', i, 'odyssey', k, cosine_similarity(corpus, 'iliad', i, 'odyssey', k)])
    edited_all_sims = []
    for item in all_sims:
        add_me = True
        for added in edited_all_sims:
            if item[0] == added[2] and item[1] == added[3] and item[2] == added[0] and item[3] == added[1]:
                add_me = False
        if add_me:
            edited_all_sims.append(item)
    header = ['text1', 'book1', 'text2', 'book2', 'cosine_sim']
    sims_df = pd.DataFrame(edited_all_sims, columns=header)
    if to_file:
        sims_df.to_csv('data/cosine_similarities.csv')
    return sims_df

