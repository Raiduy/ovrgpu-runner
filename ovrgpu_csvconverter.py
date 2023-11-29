import pandas as pd
import numpy as np
import os

RAW_FILE = 'sup.txt'

# 11/29/2023 12:01:44 AM - GPU Frequency                              :   525000000.000
def process_line(line):
    timestamp = line.split(' - ')[0]
    content = line.split(' - ')[1]
    key = str(content.split(':')[0].strip())
    value = float(content.split(':')[1].strip())
    return timestamp, key, value

def add_to_dataframe(df, timestamp, key, value):
    if key not in df.columns:
        df[key] = np.nan
    df.loc[timestamp, key] = value
    return df

def was_processed(file_name):
    return file_name.strip('.txt') + '.csv' in os.listdir('./data')

def create_dataframe(file_path, file_name):
    df = pd.DataFrame()
    for line in open(file_path, 'r', encoding='utf-16'):
        if len(line) < 27:
            continue
        timestamp, key, value = process_line(line)
        df = add_to_dataframe(df, timestamp, key, value)

    # df = df.rename({"" : "timestamp"}, axis='columns')
    df.index.name = 'timestamp'
    df = df.reset_index()
    print(df)
    df.to_csv(f'./data/{file_name.strip('.txt')}.csv', index=False)
    

def main():
    for file_name in os.listdir('./raw_data'):
        if was_processed(file_name):
            continue
        file_path = os.path.join('./raw_data', file_name)
        create_dataframe(file_path, file_name)

if __name__ == '__main__':
    main()
   