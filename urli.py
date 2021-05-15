import requests
r = requests.get('https://ashwithv.wordpress.com/')
d = r.headers
print(r.text)
print(r.status_code)
print(r.content)
with open ('ash.txt','w') as f:
    f.write(r.text)
    f.close()

