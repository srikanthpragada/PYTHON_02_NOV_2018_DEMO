import requests
from bs4 import BeautifulSoup

resp = requests.get("http://www.srikanthtechnologies.com")
bs = BeautifulSoup(resp.text,'html.parser')
anchors = bs.find_all("a")

for a in anchors:
    # if href attribute is present in <a>
    if 'href' in a.attrs:
        href = a['href']
        if href.startswith('http'):
            print(href)
