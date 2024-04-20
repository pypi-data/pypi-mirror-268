import pandas as pd
from collections import defaultdict
from statistics import geometric_mean
from . import mutual_expectancy


def count_bigrams(corpus, quiet=False):
    """
    Counts all bigrams in the Homeric corpus.

    Parameters
    ----------
    corpus : DataFrame
        contains text of Homeric corpus
    quiet : boolean
        If True, include print statements.
        
    Returns
    -------
    DataFrame
        contains all bigrams and their counts
    """
    if not quiet:
        print("Counting bigrams...")
    bigrams_dict = defaultdict(int)
    for line in corpus['string'].to_list():
        tokens = line.split(" ")
        for i in range(len(tokens) - 1):
            bigrams_dict[(tokens[i].strip(), tokens[i + 1].strip())] += 1
    bigrams = pd.Series(bigrams_dict, dtype='float64').reset_index()
    bigrams.columns = ['W1', 'W2', 'count']
    return bigrams


def filemaker_bigram_frequency(bigrams, to_file=True):
    """
    Computes forward and backward frequency of each bigram in the Homeric corpus.
    Stores this information in a .csv file for easy data loading.
    CSV File location: data/bigram_frequencies.csv

    Parameters
    ----------
    bigrams : DataFrame
        contains all bigrams, columns are word1, word2, and count
        obtain from n_grams.count_bigrams
    to_file : Boolean
        if True, save DataFrame to .csv

    Returns
    -------
    DataFrame
        contains all bigrams and their forward and backward frequencies
    """
    print("Making bigram frequency file...")
    bigram_freqs = []
    header = ['W1', 'W2', 'count', 'forward_freq', 'backward_freq']
    index_count = 0
    for index, row in bigrams.iterrows():
        if index_count % 10000 == 0:
            print("Processed: ", index_count)
        word_one = row['W1']
        word_two = row['W2']
        bi_count = row['count']

        word_one_appearances = (bigrams[bigrams.W1 == word_one])['count'].sum()
        forward_freq = bi_count / word_one_appearances

        word_two_appearances = (bigrams[bigrams.W2 == word_two])['count'].sum()
        backward_freq = bi_count / word_two_appearances
        bigram_freqs.append([word_one, word_two, bi_count, forward_freq, backward_freq])
        index_count += 1
    freq_df = pd.DataFrame(bigram_freqs, columns=header)
    if to_file:
        freq_df.to_csv('data/bigram_frequencies.csv')
    return freq_df


def filemaker_bigram_expectancy(bigram_frequencies, to_file=True):
    """
    Computes mutual expectancy of each bigram in the Homeric corpus.
    Stores this information in a .csv file for easy data loading.
    CSV File location: data/bigram_expectancies.csv

    Parameters
    ----------
    bigram_frequencies : DataFrame
        contains all bigrams and their forward and backward frequencies
        obtain from n_grams.filemaker_bigram_frequency
    to_file : Boolean
        if True, save DataFrame to .csv

    Returns
    -------
    DataFrame
        contains all bigrams and their expectancies
    """
    print("Making bigram expectancy file...")
    header = ['W1', 'W2', 'count', 'forward_freq', 'backward_freq', 'me']
    me_rows = []
    index_count = 0
    for index, row in bigram_frequencies.iterrows():
        if index_count % 10000 == 0:
            print("Processed: ", index_count)
        me = (geometric_mean([row['forward_freq'], row['backward_freq']])) * row['count']
        me_rows.append([row['W1'], row['W2'], row['count'], row['forward_freq'], row['backward_freq'], me])
        index_count += 1
    me_df = pd.DataFrame(me_rows, columns=header)
    if to_file:
        me_df.to_csv('data/bigram_expectancies.csv')
    return me_df


def count_trigrams(corpus, expectancies, to_file=True):
    """
    Computes mutual expectancy of each trigram in the Homeric corpus.
    Stores this information in a .csv file for easy data loading.
    CSV File location: data/trigram_expectancies.csv

    Parameters
    ----------
    corpus : DataFrame
        contains text of Homeric corpus
    expectancies : DataFrame
        contains all bigrams and their expectancies
    to_file : Boolean
        if True, save DataFrame to .csv

    Returns
    -------
    DataFrame
        contains all trigrams and their expectancies
    """
    print("Making trigram expectancies file...")
    trigrams_dict = defaultdict(int)
    for line in corpus['string'].to_list():
        tokens = line.split(" ")
        for i in range(len(tokens) - 2):
            trigrams_dict[(tokens[i].strip(), tokens[i + 1].strip(), tokens[i + 2].strip())] += 1
    rows = []
    test = 0
    print("Total trigrams... ", len(trigrams_dict.keys()))
    for key in trigrams_dict.keys():
        if test % 1000 == 0:
            print("Still working...", test)
        word_one = key[0]
        word_two = key[1]
        word_thr = key[2]
        count = trigrams_dict[key]
        line = word_one + " " + word_two + " " + word_thr
        expec = mutual_expectancy.expectancy(line, expectancies)
        rows.append([word_one, word_two, word_thr, count, expec])
        test += 1
    header = ['W1', 'W2', 'W3', 'count', 'me']
    df = pd.DataFrame(rows, columns=header)
    if to_file:
        df.to_csv('data/trigram_expectancies.csv')
    return df


def count_quadgrams(corpus, expectancies, to_file=True):
    """
    Computes mutual expectancy of each quadgram in the Homeric corpus.
    Stores this information in a .csv file for easy data loading.
    CSV File location: data/trigram_expectancies.csv

    Parameters
    ----------
    corpus : DataFrame
        contains text of Homeric corpus
    expectancies : DataFrame
        contains all bigrams and their expectancies
    to_file : Boolean
        if True, save DataFrame to .csv

    Returns
    -------
    DataFrame
        contains all quadgrams and their expectancies
    """
    print("Making quadgram expectancies file...")
    quadgrams_dict = defaultdict(int)
    for line in corpus['string'].to_list():
        tokens = line.split(" ")
        for i in range(len(tokens) - 3):
            quadgrams_dict[
                (tokens[i].strip(), tokens[i + 1].strip(), tokens[i + 2].strip(), tokens[i + 3].strip())] += 1
    rows = []
    test = 0
    print("Total quadgrams... ", len(quadgrams_dict.keys()))
    for key in quadgrams_dict.keys():
        if test % 1000 == 0:
            print("Still working...", test)
        word_one = key[0]
        word_two = key[1]
        word_thr = key[2]
        word_fou = key[3]
        count = quadgrams_dict[key]
        line = word_one + " " + word_two + " " + word_thr + " " + word_fou
        expec = mutual_expectancy.expectancy(line, expectancies)
        rows.append([word_one, word_two, word_thr, word_fou, count, expec])
        test += 1
    header = ['W1', 'W2', 'W3', 'W4', 'count', 'me']
    df = pd.DataFrame(rows, columns=header)
    if to_file:
        df.to_csv('data/quadgram_expectancies.csv')
    return df
