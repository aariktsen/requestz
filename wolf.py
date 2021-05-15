from bs4 import BeautifulSoup
import requests
import csv
req = requests.get("https://www.sportskeeda.com/go/epl/standings").text
soup = BeautifulSoup(req,'lxml')
art = soup.find('table',class_ = "keeda_points_table")
with open('pl_table.csv','w') as cr:
    csv_writer = csv.writer(cr)
    csv_writer.writerows('pos','club','P','W','D','L','G','Pt')
    for yenne in art.find_all('tr'):
        pos = art.find_all('td' class_="keeda_points_table_position green">
                           <span class="value">1</span><span class="same"></span></td>')
