import time, random, os, logging
import urllib
from urllib.request import Request, urlopen
from datetime import datetime
import requests
from tqdm import tqdm
from bs4 import BeautifulSoup
from urllib.parse import urljoin


base_url = 'https://www.homegate.ch/kaufen/'
id = 300160908
url = base_url + str(id)
div_headline_identifier = {"class":"schlagzeilen-content schlagzeilen-overview"}

########### sleep ###########
sleep_min = 5
sleep_max = 15
sleeptimes = list(range(sleep_min,sleep_max,1))

########### Data Name ###########
sub_dir = 'HomegateCrawlerDB'
sub_dir_logs = 'logs'
sub_dir_data = 'data'
log_file_name = 'homegate'
data_file_name = 'homegate-'+str(id)
timeout_duration = 5
num_latest_downloads = 1000
########### Data  ###########
abs_path = os.path.join(os.getcwd(),sub_dir)
abs_path_logs = os.path.join(abs_path,sub_dir_logs)
abs_path_data = os.path.join(abs_path,sub_dir_data)
#create path
if not os.path.exists(abs_path_logs):
    os.makedirs(abs_path_logs)
if not os.path.exists(abs_path_data):
    os.makedirs(abs_path_data)

latest_downloads = os.listdir(abs_path)
total_downloaded = len(latest_downloads)-1
total_timeouts = 0
total_other = 0
total_unknown_errors = 0
last_batch = 0



while True:
    id += 1
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


    file_path = os.path.join(abs_path_data, f'Homegate_{id}.html')
    #for urllib.error.HTTPError: HTTP Error 999: No Hacking
#    req = urllib.request.Request(
#        url,
#        data=None,
#        headers={'User-Agent': ("Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) "
#                                "AppleWebKit/537.36 (KHTML, like Gecko) "
#                                "Chrome/35.0.1916.47 Safari/537.36")})

    try:
        #Get URL and save it
        response = requests.get(base_url + str(id))
        string = response.text
        with open(file_path, "w") as handle:
            handle.write(string)

        total_downloaded += 1
        last_batch += 1
        print(f'Downloaded ({total_downloaded})')
        logging.info(f'Downloaded ({total_downloaded})')


    except:
        total_unknown_errors += 1
        print(f'Unknown Error ({total_unknown_errors})')
        logging.info(f'Unknown Error ({total_unknown_errors})')




