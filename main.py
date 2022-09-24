import logging
import pandas as pd
import dateparser as dp
logging.basicConfig(filename='app_log.txt', format='%(asctime)s %(message)s' ,encoding='utf-8') # log with timestamp and message. Do not print to console
data_filename = ('app_data/TSLA.csv')
try: # log if exception
    df = pd.read_csv(data_filename) # input data from csc into dataframe
except Exception as Argument:
    logging.exception(f"An error occured while creating a dataframe from {data_filename} | Error: {str(Argument)}")
df_sets = []
first_row_index = 0
last_row_index = 20
increment = 20
remain_count = len(df)
while (remain_count >= 20):
    df_slice = df.iloc[first_row_index:last_row_index]
    df_sets.append(df_slice)
    first_row_index += 20
    last_row_index += 20
    remain_count -= 20
    print(df_slice)
print(len(df_sets))
df_years = []
begin_row = df.head(n=1)
end_row = df.tail(n=1)
begin_date = pd.to_datetime(begin_row['Date'])
end_date = pd.to_datetime(end_row['Date'])
begin_date_int32 = begin_date.dt.year.astype(int).values[0]
begin_year = str(begin_date_int32) #int64 to string
end_date_int32 = end_date.dt.year.astype(int).values[0]
end_year = str(end_date_int32) #int64 to string
years_range = end_date_int32 - begin_date_int32 + 1
for i in range(years_range):
    if begin_year:
        df_year = df[(df['Date'] > f"{begin_year}-01-01") & (df['Date'] < f"{begin_year}-12-31")]
        begin_date_int32 += 1
        begin_year = str(begin_date_int32)
        df_years.append(df_year)

print(begin_year)
print(end_year)
print(years_range)
print(len(df_years))

for year in df_years:
    print(year)
#print(df_year)
jj = 66



    
    