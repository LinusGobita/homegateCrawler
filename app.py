from urllib.request import Request, urlopen

import requests
from tqdm import tqdm

base_url = 'https://www.homegate.ch/kaufen/'
id = 3001609001
url = base_url + str(id)




response = urlopen(url)
print(response)
#    soup = BeautifulSoup(response.content, "html.parser")
#    print(soup.prettify())
print(url)

req = Request('http://www.cmegroup.com/trading/products/#sortField=oi&sortAsc=false&venues=3&page=1&cleared=1&group=1', headers={'User-Agent': 'Mozilla/5.0'})
webpage = urlopen(req).read()
print(webpage)

with open(str(id), "wd") as handle:
    for data in tqdm(response.iter_content()):
        handle.write(data)
