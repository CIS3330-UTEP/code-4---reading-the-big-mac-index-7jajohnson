import csv
import pandas as pd
big_mac_file = './big-mac-full-index.csv'

def get_big_mac_price_by_year(year,country_code):
    df = pd.DataFrame(pd.read_csv(big_mac_file))
    # locate the country_code
    print(country_code)
    df = df.loc[df['iso_a3'].str.lower()== country_code.lower()]
    df = df.loc[df['date'].str[0:4] == year]
    mean_price = df['dollar_price'].mean()
    return(float(round(mean_price,2)))




def get_big_mac_price_by_country(country_code):
    df = pd.DataFrame(pd.read_csv(big_mac_file))
    # locate the country_code
    df = df.loc[df['iso_a3'].str.lower() == country_code.lower()]
    mean_price = df['dollar_price'].mean()
    return (float(round(mean_price, 2)))

def get_the_cheapest_big_mac_price_by_year(year):
    df = pd.DataFrame(pd.read_csv(big_mac_file))
    df = df.loc[df['date'].str[0:4] == year]
    df = df.loc[df['dollar_price']==df['dollar_price'].min()]
    # print(f"{df['name'].values[0]}({df['iso_a3'].values[0]}): ${round(float(df['dollar_price'].values[0]),2)}")
    return(f"{df['name'].values[0]}({df['iso_a3'].values[0]}): ${round(float(df['dollar_price'].values[0]),2)}")


    # "country_name(country_code): $dollar_price"
def get_the_most_expensive_big_mac_price_by_year(year):
    df = pd.DataFrame(pd.read_csv(big_mac_file))
    df = df.loc[df['date'].str[0:4] == year]
    df = df.loc[df['dollar_price']==df['dollar_price'].max()]
    # print(f"{df['name'].values[0]}({df['iso_a3'].values[0]}): ${round(float(df['dollar_price'].values[0]),2)}")
    return(f"{df['name'].values[0]}({df['iso_a3'].values[0]}): ${round(float(df['dollar_price'].values[0]),2)}")


if __name__ == "__main__":
    pass