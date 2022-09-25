import logging
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
logging.basicConfig(filename='app_log.txt', format='%(asctime)s %(message)s' ,encoding='utf-8') # log with timestamp and message. Do not print to console
ticker = 'TSLA' # todo: make interactive with input control
data_filename = (f"app_data/{ticker}.csv")
try: # log if exception
    df = pd.read_csv(data_filename) # input data from csc into dataframe
except Exception as Argument:
    logging.exception(f"An error occured while creating a dataframe from {data_filename} | Error: {str(Argument)}")
#df_sets = []
#first_row_index = 0
#last_row_index = 20
#increment = 20
#remain_count = len(df)
#while (remain_count >= 20):
    #df_slice = df.iloc[first_row_index:last_row_index]
    #df_sets.append(df_slice)
    #first_row_index += 20
    #last_row_index += 20
    #remain_count -= 20
    #print(df_slice)
#print(len(df_sets))
df_years = []
begin_df_row = df.head(n=1)
end_df_row = df.tail(n=1)
begin_df_date = pd.to_datetime(begin_df_row['Date'])
end_df_date = pd.to_datetime(end_df_row['Date'])
begin_year_df_date_int32 = begin_df_date.dt.year.astype(int).values[0]
begin_df_year = str(begin_year_df_date_int32) #int32 to string
end_df_date_int32 = end_df_date.dt.year.astype(int).values[0]
end_df_year = str(end_df_date_int32) #int32 to string
years_df_range = end_df_date_int32 - begin_year_df_date_int32 + 1
for i in range(years_df_range):
    if begin_df_year:
        df_year = df[(df['Date'] >= f"{begin_df_year}-01-01") & (df['Date'] <= f"{begin_df_year}-12-31")]
        begin_year_df_date_int32 += 1
        begin_df_year = str(begin_year_df_date_int32)
        df_years.append(df_year)

###print(begin_year)
#print(end_year)
#print(years_range)
#print(len(df_years))
#df_months = []
for item in df_years:
    df_item = pd.DataFrame(item) # cast as a DataFrame
    begin_year_df_row = df_item.head(n=1)
    end_year_df_row = df_item.tail(n=1)    
    begin_year_df_date = pd.to_datetime(begin_year_df_row['Date'])
    end_year_df_date = pd.to_datetime(end_year_df_row['Date'])
    begin_year_df_date_int32 = begin_year_df_date.dt.year.astype(int).values[0]
    begin_year_df_year = str(begin_year_df_date_int32) #int32 to string
    begin_month_df_date_int32 = begin_year_df_date.dt.month.astype(int).values[0]
    begin_month_df_date = str(begin_month_df_date_int32) #int32 to string
    end_month_df_date_int32 = end_year_df_date.dt.month.astype(int).values[0]
    end_month_df_date = str(end_month_df_date_int32) #int32 to string
    months_df_range = end_month_df_date_int32 - begin_month_df_date_int32 + 1
    df_months = []
    for i in range(months_df_range):
        if begin_month_df_date:
            if len(begin_month_df_date) == 1: # if month digits is less than 2
                begin_month_df_date = f"0{begin_month_df_date}"
        df_month = df_item[(df_item['Date'] >= f"{begin_year_df_year}-{begin_month_df_date}-01") & (df_item['Date'] <= f"{begin_year_df_year}-{begin_month_df_date}-31")]
        begin_month_df_date_int32 += 1
        begin_month_df_date = str(begin_month_df_date_int32)
        df_months.append(df_month)
    close_average = []
    months_xticks_labels = []
    for month_item in df_months:
        df_month_item = pd.DataFrame(month_item) # cast as a DataFrame
        month_begin_df_row = df_month_item.head(n=1)
        month_end_df_row = df_month_item.tail(n=1)
        month_begin_df_date = pd.to_datetime(month_begin_df_row['Date'])
        month_end_df_date = pd.to_datetime(month_end_df_row['Date'])
        #month_begin_df_date_str = month_begin_df_date.dt.month.astype(str).values[0]
        #month_end_df_date_str = month_end_df_date.dt.month.astype(str).values[0]
        month_begin_df_date_str = month_begin_df_date.astype(str).values[0]
        month_end_df_date_str = month_end_df_date.astype(str).values[0]
        month_xtick_label = f"{month_begin_df_date_str}\n- {month_end_df_date_str}"
        month_item_count = len(df_month_item)
        month_close_prices_sum = df_month_item['Close'].sum()
        if ((month_close_prices_sum >= 0) & (month_item_count >= 1)): # check for values            
            month_close_average = month_close_prices_sum / month_item_count
            close_average.append(month_close_average)
            months_xticks_labels.append(month_xtick_label)# provide label conditionally            
    close_average_df = pd.DataFrame(close_average)
    chart_id = f"{ticker} - {begin_year_df_year}"
    plt.figure()
    plt.plot(close_average_df)
    plt.ylabel('Moving Average')
    plt.title(chart_id)
    plt.xticks(np.arange(len(close_average)), months_xticks_labels, rotation = 70)
    plt.tight_layout()
    plt.savefig(f"charts/{chart_id}.png", facecolor = "#cfd9e4") # todo: wrap in try except, log except
    plt.show()
    #print(close_average_df)
        



    
    
    #print(months_df_range)
    #print(len(df_month))
    #print(len(df_months))
    #print(len(item))
    
    #print(item)
    #print(df_year)
jj = 66



    
    