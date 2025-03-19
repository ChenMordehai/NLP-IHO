# coding: utf8

import re
import pandas as pd
import json

INPUT_PATH = ""
OUTPUT_PATH = ""  # .json


def write_to_json(my_df, json_path):
    with open(json_path, 'w', encoding='utf-8') as file:
        for indx, row in my_df.iterrows():
            if row['Result'] is not None:
                record = {
                    'row_index': indx,
                    'text': str(row['Text']),
                    'label': []
                }
                file.write(json.dumps(record, ensure_ascii=False) + '\n')


if __name__ == '__main__':
    df = pd.read_excel(INPUT_PATH)
    write_to_json(df, OUTPUT_PATH)
