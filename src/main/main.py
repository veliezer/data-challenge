import pandas as pd
from sqlite3 import connect
import queries

results_file = '../../data/result.csv'
consoles_file = '../../data/consoles.csv'
report = r'../../data/report-walmart.txt'
header_1 = '\nTHE TOP 10 GAMES FOR ALL CONSOLES\n'
header_2 = '\nTHE WORST 10 GAMES FOR ALL CONSOLES\n'
header_3 = '\nTHE TOP 10 GAMES FOR EACH CONSOLE/COMPANY\n'
header_4 = '\nTHE WORST 10 GAMES FOR EACH CONSOLE/COMPANY\n'
convert_dict = {'userscore': float}

def read_data_from_csv(csv_file):
    return pd.read_csv(csv_file)

#deleting cols that cannot be casted to numeric(float)
def remove_data(df, column):
    return df.drop(df.loc[df[column].str.contains('[A-Za-z]')].index, inplace=True)

#removing leading and trailing blank spaces on selected col
def clean_blank_spaces(df, column):
    df[column] = pd.Series(df[column]).str.strip()

    return df

def adding_average(df, column):
    #userscore is multiplied by 10 to level userscore and metascore up to the same scale
    df[column] = ((df['userscore']*10) + df['metascore'])/2

    return df

def get_connection():
    conn = connect(':memory:')
    conn.text_factory = str

    return conn

def main_():
    cnx = get_connection()
    df_results = read_data_from_csv(results_file)
    df_consoles = read_data_from_csv(consoles_file)

    #applying cleaning, casting and converting to data
    df_results = clean_blank_spaces(df_results, 'console')
    remove_data(df_results, 'userscore')
    df_results = df_results.astype(convert_dict) #casting some columns datatypes
    df_results = adding_average(df_results, 'avg_score')

    df_results.to_sql('results_', cnx, index=False)
    df_consoles.to_sql('consoles_', cnx, index=False)

    top_10_ = pd.read_sql(queries.all_top_10, cnx)
    worst_10_ = pd.read_sql(queries.all_bottom_10, cnx)
    top_10_by = pd.read_sql(queries.top_10_by_console_cmp, cnx)
    worst_10_by = pd.read_sql(queries.worst_10_by_console_cmp, cnx)

    pd.DataFrame([header_1]).to_csv(report, index=None, header=None, sep=' ', mode='a')
    top_10_.to_csv(report, sep=' ', mode='a')

    pd.DataFrame([header_2]).to_csv(report, index=None, header=None, sep=' ', mode='a')
    worst_10_.to_csv(report, sep=' ', mode='a')

    pd.DataFrame([header_3]).to_csv(report, index=None, header=None, sep=' ', mode='a')
    top_10_by.to_csv(report, sep=' ', mode='a')

    pd.DataFrame([header_4]).to_csv(report, index=None, header=None, sep=' ', mode='a')
    worst_10_by.to_csv(report, sep=' ', mode='a')

    return None

main_()
