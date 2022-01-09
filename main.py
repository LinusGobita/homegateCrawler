import time, random, os, logging
from datetime import datetime
import requests
from tqdm import tqdm
from bs4 import BeautifulSoup
from urllib.parse import urljoin


base_url = 'https://www.homegate.ch/kaufen/'
id = 3001609010

sub_dir = 'HomegateCrawlerDB'
sub_dir_logs = 'logs'
log_file_name = 'homegate-'+str(id)
timeout_duration = 5
num_latest_downloads = 1000
sleep_min = 1
sleep_max = 10
#div_headline_identifier = {"class":"schlagzeilen-content schlagzeilen-overview"}

sleeptimes = list(range(sleep_min,sleep_max,1))

abs_path = os.path.join(os.getcwd(),sub_dir)
abs_path_logs = os.path.join(abs_path,sub_dir_logs)
abs_path_data = os.path.join(abs_path,log_file_name)
if not os.path.exists(abs_path_logs):
    os.makedirs(abs_path_logs)

latest_downloads = os.listdir(abs_path)
total_downloaded = len(latest_downloads)-1
total_timeouts = 0
total_other = 0
total_unknown_errors = 0
last_batch = 0



while True:
    id += 1
    print(id)
    date_str = datetime.now().strftime("%Y%m%d")
    log_file = os.path.join(abs_path_logs, f'{log_file_name}_{date_str}.log')
    logging.basicConfig(
        level=logging.DEBUG,
        filename=log_file,
        filemode="a+",
        format="%(asctime)-15s %(message)s"
    )

    sleeptime = random.choice(sleeptimes)
    print(f'Sleeping: {sleeptime} \tLast bach-size: {last_batch}')
    logging.info(f'Sleeping: {sleeptime} \tLast bach-size: {last_batch}')
    time.sleep(sleeptime)
    last_batch = 0

    response = requests.get(base_url + str(id))
    print(base_url + str(id))
    print(response)
    try:
        file_path = os.path.join(abs_path_data, f'Homegate_{id}.webloc')
        with open(file_path, 'wb') as handle:
            for data in tqdm(response.iter_content()):
                handle.write(data)

        total_downloaded += 1
        last_batch += 1
        print(f'Downloaded ({total_downloaded})')
        logging.info(f'Downloaded ({total_downloaded})')


    except:
        total_unknown_errors += 1
        print(f'Unknown Error ({total_unknown_errors})')
        logging.info(f'Unknown Error ({total_unknown_errors})')




