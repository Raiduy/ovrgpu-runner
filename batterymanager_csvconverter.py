import pandas as pd
import numpy as np
import os

RAW_DATA = './raw_data/batterymanager/batterymanager-companion.log'



def main():
    for line in open(RAW_DATA):
        if 'rawFields => ' in line:
            cols = line.split('rawFields => ')[1].split(',')
            cols = [col.strip() for col in cols]
            
            print(cols)




if __name__ == '__main__':
    main()