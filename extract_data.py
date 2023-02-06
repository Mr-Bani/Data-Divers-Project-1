import requests
import json
import os
import logging
from requests.exceptions import HTTPError, ConnectionError, Timeout, RequestException
import sys

def extract_data(urls):
    logging.basicConfig(filename='delino_eror.log', filemode='w', format='%(asctime)s %(levelname)s: %(message)s')
    logger = logging.getLogger()
    logger.setLevel(logging.DEBUG)
    restaurants = []
    try:
      for url in urls:
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
        restaurants.append(restaurant_data)
      save_file(restaurants)
    except HTTPError as http_err:
          logger.error('HTTP error occurred: {}'.format(http_err))
    except ConnectionError as conn_err:
          logger.error('Connection error occurred: {}'.format(conn_err))
    except Timeout as timeout_err:
         logger.error('Timeout error occurred: {}'.format(timeout_err))
    except RequestException as req_err:
            logger.error('Request error occurred: {}'.format(req_err))



def save_file(data):

    entry=data
    if os.path.isfile("data.json"):
        os.remove("data.json")
    with open("data.json", mode='w', encoding='utf-8') as f:
        f.write(json.dumps(entry, indent=2))

sys.modules[__name__] = extract_data


