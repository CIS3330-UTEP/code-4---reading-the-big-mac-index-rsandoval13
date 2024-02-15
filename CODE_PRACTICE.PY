import pandas as pd
import csv

big_mac_file = './big-mac-full-index.csv'
df = pd.read_csv(big_mac_file)

def get_big_mac_price_by_year(year,country_code):
    country_code= country_code.upper()
    df_by_date=df[df['date'].str.startswith(str(year))&(df['iso_a3']==country_code)]
    mean_dollar_price = round(df_by_date['dollar_price'].mean(),2)
    return mean_dollar_price


def get_big_mac_price_by_country(country_code):
    country_code=country_code.upper()
    df_by_country=df[df['iso_a3']==country_code]
    return round(df_by_country['dollar_price'].mean(),2)
    

def get_the_cheapest_big_mac_price_by_year(year):
    min_price_row = df[df['date'].str.startswith(str(year))].nsmallest(1, 'dollar_price').iloc[0]
    return f"{min_price_row['name']}({min_price_row['iso_a3']}): ${round(min_price_row['dollar_price'], 2)}"

def get_the_most_expensive_big_mac_price_by_year(year):
    max_price_row = df[df['date'].str.startswith(str(year))].nlargest(1, 'dollar_price').iloc[0]
    return f"{max_price_row['name']}({max_price_row['iso_a3']}): ${round(max_price_row['dollar_price'], 2)}"

if __name__ == "__main__":
    

    year = '2012'
    country_code='arg'
    # Example usage:
    #print("Average Big Mac price by year and country:", get_big_mac_price_by_year(year, country_code))
    #print(get_big_mac_price_by_year(2000, 'usa'))
    #print(get_big_mac_price_by_country('usa'))
    


    print("Average Big Mac price by year and country:", get_big_mac_price_by_year(year,country_code))
    print("Average Big Mac price by country:", get_big_mac_price_by_country(country_code))    
    print("Cheapest Big Mac price by year:", get_the_cheapest_big_mac_price_by_year(2008))
    print("Most Expensive Big Mac price by year:", get_the_most_expensive_big_mac_price_by_year(2003))
    #print(get_the_cheapest_big_mac_price_by_year(2008))
    #print(get_the_most_expensive_big_mac_price_by_year(2003))
