import requests, webbrowser
from bs4 import BeautifulSoup

searchinput = input('Please enter ')
print('Searching...')


google_search = requests.get('https://www.google.com/search?q='+searchinput)
soup = BeautifulSoup(google_search.text , 'html.parser')

search_results = soup.select('.r a')

for links in search_results[:5]:
    actual_link = links.get('href')
    webbrowser.open(f'https://www.google.com{actual_link}')

