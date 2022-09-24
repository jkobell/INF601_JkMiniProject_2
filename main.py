import logging
import pandas as pd
logging.basicConfig(filename='app_log.txt', format='%(asctime)s %(message)s' ,encoding='utf-8') # log with timestamp and message. Do not print to console
data_filename = ('app_data/TSLA.csv')
try: # log if exception
    df = pd.read_csv(data_filename) # input data from csc into dataframe
except Exception as Argument:
    logging.exception(f"An error occured while creating a dataframe from {data_filename} | Error: {str(Argument)}")
    
    