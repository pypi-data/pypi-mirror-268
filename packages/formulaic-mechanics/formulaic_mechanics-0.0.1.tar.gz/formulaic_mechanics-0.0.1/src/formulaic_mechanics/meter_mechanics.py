import glob
import os
from collections import defaultdict
import pandas as pd
import scipy.stats as stats
import statsmodels.api as sm
import statsmodels.stats.multicomp as mc


def full_metrical_distribution(corpus, to_file=True):
    """
    Counts metrical patterns in the Homeric corpus.
    Stores this information in a .csv file for easy data loading.
    CSV File location: data/metrical_pattern_counts.csv

    Parameters
    ----------
    corpus : DataFrame
        contains text of Homeric corpus, including scansion of each line
    to_file : Boolean
        if True, save DataFrame to .csv

    Returns
    -------
    DataFrame
        contains counts of the 32 metrical patterns in the Homeric corpus
    """
    meters = defaultdict(int)
    for index, row in corpus.iterrows():
        meters[row['meter']] += 1
    rows = []
    for key in meters.keys():
        rows.append([key, meters[key]])
    df = pd.DataFrame(rows, columns=[['meter', 'full_count']])
    total_prevs = df['full_count'].sum()
    df['Full_percent'] = (df['full_count'] / total_prevs)
    if to_file:
        df.to_csv('data/metrical_pattern_counts.csv')
    return df


def get_hemistiches(to_file=True):
    """
    Reads all csv files in data/meter/meter_files to a pandas dataframe.

    Parameters
    ----------
    to_file : boolean
        if True, save DataFrame to .csv

    Returns
    -------
    DataFrame
        contains meters and hemistiches for each line in the Homeric corpus
    """
    path = os.getcwd() + '\data' + '\meter' + '\meter_files'
    csv_files = glob.glob(os.path.join(path, "*.csv"))
    all_files = []
    for file in csv_files:
        df = pd.read_csv(file)
        all_files.append(df)
        # print('File Name:', file.split("\\")[-1])
    meter_files = pd.concat(all_files, axis=0, ignore_index=True)
    if to_file:
        meter_files.to_csv('data/hemistiches.csv')
    return meter_files


def count_meters_by_text(corpus):
    """
    Returns a table with counts of meter types for the Iliad and the Odyssey.

    Parameters
    ----------
    corpus : DataFrame
        contains text of Homeric corpus, including scansion of each line (use corpus.full_corpus)

    Returns
    -------
    pivot_table
        counts of meter types for the Iliad and the Odyssey
    """
    corpus = corpus.groupby(['text', 'meter']).size().reset_index(name='counts')
    corpus = corpus.sort_values(by='counts', ascending=False)
    table = pd.pivot_table(corpus, values='counts', index='meter', columns='text').reset_index()
    table.columns = ['meter', 'iliad', 'odyssey']
    table['canon'] = table[['iliad', 'odyssey']].sum(axis=1)
    table['iliad_per'] = (table['iliad'] / table['iliad'].sum()) * 100
    table['odyssey_per'] = (table['odyssey'] / table['odyssey'].sum()) * 100
    table['canon_per'] = (table['canon'] / table['canon'].sum()) * 100
    return table


def count_feet(corpus, to_file=True):
    """
    Counts feet shapes (dactyl, spondee, anceps) in the Homeric corpus.
    Stores this information in a .csv file for easy data loading.
    CSV File location: data/feet_shape_counts.csv

    Parameters
    ----------
    corpus : DataFrame
        contains text of Homeric corpus, including scansion of each line (use Corpus.full_corpus)
    to_file : Boolean
        if True, save DataFrame to .csv

    Returns
    -------
    DataFrame
        contains counts feet shapes in the Homeric corpus
    """
    concatenated_canon = corpus['meter'].str.cat()
    concatenated_iliad = corpus[corpus.text == 'iliad']['meter'].str.cat()
    concatenated_odyssey = corpus[corpus.text == 'odyssey']['meter'].str.cat()
    feet = {'canon_total': len(concatenated_canon),
            'canon_spondees': concatenated_canon.count('S'),
            'canon_dactyls': concatenated_canon.count('D'),
            'canon_ancipites': concatenated_canon.count('A'),
            'canon_unknown': concatenated_canon.count('N'),
            'iliad_total': len(concatenated_iliad),
            'iliad_spondees': concatenated_iliad.count('S'),
            'iliad_dactyls': concatenated_iliad.count('D'),
            'iliad_ancipites': concatenated_iliad.count('A'),
            'odyssey_total': len(concatenated_odyssey),
            'odyssey_spondees': concatenated_odyssey.count('S'),
            'odyssey_dactyls': concatenated_odyssey.count('D'),
            'odyssey_ancipites': concatenated_odyssey.count('A')}
    feet_df = pd.DataFrame.from_dict(feet, orient='index')
    feet_df.columns = ['count']
    if to_file:
        feet_df.to_csv('data/feet_shape_counts.csv')
    return feet_df


def count_unit(meters, unit, foot):
    """
    Helper method for dactyl/spondee counts.

    Parameters
    ----------
    meters : list
        list of lists; each sub-list is a meter string (e.g. DSDSDA)
    unit : string
        'D' or 'S'; unit to count
    foot : int
        in which foot to count unit types

    Returns
    -------
    int
        count of `unit` in `foot` position in `meters`
    """
    count = 0
    for line in meters:
        if line[foot - 1] == unit:
            count += 1
    return count


def foot_type_and_position(corpus, to_file=False):
    """
    Counts feet shapes (dactyl, spondee, anceps) in line locations in the Homeric corpus.
    Stores this information in a .csv file for easy data loading.
    CSV File location: data/foot_shapes_by_position_counts.csv

    Parameters
    ----------
    corpus : DataFrame
        contains text of Homeric corpus, including scansion of each line (use Corpus.full_corpus)
    to_file : Boolean
        if True, save DataFrame to .csv

    Returns
    -------
    DataFrame
        contains counts feet shapes in the Homeric corpus, grouped by foot position
    """
    canon = corpus['meter'].tolist()
    iliad = corpus[corpus.text == 'iliad']['meter'].tolist()
    odyssey = corpus[corpus.text == 'odyssey']['meter'].tolist()
    ftp_df = pd.DataFrame({'canon_dactyl': [count_unit(canon, 'D', 1),
                                            count_unit(canon, 'D', 2),
                                            count_unit(canon, 'D', 3),
                                            count_unit(canon, 'D', 4),
                                            count_unit(canon, 'D', 5),
                                            count_unit(canon, 'D', 6)],
                           'canon_spondee': [count_unit(canon, 'S', 1),
                                             count_unit(canon, 'S', 2),
                                             count_unit(canon, 'S', 3),
                                             count_unit(canon, 'S', 4),
                                             count_unit(canon, 'S', 5),
                                             count_unit(canon, 'S', 6)],
                           'iliad_dactyl': [count_unit(iliad, 'D', 1),
                                            count_unit(iliad, 'D', 2),
                                            count_unit(iliad, 'D', 3),
                                            count_unit(iliad, 'D', 4),
                                            count_unit(iliad, 'D', 5),
                                            count_unit(iliad, 'D', 6)],
                           'iliad_spondee': [count_unit(iliad, 'S', 1),
                                             count_unit(iliad, 'S', 2),
                                             count_unit(iliad, 'S', 3),
                                             count_unit(iliad, 'S', 4),
                                             count_unit(iliad, 'S', 5),
                                             count_unit(iliad, 'S', 6)],
                           'odyssey_dactyl': [count_unit(odyssey, 'D', 1),
                                              count_unit(odyssey, 'D', 2),
                                              count_unit(odyssey, 'D', 3),
                                              count_unit(odyssey, 'D', 4),
                                              count_unit(odyssey, 'D', 5),
                                              count_unit(odyssey, 'D', 6)],
                           'odyssey_spondee': [count_unit(odyssey, 'S', 1),
                                               count_unit(odyssey, 'S', 2),
                                               count_unit(odyssey, 'S', 3),
                                               count_unit(odyssey, 'S', 4),
                                               count_unit(odyssey, 'S', 5),
                                               count_unit(odyssey, 'S', 6)]})

    if to_file:
        ftp_df.to_csv('data/foot_shapes_by_position_counts.csv')
    return ftp_df


def convert_ftp_to_percent(corpus, to_file=False):
    """
    Counts feet shapes (dactyl, spondee, anceps) in line locations in the Homeric corpus.
    Converts those counts to percents and stores information in dataframe.
    This is the same method as `foot_type_and_position`, but returns percentages.
    Stores this information in a .csv file for easy data loading.
    CSV File location: data/foot_shapes_by_position_counts.csv

    Parameters
    ----------
    corpus : DataFrame
        contains text of Homeric corpus, including scansion of each line (use Corpus.full_corpus)
    to_file : Boolean
        if True, save DataFrame to .csv

    Returns
    -------
    DataFrame
        contains percents/frequencies of feet shapes in the Homeric corpus, grouped by foot position
    """
    canon = corpus['meter'].tolist()
    iliad = corpus[corpus.text == 'iliad']['meter'].tolist()
    odyssey = corpus[corpus.text == 'odyssey']['meter'].tolist()
    ftp_df = pd.DataFrame({'canon_dactyl': [(count_unit(canon, 'D', 1) / len(canon)) * 100,
                                            (count_unit(canon, 'D', 2) / len(canon)) * 100,
                                            (count_unit(canon, 'D', 3) / len(canon)) * 100,
                                            (count_unit(canon, 'D', 4) / len(canon)) * 100,
                                            (count_unit(canon, 'D', 5) / len(canon)) * 100,
                                            (count_unit(canon, 'D', 6) / len(canon)) * 100],
                           'canon_spondee': [(count_unit(canon, 'S', 1) / len(canon)) * 100,
                                             (count_unit(canon, 'S', 2) / len(canon)) * 100,
                                             (count_unit(canon, 'S', 3) / len(canon)) * 100,
                                             (count_unit(canon, 'S', 4) / len(canon)) * 100,
                                             (count_unit(canon, 'S', 5) / len(canon)) * 100,
                                             (count_unit(canon, 'S', 6) / len(canon)) * 100],
                           'iliad_dactyl': [(count_unit(iliad, 'D', 1) / len(iliad)) * 100,
                                            (count_unit(iliad, 'D', 2) / len(iliad)) * 100,
                                            (count_unit(iliad, 'D', 3) / len(iliad)) * 100,
                                            (count_unit(iliad, 'D', 4) / len(iliad)) * 100,
                                            (count_unit(iliad, 'D', 5) / len(iliad)) * 100,
                                            (count_unit(iliad, 'D', 6) / len(iliad)) * 100],
                           'iliad_spondee': [(count_unit(iliad, 'S', 1) / len(iliad)) * 100,
                                             (count_unit(iliad, 'S', 2) / len(iliad)) * 100,
                                             (count_unit(iliad, 'S', 3) / len(iliad)) * 100,
                                             (count_unit(iliad, 'S', 4) / len(iliad)) * 100,
                                             (count_unit(iliad, 'S', 5) / len(iliad)) * 100,
                                             (count_unit(iliad, 'S', 6) / len(iliad)) * 100],
                           'odyssey_dactyl': [(count_unit(odyssey, 'D', 1) / len(odyssey)) * 100,
                                              (count_unit(odyssey, 'D', 2) / len(odyssey)) * 100,
                                              (count_unit(odyssey, 'D', 3) / len(odyssey)) * 100,
                                              (count_unit(odyssey, 'D', 4) / len(odyssey)) * 100,
                                              (count_unit(odyssey, 'D', 5) / len(odyssey)) * 100,
                                              (count_unit(odyssey, 'D', 6) / len(odyssey)) * 100],
                           'odyssey_spondee': [(count_unit(odyssey, 'S', 1) / len(odyssey)) * 100,
                                               (count_unit(odyssey, 'S', 2) / len(odyssey)) * 100,
                                               (count_unit(odyssey, 'S', 3) / len(odyssey)) * 100,
                                               (count_unit(odyssey, 'S', 4) / len(odyssey)) * 100,
                                               (count_unit(odyssey, 'S', 5) / len(odyssey)) * 100,
                                               (count_unit(odyssey, 'S', 6) / len(odyssey)) * 100]})
    if to_file:
        ftp_df.to_csv('data/foot_shapes_by_position_percents')
    return ftp_df


def feet_by_book(corpus, to_file=False):
    """
    Counts feet shapes (dactyl, spondee, anceps) grouped by book in the Homeric corpus.
    Optionally stores this information in a .csv file for easy data loading.
    CSV File location: data/dactyls_spondees_by_book.csv

    Parameters
    ----------
    corpus : DataFrame
        contains text of Homeric corpus, including scansion of each line (use Corpus.full_corpus)
    to_file : Boolean
        if True, save DataFrame to .csv

    Returns
    -------
    DataFrame
        contains feet shapes (dactyl, spondee, anceps) grouped by book
    """
    iliad = corpus[corpus.text == 'iliad']
    odyssey = corpus[corpus.text == 'odyssey']
    rows = []
    odyssey_rows = []
    for i in range(1, 25):
        iliad_book = iliad[iliad.book == i]['meter'].to_list()
        d_icount = 0
        s_icount = 0
        a_icount = 0
        for strings in iliad_book:
            for character in strings:
                if character == 'D':
                    d_icount += 1
                elif character == 'S':
                    s_icount += 1
                elif character == 'A':
                    a_icount += 1
        di = (d_icount / (d_icount + s_icount + a_icount)) * 100
        si = (s_icount / (d_icount + s_icount + a_icount)) * 100
        rows.append(['iliad', i, di, si])
        odyssey_book = odyssey[odyssey.book == i]['meter'].to_list()
        d_ocount = 0
        s_ocount = 0
        a_ocount = 0
        for strings in odyssey_book:
            for character in strings:
                if character == 'D':
                    d_ocount += 1
                elif character == 'S':
                    s_ocount += 1
                elif character == 'A':
                    a_ocount += 1
        do = (d_ocount / (d_ocount + s_ocount + a_ocount)) * 100
        so = (s_ocount / (d_ocount + s_ocount + a_ocount)) * 100
        rows.append(['odyssey', i, do, so])
    df = pd.DataFrame(rows, columns=['text', 'book', 'dactyls', 'spondees'])
    if to_file:
        df.to_csv('data/dactyls_spondees_by_book.csv')
    return df


def oneway_anova_meter_me(corpus):
    """
    Performs a one-way ANOVA using metrical pattern as the independent variable and mutual expectancy as the
    dependent variable.

    Parameters
    ----------
    corpus : DataFrame
        use corpus.full_corpus

    Returns
    -------
    float
        computed F statistic of the test
    float
        the associated p-value from the F distribution
    """
    return stats.f_oneway(corpus[corpus.meter == 'DDSDDA']['me'],
                          corpus[corpus.meter == 'DSDSDA']['me'],
                          corpus[corpus.meter == 'SSSDDA']['me'],
                          corpus[corpus.meter == 'SSDDDA']['me'],
                          corpus[corpus.meter == 'SDDDDA']['me'],
                          corpus[corpus.meter == 'SSDSDA']['me'],
                          corpus[corpus.meter == 'DDSSDA']['me'],
                          corpus[corpus.meter == 'DDDDDA']['me'],  # end line 1
                          corpus[corpus.meter == 'DSSDSA']['me'],
                          corpus[corpus.meter == 'DSDDSA']['me'],
                          corpus[corpus.meter == 'DSSDDA']['me'],
                          corpus[corpus.meter == 'DDDSDA']['me'],
                          corpus[corpus.meter == 'SDDSDA']['me'],
                          corpus[corpus.meter == 'DSDDDA']['me'],
                          corpus[corpus.meter == 'DDDDSA']['me'],
                          corpus[corpus.meter == 'DSSSDA']['me'],  # end line 1
                          corpus[corpus.meter == 'SDSDDA']['me'],
                          corpus[corpus.meter == 'SSSSDA']['me'],
                          corpus[corpus.meter == 'SDSSDA']['me'],
                          corpus[corpus.meter == 'SDDDSA']['me'],
                          corpus[corpus.meter == 'DDDSSA']['me'],
                          corpus[corpus.meter == 'DDSDSA']['me'],
                          corpus[corpus.meter == 'DDSSSA']['me'],
                          corpus[corpus.meter == 'SDSDSA']['me'],  # end line 3 (exclude NNNNNN)
                          corpus[corpus.meter == 'SDDSSA']['me'],
                          corpus[corpus.meter == 'DSDSSA']['me'],
                          corpus[corpus.meter == 'SSDDSA']['me'],
                          corpus[corpus.meter == 'SSDSSA']['me'],
                          corpus[corpus.meter == 'SSSDSA']['me'],
                          corpus[corpus.meter == 'DSSSSA']['me'],
                          corpus[corpus.meter == 'SDSSSA']['me'],
                          corpus[corpus.meter == 'SSSSSA']['me'], )


def tukey_hsd_meter_me(corpus):
    """
    Performs a Tukey HSD post-hoc test.

    Parameters
    ----------
    corpus : DataFrame
        use corpus.full_corpus

    Returns
    -------
    string
        summary of post-hoc test results
    """
    comp = mc.MultiComparison(corpus['me'], corpus['meter'])
    post_hoc_res = comp.tukeyhsd()
    return post_hoc_res.summary()


def metrical_pattern_linear_regression(corpus):
    """
    Performs a linear regression using metrical pattern as the independent variable and mutual expectancy as the
    dependent variable. Prints model summary.

    Parameters
    ----------
    corpus : DataFrame
        use corpus.full_corpus

    Returns
    -------
    model
        linear regression model
    """
    X = corpus['meter']  # me_by_line_df
    independent = pd.get_dummies(data=X, drop_first=True)
    independent = sm.add_constant(independent)
    dependent = corpus['me']
    model = sm.OLS(dependent, independent).fit()
    print(model.summary())
    return model


def foot_placement_linear_regression():
    """
    Performs a linear regression using metrical foot as the independent variable and spondee/dactyl as the
    dependent variable. Prints model summary. Relies on data/me_by_line_meter_split.csv.

    Returns
    -------
    model
        linear regression model
    """
    csv = pd.read_csv('../data/me_by_line_meter_split.csv')
    csv = csv[csv.foot1 != "N"]
    csv = csv.replace({'D': 1, 'S': 0})
    independent = csv[['foot1', 'foot2', 'foot3', 'foot4', 'foot5']]
    independent = sm.add_constant(independent)
    dependent = csv['me']
    model = sm.OLS(dependent, independent).fit()
    print(model.summary())
    return model


def avg_me_by_foot_placement():
    """
    Calculates average mutual expectancy for each possible foot configuration. Relies on
    data/me_by_line_meter_split.csv.

    Returns
    -------
    dictionary
        average mutual expectancy by foot and shape
    """
    split = pd.read_csv('../data/me_by_line_meter_split.csv')
    foot_me = {'foot1S': split[split.foot1 == 'S']['me'].mean(),
               'foot1D': split[split.foot1 == 'D']['me'].mean(),
               'foot2S': split[split.foot2 == 'S']['me'].mean(),
               'foot2D': split[split.foot2 == 'D']['me'].mean(),
               'foot3S': split[split.foot3 == 'S']['me'].mean(),
               'foot3D': split[split.foot3 == 'D']['me'].mean(),
               'foot4S': split[split.foot4 == 'S']['me'].mean(),
               'foot4D': split[split.foot4 == 'D']['me'].mean(),
               'foot5S': split[split.foot5 == 'S']['me'].mean(),
               'foot5D': split[split.foot5 == 'D']['me'].mean()}
    return foot_me


def describe_caesura_data(caesura_df):
    """
    Prints out information about caesura distributions in the Homeric corpus.

    Parameters
    ----------
    caesura_df : DataFrame
        contains text of Homeric corpus, including scansion of each line
    """
    caesura_df['len_hemi1'] = caesura_df['first_hemistich'].str.count(' ') + 1
    caesura_df['len_hemi2'] = caesura_df['second_hemistich'].str.count(' ') + 1
    print("FULL CANON")
    print(caesura_df[['len_hemi1', 'len_hemi2']].describe())
    print()
    print("ILIAD")
    print(caesura_df[caesura_df.text == 'iliad'][['len_hemi1', 'len_hemi2']].describe())
    print()
    print("ODYSSEY")
    print(caesura_df[caesura_df.text == 'odyssey'][['len_hemi1', 'len_hemi2']].describe())


def compare_meter(corpus1, corpus2):
    """
    Compares the numbers of dactyls and spondees in two given corpora.

    Parameters
    ----------
    corpus1 : DataFrame
        first corpus to use

    corpus2: DataFrame
        second corpus to use

    Returns
    -------
    dictionary
        Contains numbers of dactyls and spondees in two given corpora
    """
    meter1 = corpus1['meter'].to_list()
    meter2 = corpus2['meter'].to_list()
    m1d, m1s, m1a, m1n, m2d, m2s, m2a, m2n = 0, 0, 0, 0, 0, 0, 0, 0
    for meter in meter1:
        for character in meter:
            if character == 'D':
                m1d += 1
            elif character == 'S':
                m1s += 1
            elif character == 'A':
                m1a += 1
            elif character == 'N':
                m1n += 1
    for meter in meter2:
        for character in meter:
            if character == 'D':
                m2d += 1
            elif character == 'S':
                m2s += 1
            elif character == 'A':
                m2a += 1
            elif character == 'N':
                m2n += 1
    df = {'meter1_dactyls': m1d,
          'meter1_spondees': m1s,
          'meter1_ancipites': m1a,
          'meter1_notscanned': m1n,
          'meter2_dactyls': m2d,
          'meter2_spondees': m2s,
          'meter2_ancipites': m2a,
          'meter2_notscanned': m2n
          }
    return df
