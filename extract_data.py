import requests
import json
import os
import logging
from requests.exceptions import HTTPError, ConnectionError, Timeout, RequestException
import sys
import time
from random import randint

def extract_data(urls):
    counter = 0
    logging.basicConfig(filename='delino_eror.log', filemode='w', format='%(asctime)s %(levelname)s: %(message)s')
    logger = logging.getLogger()
    logger.setLevel(logging.DEBUG)
    for url in urls:
        try:
            time.sleep(randint(1,3))
            if url:
                restaurant_data=[]
                u = url.replace('https://www.delino.com/restaurant/', 'https://www.delino.com/restaurant/data/')
                response = requests.get(u, timeout=5)
                restaurant = response.json()
                restaurant_data.append(restaurant)
                id = restaurant["id"]
                menu_req = requests.get('https://www.delino.com/restaurant/menu/' + id, timeout=5)
                menu = menu_req.json()
                restaurant_data.append(menu)
                info_req = requests.get('https://www.delino.com/restaurant/info/' + id, timeout=5)
                info= info_req.json()
                restaurant_data.append(info)
                save_file(restaurant_data)
        except HTTPError as http_err:
            logger.error('HTTP error occurred: {}'.format(http_err))
        except ConnectionError as conn_err:
            logger.error('Connection error occurred: {}'.format(conn_err))
        except Timeout as timeout_err:
            logger.error('Timeout error occurred: {}'.format(timeout_err))
        except RequestException as req_err:
            logger.error('Request error occurred: {}'.format(req_err))
        print(counter)
        counter += 1



def save_file(entry):

    if os.path.isfile("data.json"):
        jsoncontent = None
        with open("data.json", mode='r', encoding='utf-8') as f:
            jsoncontent = json.load(f)
            jsoncontent.append(entry)
            f.close()
        with open("data.json", mode='w', encoding='utf-8') as f:
            f.write(json.dumps(jsoncontent, indent=2))            
            f.close()
    else:   
        firstjson = []
        firstjson.append(entry)     
        with open("data.json", mode='w', encoding='utf-8') as f:
            f.write(json.dumps(firstjson, indent=2))
            f.close()

sys.modules[__name__] = extract_data


