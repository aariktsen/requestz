from bs4 import BeautifulSoup
import requests
req = requests.get("https://www.sportskeeda.com/go/epl/standings").text
soup = BeautifulSoup(req,'lxml')
art = soup.find('table',class_ = "keeda_points_table")
#for a in art.find_all('tr'):
for b in art.find_all('td'):
    print(b.text)
#print(art)
#art=soup.find_all('tr')
#for allie in art.find_all('a',class_ = "keeda_football_table_team_name"):
 #   print(allie.text)
#for yenne in art.find_all('tr'):
 #   print(yenne.text)
#with open('pl_table.txt','w') as f:
 #   for yenne in art.find_all('tr'):
  #      f.write(str(yenne.contents))
