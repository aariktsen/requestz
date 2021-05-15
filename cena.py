import requests
from bs4 import BeautifulSoup
req = requests.get('https://www.cricbuzz.com/cricket-series/2676/indian-premier-league-2018/points-table').content
soup = BeautifulSoup(req,'lxml')
soup.prettify()
with open('ipl.html','w') as f:
     f.write(str(req))