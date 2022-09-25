# INF601 - Advanced Programming in Python
# James Kobell
# Mini Project 2
import logging
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
logging.basicConfig(filename='app_log.txt', format='%(asctime)s %(message)s' ,encoding='utf-8') # log with timestamp and message.
ticker = 'TSLA' # todo: make interactive with input control
data_filename = (f"app_data/{ticker}.csv")
try: # log if exception
    df = pd.read_csv(data_filename) # input data from csv into dataframe | todo: make interactive with input control
except Exception as Argument:
    logging.exception(f"An error occured while creating a dataframe from {data_filename} | Error: {str(Argument)}")
df_years = [] # declare years list
begin_df_row = df.head(n=1) # parent df head
end_df_row = df.tail(n=1) # parent df tail
begin_df_date = pd.to_datetime(begin_df_row['Date']) # date from head
end_df_date = pd.to_datetime(end_df_row['Date']) # date from tail
begin_year_df_date_int32 = begin_df_date.dt.year.astype(int).values[0] # date to int - used for incrementing 
begin_df_year = str(begin_year_df_date_int32) #int32 to string - used for f" interpolation
end_df_date_int32 = end_df_date.dt.year.astype(int).values[0] # date to int - used for incrementing
end_df_year = str(end_df_date_int32) #int32 to string - used for f" interpolation
years_df_range = end_df_date_int32 - begin_year_df_date_int32 + 1 # parent df year range
for i in range(years_df_range): #iterate parent df. append each child/year df to years list
    if begin_df_year:
        df_year = df[(df['Date'] >= f"{begin_df_year}-01-01") & (df['Date'] <= f"{begin_df_year}-12-31")]
        begin_year_df_date_int32 += 1
        begin_df_year = str(begin_year_df_date_int32)
        df_years.append(df_year)
for item in df_years: # iterate each year df. query year and month for each
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
    df_months = [] # declare months df list
    for i in range(months_df_range): # iterate available months in year. append each month df to df_months list
        if begin_month_df_date:
            if len(begin_month_df_date) == 1: # if month digits is less than 2 prepend a 0
                begin_month_df_date = f"0{begin_month_df_date}"
        df_month = df_item[(df_item['Date'] >= f"{begin_year_df_year}-{begin_month_df_date}-01") & (df_item['Date'] <= f"{begin_year_df_year}-{begin_month_df_date}-31")]
        begin_month_df_date_int32 += 1
        begin_month_df_date = str(begin_month_df_date_int32)
        df_months.append(df_month)
    close_average = []
    months_xticks_labels = []
    for month_item in df_months: # iterate df_months list 
        df_month_item = pd.DataFrame(month_item) # cast as a DataFrame
        month_begin_df_row = df_month_item.head(n=1)
        month_end_df_row = df_month_item.tail(n=1)
        month_begin_df_date = pd.to_datetime(month_begin_df_row['Date'])
        month_end_df_date = pd.to_datetime(month_end_df_row['Date'])
        month_begin_df_date_str = month_begin_df_date.astype(str).values[0]
        month_end_df_date_str = month_end_df_date.astype(str).values[0]
        month_xtick_label = f"{month_begin_df_date_str}\n- {month_end_df_date_str}" # build xticks label
        month_item_count = len(df_month_item) # for x-axis datapoints formatting
        month_close_prices_sum = df_month_item['Close'].sum()
        if ((month_close_prices_sum >= 0) & (month_item_count >= 1)): # check for values            
            month_close_average = month_close_prices_sum / month_item_count
            close_average.append(month_close_average)
            months_xticks_labels.append(month_xtick_label)# provide label conditionally. only if moving average            
    close_average_df = pd.DataFrame(close_average) # new df for plotting
    chart_id = f"{ticker} - {begin_year_df_year}" # value str built for chart title AND for png filename
    plt.figure() #new instance for each chart 
    plt.plot(close_average_df)
    plt.ylabel('Moving Average')
    plt.title(chart_id)
    plt.xticks(np.arange(len(close_average)), months_xticks_labels, rotation = 70)
    plt.tight_layout() # provides padding at xticks and labels
    try: # log if exception
        plt.savefig(f"charts/{chart_id}.png", facecolor = "#cfd9e4") # create charts as png files
    except Exception as Argument: # throw if exception during savefig
        logging.exception(f"An error occured while saving chart: {chart_id} | Error: {str(Argument)}")    
    #plt.show() # uncomment for degugging



    
    