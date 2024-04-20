import statistics
import pandas as pd
from . import helpers


def expectancy(phrase, expectancies):
    """
    Calculates mutual expectancy for a phrase of line-length or less.

    Parameters
    ----------
    phrase : String
        target phrase to calculate mutual expectancy
    expectancies : DataFrame
        contains all bigrams and their expectancies

    Returns
    -------
    Float
        mutual expectancy for given phrase
    """
    tokens = phrase.split(" ")
    if len(tokens) < 2:
        (phrase)
        return 'N'
    freqs = []
    bigrams = []
    for i in range(len(tokens) - 1):
        bigrams.append([tokens[i], tokens[i + 1]])
    for w1, w2 in bigrams:
        b_row = expectancies[(expectancies.W1 == w1) & (expectancies.W2 == w2)]
        if len(b_row['me']) != 1:
            print(w1, ' ', w2)
        freqs.append(b_row['me'].item())
    return statistics.geometric_mean(freqs)


def geometric_passage_expectancy(passage, bigram_expectancies, split_on='\n'):
    """
    Calculates (geometric) mutual expectancy for a passage (more than length of a line).
    Not recommended; Recommend use arithmetic passage expectancy.

    Parameters
    ----------
    passage : String
        target passage to calculate mutual expectancy
    split_on : String
        demarcates new lines in passage
    bigram_expectancies : DataFrame
        contains all bigrams and their expectancies

    Returns
    -------
    Float
        geometric mutual expectancy for given passage
    """
    lines = passage.split(split_on)
    expectancies = []
    for line in lines:
        exp = expectancy(line.strip(), bigram_expectancies)
        if exp == 'N':
            continue
        else:
            expectancies.append(exp)
    return statistics.geometric_mean(expectancies)


def arithmetic_passage_expectancy(passage, bigram_expectancies, split_on='\n'):
    """
    Calculates arithmetic mutual expectancy for a passage (more than length of a line).

    Parameters
    ----------
    passage : String
        target passage to calculate mutual expectancy
    split_on : String
        demarcates new lines in passage
    bigram_expectancies : DataFrame
        contains all bigrams and their expectancies

    Returns
    -------
    Float
        arithmetic mutual expectancy for given passage
    """
    lines = passage.split(split_on)
    expectancies = []
    for line in lines:
        exp = expectancy(line.strip(), bigram_expectancies)
        if exp == 'N':
            continue
        else:
            expectancies.append(exp)
    return statistics.mean(expectancies)


def me_by_book_geometric(corpus, bigram_expectancies, to_file=True):
    """
    NOT RECOMMENDED: USE ARITHMETIC MUTUAL EXPECTANCY FOR PASSAGE-LENGTH TEXT
    Computes geometric mutual expectancy for each book in the Homeric corpus.
    Stores this information in a .csv file for easy data loading.
    CSV File location: data/me_by_book_geometric.csv

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
        contains computed geometric expectancies for each book in the Homeric corpus
    """
    rows = []
    header = ['text', 'book', 'me']
    for book in range(1, 25):
        print("Calculating m.e. for Iliad book ", str(book), "...")
        iliad_book = corpus[(corpus['text'] == 'iliad') & (corpus['book'] == book)]
        iliad_lines = ""
        for index, row in iliad_book.iterrows():
            iliad_lines += row['string'] + "\n "
        iliad_lines = iliad_lines[:-2]
        iliad_me = geometric_passage_expectancy(iliad_lines, bigram_expectancies)
        rows.append(['iliad', book, iliad_me])

        print("Calculating m.e. for Odyssey book ", str(book), "...")
        odyssey_book = corpus[(corpus['text'] == 'odyssey') & (corpus['book'] == book)]
        odyssey_lines = ""
        for index, row in odyssey_book.iterrows():
            odyssey_lines += row['string'] + "\n "
        odyssey_lines = odyssey_lines[:-2]
        odyssey_me = geometric_passage_expectancy(odyssey_lines, bigram_expectancies)
        rows.append(['odyssey', book, odyssey_me])
    df = pd.DataFrame(rows, columns=header)
    if to_file:
        df.to_csv('data/me_by_book_geometric.csv')
    return df


def me_by_book_arithmetic(corpus, bigram_expectancies, to_file=True):
    """
    RECOMMENDED FOR PASSAGE-LENGTH TEXT
    Computes arithmetic mutual expectancy for each book in the Homeric corpus.
    Stores this information in a .csv file for easy data loading.
    CSV File location: data/me_by_book_arithmetic.csv

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
        contains computed arithmetic expectancies for each book in the Homeric corpus
    """
    rows = []
    header = ['text', 'book', 'me']
    for book in range(1, 25):
        print("Calculating m.e. for Iliad book ", str(book), "...")
        iliad_book = corpus[(corpus['text'] == 'iliad') & (corpus['book'] == book)]
        iliad_lines = ""
        for index, row in iliad_book.iterrows():
            iliad_lines += row['string'] + "\n "
        iliad_lines = iliad_lines[:-2]
        iliad_me = arithmetic_passage_expectancy(iliad_lines, bigram_expectancies)
        rows.append(['iliad', book, iliad_me])

        print("Calculating m.e. for Odyssey book ", str(book), "...")
        odyssey_book = corpus[(corpus['text'] == 'odyssey') & (corpus['book'] == book)]
        odyssey_lines = ""
        for index, row in odyssey_book.iterrows():
            odyssey_lines += row['string'] + "\n "
        odyssey_lines = odyssey_lines[:-2]
        odyssey_me = arithmetic_passage_expectancy(odyssey_lines, bigram_expectancies)
        rows.append(['odyssey', book, odyssey_me])
    df = pd.DataFrame(rows, columns=header)
    if to_file:
        df.to_csv('data/me_by_book_arithmetic.csv')
    return df


def me_by_line(corpus, bigram_expectancies, to_file=True):
    """
    Computes  mutual expectancy for each line in the Homeric corpus.
    Stores this information in a .csv file for easy data loading.
    CSV File location: data/me_by_line.csv

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
        contains mutual expectancy for each line in the Homeric corpus
    """
    new_rows = []
    header = ['text', 'book', 'line', 'string', 'meter', 'me']
    meter_df = helpers.meter_files_to_df()
    counter = 1
    for index, row in corpus.iterrows():
        if counter % 1000 == 0:
            print("Still working on lines: ", str(counter))
        text = row['text']
        book = row['book']
        line = row['line']
        strn = row['string']
        meter = meter_df[(meter_df.text == text) & (meter_df.book == book) & (meter_df.line == line)][
            'meter'].item()
        me = expectancy(row['string'].strip(), bigram_expectancies)
        new_rows.append([text, book, line, strn, meter, me])
        counter += 1
    df = pd.DataFrame(new_rows, columns=header)
    if to_file:
        df.to_csv('data/me_by_line.csv')
    return df


def me_by_meter(corpus, to_file=True):
    """
    Computes (arithmetic)  mutual expectancy for each metrical pattern in the Homeric corpus.
    Stores this information in a .csv file for easy data loading.
    CSV File location: data/me_by_meter.csv

    Parameters
    ----------
    corpus : DataFrame
        contains text of Homeric corpus
    to_file : Boolean
        if True, save DataFrame to .csv

    Returns
    -------
    DataFrame
        contains mutual expectancy for each metrical pattern in the Homeric corpus
    """
    rows = []
    all_meters = corpus['meter'].unique()
    header = ['meter', 'me']
    for metrical_pattern in all_meters:
        print("Calculating m.e. for metrical pattern ", metrical_pattern, "...")
        meter_lines_current = corpus[corpus.meter == metrical_pattern]
        current_me = meter_lines_current['me'].mean()
        rows.append([metrical_pattern, current_me])
    df = pd.DataFrame(rows, columns=header)
    if to_file:
        df.to_csv('data/me_by_meter.csv')
    return df


def same_me_diff_count_bigrams(bigram_expectancies, to_file=True):
    """
    Finds all bigrams with same frequencies and different counts.
    Stores this information in a .csv file for easy data loading.
    CSV File location: data/same_me_diff_count_bigrams.csv

    Parameters
    ----------
    bigram_expectancies : DataFrame
        contains all bigrams and their expectancies
    to_file : Boolean
        if True, save DataFrame to .csv

    Returns
    -------
    DataFrame
        all bigrams with same frequencies and different counts
    """
    results = []
    header = ['bigram1_W1',
              'bigram1_W2',
              'bigram1_for_freq',
              'bigram1_back_freq',
              'bigram1_count',
              'bigram2_W1',
              'bigram2_W2',
              'bigram2_for_freq',
              'bigram2_back_freq',
              'bigram2_count',
              'same_frequency',
              'different_count']
    for index, row in bigram_expectancies.iterrows():
        W1 = row['W1']
        W2 = row['W2']
        forward = row['forward_freq']
        backward = row['backward_freq']
        count = row['count']
        for i, r in bigram_expectancies.iterrows():
            if W1 == r['W1'] and W2 == r['W2']:
                continue
            else:
                same_freq = False
                diff_count = False
                if forward == r['forward_freq'] and backward == r['backward_freq']:
                    same_freq = True
                    if count != r['count']:
                        diff_count = True
                results.append([W1, W2, forward, backward, count,
                                r['W1'], r['W2'],
                                r['forward_freq'], r['backward_freq'], r['count'],
                                same_freq, diff_count])
        results_df = pd.DataFrame(results, columns=header)
        if to_file:
            results_df.to_csv('data/same_me_diff_count_bigrams.csv')
        return results
