import re
import pandas as pd
from datetime import datetime
from bs4 import BeautifulSoup
import requests



#Finding out basic information regarding Canoo
url = 'https://en.wikipedia.org/wiki/Canoo'
page = requests.get(url)
soup = BeautifulSoup(page.text,'html')

table = soup.find_all('table')
title = soup.find_all('th')
tabel_titles = [title.text for title in title]
tabel_titles

for row in tabel_titles:
  row_data = soup.find_all('td')[1:12]
  row_data = [data.text.strip() for data in row_data]
  print(row_data)
  break

data = {'Column Heading': tabel_titles, 'Row Heading': row_data}
Basic_info = pd.DataFrame(data)
Basic_info = Basic_info.reset_index(drop=True)
Basic_info

Basic_info.to_excel('basic_info.xlsx', sheet_name='Sheet1')


#finding out competitors to Canoo
url_alt = 'https://growjo.com/company/Canoo'
page = requests.get(url_alt)
soup_alt = BeautifulSoup(page.text,'html')

table_alt = soup_alt.find_all('table')
title_alt = soup_alt.find_all('th')
alt_tabel_titles = [title_alt.text for title_alt in title_alt]
alt_tabel_titles

Canoo_competitors = pd.DataFrame(columns = alt_tabel_titles)
Canoo_competitors

column_data = soup_alt.find_all('tr')
column_data

for row in column_data[1:]:
  row_data = row.find_all('td')
  individual_row_data = [data.text.strip() for data in row_data]

  length = len(Canoo_competitors)
  Canoo_competitors.loc[length] = individual_row_data

# Droping columns because of NA values
Canoo_competitors.drop(['Total Funding', 'Valuation'], axis=1, inplace=True)

# Cleaning in column Competitor Name
Canoo_competitors['Competitor Name'] = Canoo_competitors['Competitor Name'].apply(lambda x: x[2:])
Canoo_competitors.iloc[4, 0] = 'Dependable Dodge'
Canoo_competitors.iloc[9, 0] = 'Extreme Dimensions'

Canoo_competitors.to_excel('Canoo_competitors.xlsx', sheet_name='Sheet1')


# Script to Seach Internet on Google custom search API
def clean_Filename(filename):
 filename = re.sub(r'[\\/*?:"<>|]',"",filename)
 return filename


def build_payload(query, start=1, num=10,date_restrict='m1', **params):
 payload ={
  'key':API_KEY,
  'q':query,
  'cx': SEARCH_ENGINE_ID,
  'start': start,
  'num':num,
  'DateRestrict': date_restrict
 }

 payload.update(params)
 return payload


def make_request(payload):
 response = requests.get("https://customsearch.googleapis.com/customsearch/v1", params = payload)
 if response.status_code != 200:
  raise Exception('Request failed')
 return response.json()


def main(query, result_total=10):
    items = []
    remainder = result_total % 10
    if remainder > 0:
        pages = (result_total // 10) + 1
    else:
        pages = result_total // 10

    for i in range(pages):
        if pages == i + 1 and remainder > 0:
            payload = build_payload(query, start=(i + 1) * 10, num=remainder)
        else:
            payload = build_payload(query, start=(i + 1) * 10)
        response = make_request(payload)
        items.extend(response['items'])

    query_string_clean = clean_Filename(query)
    df = pd.json_normalize(items)
    df.to_excel(f'{query_string_clean}.xlsx', format(query_string_clean), index=False)

if __name__ == '__main__':
 API_KEY = 'Your API_KEY'
 SEARCH_ENGINE_ID = 'Your SEARCH_ENGINE_ID'
 search_query = 'Query'  # 'query'is volatile and can be changed to any thing that reaquire a search
 total_results = 30
 main(search_query,total_results)
