from pathlib import Path
import os

import pandas as pd
import numpy as np


def get_country_isocode_mapping():
    dir_path = os.path.dirname(os.path.realpath(__file__))
    country_mapping = pd.read_csv(
        dir_path + '/data_files/country-codes_csv.csv', dtype=str)
    country_mapping = country_mapping.iloc[1:, [2, 8]]
    mapping = {row['official_name_en']: row['ISO3166-1-numeric']
               for _, row in country_mapping.iterrows()}
    # add missing countries > 1000 students
    mapping['Taiwan']='158'
    mapping['Hong Kong']='364'
    mapping['Iran']='364'
    mapping['North Korea'] = '408'
    mapping['South Korea'] = '410'
    mapping['Vietnam'] = '704'
    mapping['United Kingdom'] = '826'
    mapping['Venezuela'] = '862'
    mapping['Russia'] = '643'
    mapping['Bolivia'] = '068'
    mapping['Côte d’Ivoire/Ivory Coast'] ='384'
    return mapping

def get_output_filename(path, out_folder):
    outfile = Path(path).stem + '.csv'
    return os.path.join(out_folder, outfile)


def write_csv(df, excel_file, out_folder, index=False):
    out_csv = get_output_filename(excel_file, out_folder)
    df.to_csv(out_csv, index=index)


def clean_new_enrollment(excel_file, out_folder):
    df = pd.read_excel(excel_file)
    # remove empty row
    df = df.drop(6)
    # prepare headers
    headers = []
    for i, column in enumerate(df.columns):
        first_header = df[column].iloc[1]
        if i == 0:
            headers.append('Academic Level')
            continue
        if pd.isna(first_header):
            headers.append(df[column].iloc[2])
        else:
            headers.append(f'{first_header} {df[column].iloc[2]}')

    df.columns = headers
    # chose data rows
    df = df.iloc[3:8]
    write_csv(df, excel_file, out_folder)


def clean_academic_level(excel_file, out_folder):
    # TODO change hyphen to null
    df = pd.read_excel(excel_file)
    df = df.drop([2,
                  4, 5, 6, 7, 8, 9, 10, 11, 12,
                  14, 15, 16, 17, 18,
                  20, 21, 22,
                  24, 26,
                  28, 29, 30, 31, 32, 33, 34])

    # drop upto column 34 pre 2009/10
    columns_to_drop = [i for i in range(33) if i != 1]

    # drop empty columns, every third column is empty
    empty_columns = [i for i in range(33, 62) if not (i+1) % 3]

    columns_to_drop = list(set(columns_to_drop) | set(empty_columns))
    df = df.drop(df.columns[columns_to_drop], axis=1)

    df = df.reset_index(drop=True)

    headers = []
    for i, column in enumerate(df.columns):
        if i == 0:
            # print(column)
            # academic level column
            headers.append(df[column].iloc[1])
            continue

        first_header = df[column].iloc[0]
        if i % 2 != 0:
            year = first_header
        if pd.isna(first_header):

            headers.append(f'{year} {df[column].iloc[1]}')
        else:
            headers.append(f'{first_header} {df[column].iloc[1]}')

    df.columns = headers
    df = df.iloc[2:]
    df = df.set_index('Academic Level').transpose()
    df = df.reset_index(level=0)
    df = df.rename(columns={'index': 'Year'})
    # df.index.name = None

    # df.columns = df.iloc[1].values
    print(df)
    # df = df.iloc[2:38]
    write_csv(df, excel_file, out_folder)


def clean_places_of_origin(excel_file, out_folder):
    df = pd.read_excel(excel_file)
    df.columns = df.loc[1].values
    print(df)


def clean_top25_institution(excel_file, out_folder):
    df = pd.read_excel(excel_file)
    columns_to_drop = [i for i in range(55)]
    df = df.drop(df.columns[columns_to_drop], axis=1)

    print(df)


def clean_top25_institution_csv():
    dir_path = os.path.dirname(os.path.realpath(__file__))
    out_folder = dir_path + '/cleaned_data_files'
    csv_file = out_folder + '/Census-Top-25-Institutions.csv'
    df = pd.read_csv(csv_file)
    df = df.iloc[:, :6]
    write_csv(df, csv_file, out_folder)


def clean_all_places_of_origin_csv():
    dir_path = os.path.dirname(os.path.realpath(__file__))
    out_folder = dir_path + '/cleaned_data_files'
    csv_file = out_folder + '/Census-All-Places-of-Origin.csv'
    df = pd.read_csv(csv_file)
    # df = df.iloc[:264, 1:12]
    mapping = get_country_isocode_mapping()
    df = df.assign(country_code=df['Place of Origin'].map(mapping))
    df = df.replace('-', np.nan)
    print(df)
    # print(country_mapping)
    write_csv(df, csv_file, out_folder)


if __name__ == "__main__":
    dir_path = os.path.dirname(os.path.realpath(__file__))
    out_folder = dir_path + '/cleaned_data_files'
    # clean_new_enrollment('data_files/Census-New-Enrollment-2009-2019.xlsx',
    #     out_folder)
    # clean_academic_level('data_files/Census-Academic-Level.xlsx', out_folder)
    # clean_places_of_origin('data_files/Census-All-Places-of-Origin.xlsx',
    #     out_folder)
    # clean_top25_institution('data_files/Census-Top-25-Institutions.xlsx',out_folder)
    # clean_top25_institution_csv()
    clean_all_places_of_origin_csv()
