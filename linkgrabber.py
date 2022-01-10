import os
import random
import downloader
from time import sleep

from bs4 import BeautifulSoup
import requests

if __name__ == "__main__":
    base_urls = ["https://www.homegate.ch/mieten/immobilien/land-schweiz/trefferliste?ep=",
                 "https://www.homegate.ch/kaufen/immobilien/land-schweiz/trefferliste?ep="]
    download_counter = 0
    sleep_min = 2
    sleep_max = 5
    sleeptimes = list(range(sleep_min, sleep_max, 1))
    os.listdir()
    for base_url in base_urls:
        page = 0
        while True:
            page += 1
            url = base_url + str(page)
            response = requests.get(url)
            soup = BeautifulSoup(response.text, "html.parser")
            listingsGroup = BeautifulSoup(str(soup.find("div", {"data-test": "result-list"})), "html.parser")
            listingsList = listingsGroup.find_all("a", {"data-test": "result-list-item"})

            for listing in listingsList:
                downloader.get_listing("https://www.homegate.ch"+listing["href"])
                sleepTime = random.choice(sleeptimes)
                download_counter += 1
                print(f'Download  {download_counter} | Sleeping: {sleepTime} ')
                sleep(sleepTime)
            if len(listingsList) < 10:
                break
