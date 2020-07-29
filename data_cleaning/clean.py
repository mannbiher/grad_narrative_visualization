from pathlib import Path
import os

import pandas as pd

def get_output_filename(path, out_folder):
    outfile = Path(path).stem +'.csv'
    return os.path.join(out_folder, outfile)


def write_csv(df, excel_file, out_folder):
    out_csv = get_output_filename(excel_file, out_folder)
    df.to_csv(out_csv, index=False)



def clean_new_enrollment(excel_file, out_folder):
    df = pd.read_excel(excel_file)
    ## remove empty row
    df = df.drop(6)
    ## prepare headers
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
    # df.columns = df.iloc[1].values
    print(df)
    # df = df.iloc[2:38]
    # write_csv(df, excel_file, out_folder)

def clean_places_of_origin(excel_file, out_folder):
    df = pd.read_excel(excel_file)
    df.columns = df.loc[1].values
    print(df)
    


if __name__ == "__main__":
    dir_path = os.path.dirname(os.path.realpath(__file__))
    out_folder = dir_path + '/cleaned_data_files'
    # clean_new_enrollment('data_files/Census-New-Enrollment-2009-2019.xlsx', 
    #     out_folder)
    clean_academic_level('data_files/Census-Academic-Level.xlsx', out_folder)
    # clean_places_of_origin('data_files/Census-All-Places-of-Origin.xlsx',
    #     out_folder)