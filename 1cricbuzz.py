import time

import requests
from bs4 import BeautifulSoup

url = "https://www.cricbuzz.com/"
r = requests.get(url)
# print(r.text)
# print(r.content)
time.sleep(10)
soup = BeautifulSoup(r.text, 'html.parser')
links = soup.find_all(attrs={'class':"cb-col"})
print(links)
for i in links:
    print(i.text)
    print()
print("\n")
