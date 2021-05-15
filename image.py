import requests
q = requests.get('https://www.thenationalnews.com/image/policy:1.906316:1567597962/sp05-Man-City-Trophy-Tour.jpg?f=16x9&w=940&$p$f$w=0ee2b1c')
print(q.content)
with open ('chelsea.jpeg','wb') as n:
    n.write(q.content)
    n.close()