import requests
from bs4 import BeautifulSoup
import pandas as pd

# url of Wikipedia page that we are using: 
url = 'https://en.wikipedia.org/wiki/List_of_Formula_One_World_Drivers%27_Champions'

try:
    page = requests.get(url)
except Exception as e:
    print('Error downloading page: ',e)

soup = BeautifulSoup(page.text, 'html.parser')

tables = soup.find('table', class_=['wikitable', 'sortable', 'jquery-tablesorter'])


# Defining of the dataframe
df = pd.DataFrame(columns=['Season', 'Driver', 'Nationality', 'Age', 'Wins', 'Podiums', 'Fastest laps', 'Points', '% Points', 'Margin', '% of Margin'])

# Collecting Ddata
for row in tables.find_all('tr'): 
    cells = row.find_all('td')
    for cell in cells:
        if cell.find('a'):
            cell_text = cell.find('a').get_text(strip=True)
            print(cell_text)

