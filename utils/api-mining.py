import time
import requests
import pandas as pd
from lxml import etree

def set_currency_rate(xml, date):
    row = [date[1] + '-' + date[0]]
    for currency in currencies:
        valute = xml.xpath(f"//Valute[CharCode='{currency}']")
        value = float(valute[0].find('VunitRate').text.replace(',', '.')) if valute else None
        row.append(value)
    data.append(row)

BASE_URL = 'https://www.cbr.ru/scripts/XML_daily.asp'
currencies = ['BYR','USD','EUR','KZT','UAH','AZN','KGS','UZS','GEL']
MIN_DATE = f'2002-12-31'
MAX_DATE = f'2024-11-01'

months = pd.date_range(MIN_DATE,MAX_DATE,
              freq='MS').strftime("%d/%m/%Y").tolist()

data = []
for month in months:
    response = requests.get(f"{BASE_URL}?date_req={month}")
    xml = etree.fromstring(response.content)
    set_currency_rate(xml, month.split('/')[1:])
    print(f"LOG: {month}")
    time.sleep(0.2)

df = pd.DataFrame(data, columns=['date'] + currencies)
df.to_csv("currency.csv", index=False) # "currency.csv"