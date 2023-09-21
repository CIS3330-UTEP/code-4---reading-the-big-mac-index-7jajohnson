import csv
import pandas as pd
big_mac_file = './big-mac-full-index.csv'

def get_big_mac_price_by_year(year,country_code):
    df = pd.DataFrame(pd.read_csv(big_mac_file))
    # locate the country_code
    # print(country_code)
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
    print("Testing Most Expensive")
    year = [2003, 2014, 2016, 2014, 2013, 2005, 2006, 2010, 2011, 2009]
    value = ['Switzerland(CHE): $4.6', 'Norway(NOR): $7.8', 'Switzerland(CHE): $6.59', 'Norway(NOR): $7.8',
             'Venezuela(VEN): $9.08', 'Norway(NOR): $6.06', 'Norway(NOR): $7.05', 'Norway(NOR): $7.2',
             'Norway(NOR): $8.31', 'Norway(NOR): $6.15']

    x = 0
    for item in year:
        print(get_the_most_expensive_big_mac_price_by_year(str(item))==value[x])
        x += 1



    x = 0
    print("Testing Cheapest")
    year = [2008,2012,2019,2016,2011,2000,2004,2007,2015,2005]
    value = ['Malaysia(MYS): $1.7', 'India(IND): $1.58', 'Russia(RUS): $1.65', 'Venezuela(VEN): $0.66',
             'India(IND): $1.89', 'Malaysia(MYS): $1.19', 'Saudi Arabia(SAU): $0.64', 'China(CHN): $1.41',
             'Venezuela(VEN): $0.67', 'China(CHN): $1.27']
    for item in year:
        print(get_the_cheapest_big_mac_price_by_year(str(item))==value[x])
        x +=1
    country_code = ['arg', 'rus', 'mex', 'twn', 'kor', 'jpn', 'gbr', 'zaf', 'chn', 'hun']

    value = [3.04, 1.98, 2.68, 2.37, 3.35, 3.14, 3.98, 2.13, 2.37, 3.06]
    x = 0
    print("price by country")
    for item in country_code:
        print(get_big_mac_price_by_country(item) == value[x])
        x+=1

    country_code = ['arg', 'usa', 'mex', 'arg', 'kor', 'jpn', 'gbr', 'bra', 'chn', 'can']
    year = [2012, 2018, 2009, 2017, 2019, 2012, 2014, 2008, 2016, 2006]
    value = [4.4, 4.62, 2.39, 3.8, 3.92, 4.13, 4.78, 4.73, 2.73, 3.07]
    x = 0
    print("price by year and country code")
    for num in range(10):
        print(get_big_mac_price_by_year(str(year[num]),country_code[num]) == value[x])
        x+=1