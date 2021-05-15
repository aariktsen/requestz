from bs4 import BeautifulSoup
import requests
req = requests.get('https://www.cricbuzz.com/cricket-series/2676/indian-premier-league-2018/points-table').text
soup = BeautifulSoup(req,'lxml')
def team_name():
    jio = soup.find('th',class_ ='cb-srs-pnts-th text-left').text
    print(jio,end=",")
def matches():
    lio = soup.find('td',class_ ='cb-srs-pnts-th').text
    print(lio)
def win():
    for art in soup.find_all('td'):
        pio =art.
        print(pio)
def lost():
    jio = soup.find('th',class_ ='cb-srs-pnts-th text-left').text
def tied():
    jio = soup.find('th',class_ ='cb-srs-pnts-th text-left').text
def nr():
    jio = soup.find('th',class_ ='cb-srs-pnts-th text-left').text
def pts():
    jio = soup.find('th',class_ ='cb-srs-pnts-th text-left').text
def nrr():
    jio = soup.find('th',class_ ='cb-srs-pnts-th text-left').text
team_name()
matches()
win()
