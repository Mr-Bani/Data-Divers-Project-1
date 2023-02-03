import requests
import json
def extract_data(url):
    restaurant_data=[]
    u = url.replace('https://www.delino.com/restaurant/', 'https://www.delino.com/restaurant/data/')
    response = requests.get(u)
    restaurant = response.json()
    restaurant_data.append(restaurant)
    id = restaurant["id"]
    menu_req = requests.get('https://www.delino.com/restaurant/menu/' + id)
    menu = menu_req.json()
    restaurant_data.append(menu)
    info_req = requests.get('https://www.delino.com/restaurant/info/' + id)
    info= info_req.json()
    restaurant_data.append(info)
    return restaurant_data



