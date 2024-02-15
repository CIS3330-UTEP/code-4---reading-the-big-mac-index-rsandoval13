import csv
import pandas as pd
big_mac_file = './big-mac-full-index.csv'
df=pd.read_csv(big_mac_file)
#print(df[:2])

#print(df[['iso_a3','name']])
#print(df.iloc[[0,100]])
cnt=0
for x in df:
    #print(x)
    if x == "iso_a3":
        cnt+=1
#print(cnt)


#pinput=input('country_code all Caps: ')
country_code1='ARG'
country_query=f"iso_a3==@country_code1"
df_arg=df.query(country_query)
#print(round(df_arg['dollar_price'].mean(),2))
#print(round(df_arg['dollar_price'].min(),2))
#print(round(df_arg['dollar_price'].max(),2))

date_code = '2001-04-01'
date_query=f"date==@date_code"
df_date=df.query(date_query)
#print(df_date)

mx_query=f"iso_a3 == ‘Mex’ and (date > 2019-01-01 and date < 2019-12-31)"
df_mx=df.query(mx_query)
print(df_mx)




#def get_number_of_great():
#    gfcnt=0
#    for x in data:
#        if x.upper() == 'GREAT':
#            gfcnt+=1
#    return gfcnt
#great_count=get_number_of_great()
#print(great_count)

#idx_dollar_price = df_arg['dollar_price'].idxmax()

#print(idx_dollar_price)

def get_big_mac_price_by_year(year,country_code):
    pass # Remove this line and code your function

def get_big_mac_price_by_country(country_code):
    pass # Remove this line and code your function

def get_the_cheapest_big_mac_price_by_year(year):
    pass # Remove this line and code your function

def get_the_most_expensive_big_mac_price_by_year(year):
    pass # Remove this line and code your function

if __name__ == "__main__":
    pass # Remove this line and code your user interface