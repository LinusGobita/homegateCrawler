import requests
from tqdm import tqdm

base_url = 'https://www.homegate.ch/kaufen/'
id = 3001609001
url = base_url + str(id)

response = requests.get(url)
print(response)
#    soup = BeautifulSoup(response.content, "html.parser")
#    print(soup.prettify())
print(url)
with open(str(id), "wd") as handle:
    for data in tqdm(response.iter_content()):
        handle.write(data)
