from bs4 import BeautifulSoup
import requests
req = requests.get('https://www.cricbuzz.com/cricket-series/2676/indian-premier-league-2018/points-table').text
soup=BeautifulSoup(req,'lxml')
#for at in soup.find
'''for eve in soup.find_all('td',class_ = 'cb-srs-pnts-name'):
    prin =eve.a.text
    print(prin)'''
for cein in soup.find_all('td'):
     o=cein.text
     print(o,delimiter=',',newline='')
print()
'''for shaun in soup.find('tbody'):
    for kio in soup.find_all('td',class_ = 'cb-srs-pnts-name'):
        print(kio.text,end=",")
        for bliz in shaun.find_all('td',class_='cb-srs-pnts-td'):
            l=bliz.text
            print(l,end=",")
    print()'''
