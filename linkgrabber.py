import os
from bs4 import BeautifulSoup
import requests


def grab_url(base_url):


    link_list = []

    os.listdir()
    page = 0
    while True:
        page += 1
        url = base_url + '/trefferliste?ep='
        print(f'{page},', end=" ")
        response = requests.get(url)
        soup = BeautifulSoup(response.text, "html.parser")
        listingsGroup = BeautifulSoup(str(soup.find("div", {"data-test": "result-list"})), "html.parser")
        listingsList = listingsGroup.find_all("a", {"data-test": "result-list-item"})

        for listing in listingsList:
            #print(f'page :{page} grab Advertisement {listing["href"]} ')
            link_list.append("https://www.homegate.ch" + listing["href"])
        if len(listingsList) < 5:
            print(f'\nthis zip has {page} page and {len(link_list)} inserat')
            break
    return link_list
