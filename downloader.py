import time, random, os, logging
from datetime import datetime
import requests
import app


def get_listing(listingURL):
    sub_dir = 'HomegateCrawlerDB'
    sub_dir_logs = 'logs'
    sub_dir_data = 'data'
    log_file_name = 'homegate'
    timeout_duration = 5
    abs_path = os.path.join(os.getcwd(), sub_dir)
    abs_path_logs = os.path.join(abs_path, sub_dir_logs)
    abs_path_data = os.path.join(abs_path, sub_dir_data)
    if not os.path.exists(abs_path_logs):
        os.makedirs(abs_path_logs)
    if not os.path.exists(abs_path_data):
        os.makedirs(abs_path_data)

    log_file_name = 'homegate'
    listing_ID = str.split(listingURL, "/")[-1]
    data_file_name = 'homegate-' + str(id)
    date_str = datetime.now().strftime("%Y%m%d")

    log_file = os.path.join(abs_path_logs, f'{log_file_name}_{date_str}.log')
    logging.basicConfig(
        level=logging.DEBUG,
        filename=log_file,
        filemode="a+",
        format="%(asctime)-15s %(message)s"
    )

    date_str = datetime.now().strftime("%Y%m%d")
    listing_ID = str.split(listingURL, "/")[-1]

    file_path = os.path.join(abs_path_data, f'Homegate_{listing_ID}_{date_str}.html')


    try:
        # Get URL and save it
        response = requests.get(listingURL)
        string = response.text
        with open(file_path, "w", encoding="utf-8") as handle:
            handle.write(string)
        print(f'Downloaded')
        logging.info(f'Downloaded ({listingURL})')
    except requests.exceptions.Timeout:
        print("Timeout Error")
        quit(1)
