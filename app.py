from time import sleep
import random
import pandas as pd

import downloader
import linkgrabber


if __name__ == "__main__":

    read_file = pd.read_csv('Postleitzahlen-Schweiz.csv', header=None)
    read_file.head()
    #read_file.colums = ['zip', 'location', 'kanton', 'canton', 'shortcut', 'land', 'pays', 'paese', 'somthing' ]
    zip_in_ch = read_file[0]
    base_urls = [f'https://www.homegate.ch/mieten/immobilien/plz-',
                 f'https://www.homegate.ch/kaufen/immobilien/plz-']

    sleep_min = 3
    sleep_max = 9
    sleeptimes = list(range(sleep_min, sleep_max, 1))
    download_counter_total = 1


    #Grab all URL from Advertisement
    for base_url in base_urls:

        for zip in zip_in_ch:
            #grab the urls
            print(f'Scanning zip {zip} on Page: ', end=" ")
            listing_list = linkgrabber.grab_url(base_url + str(zip))
            download_counter_zip = 1

            for link in listing_list:
                #take a Break
                sleepTime = random.choice(sleeptimes)
                sleep(sleepTime)
                print(f'Zip : {zip} download {download_counter_zip} from {len(listing_list)}   |  Download Total Nr:  {download_counter_total}    | Sleeping: {sleepTime} '
                      f'| URL : {link}', end=" ")
                download_counter_total += 1
                download_counter_zip += 1
                #Download the Advertisement
                downloader.get_listing(link)
