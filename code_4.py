import pandas as pd
big_mac_file = './big-mac-full-index.csv'
df = pd.read_csv(big_mac_file)

def get_big_mac_price_by_year(year,country_code):
    country_code= country_code.upper()
    df_by_date=df[df['date'].str.startswith(str(year))&(df['iso_a3']==country_code)]
    return round(df_by_date['dollar_price'].mean(),2)    

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
    pass # Remove this line and code your user interface