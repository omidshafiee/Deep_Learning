df['TICKER'].value_counts()

df.drop(['TICKER'], axis=1, inplace=True)

# Intentionally separate from ticker, since data cleansing will do on time column
# Right now just drop it, to concentrate on RNN
df.drop(['TIME'], axis=1, inplace=True)


def convert_to_timestamp(in_date, in_time):
    date_time_str = str(in_date) + ' ' + str(in_time)
    # print(type(date_time_str))
    s_datetime = datetime.strptime(date_time_str, '%Y%m%d %H%M%S')
    # date = datetime(year=int(s[0:4]), month=int(s[4:6]), day=int(s[6:8]))
    # print(s_datetime)
    # print(type(s_datetime))
    return s_datetime
    
    
print(df['DATE'][0], df['TIME'][0])
convert_to_timestamp(df['DATE'][0], df['TIME'][0])    

df['TIME_STAMP'] = df.apply(lambda x: convert_to_timestamp(x['DATE'], x['TIME']), axis=1)