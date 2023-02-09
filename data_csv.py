import json
import csv
from csv import DictWriter

with open("D:\data\\data.json", "r") as files:
  data_json = json.load(files)



restaurant = ['restaurant_id', 'restaurant_name', 'delivery_time', ' delivery_duration', 'cooking_duration','rate','rate_count' ,'full_address','city','area' ,'lat','lng','inRamadan']
mea=['restaurant_id','meal_type','day','froms','to']
category_dicta=['restaurant_id','category','id_food','food_name','price','discount_percentage','ingredients_name']

with open('D:\\restaurant.csv', 'a') as f_object:
    dictwriter_object = DictWriter(f_object,delimiter=',', fieldnames=restaurant)
    dictwriter_object.writeheader()
with open('D:\\restaurant_active_periods.csv', 'a') as meals_object:
    meals_object = DictWriter(meals_object,delimiter=',', fieldnames=mea)
    meals_object.writeheader()
with open('D:\\foods.csv', 'a') as categories_object:
    categories_object = DictWriter(categories_object,delimiter=',', fieldnames=category_dicta)
    categories_object.writeheader()

for i in range(len(data_json)):

    restaurant_id = i
    restaurant_name =  data_json[i][0]['name']
    delivery_time =  data_json[i][0]['deliveryTime']
    delivery_duration = data_json[i][0]['deliveryDuration']
    cooking_duration = data_json[i][0]['cookingDuration']
    rate = data_json[i][0]['rate']
    rate_count = data_json[i][0]['rateCount']
    dict_rate={'rate':rate,'rate_count':rate_count }
    full_address =  data_json[i][0]['fullAddress']
    city = data_json[i][0]['cityId']
    area = data_json[i][0]['areaId']
    lat =  data_json[i][0]['lat']
    lng =  data_json[i][0]['lng']
    inRamadan=data_json[i][0]['inRamadan']
    dict = {'restaurant_id': restaurant_id, 'restaurant_name': restaurant_name, 'delivery_time': delivery_time,'rate':rate,'rate_count':rate_count,
            ' delivery_duration': delivery_duration, 'cooking_duration': cooking_duration,'full_address': full_address ,'city':city,'area':area ,'lat':lat,'lng':lng ,'inRamadan':inRamadan}
    with open('D:\\restaurant.csv', 'a',encoding="utf-8") as file_restaurant:
       dictwriter_restaurant = DictWriter(file_restaurant, fieldnames= restaurant)
       dictwriter_restaurant.writerow(dict)

    print(restaurant_id)
    if data_json[i][2]['meals']!=None:
     for meals in data_json[i][2]['meals']:
         meal_typs = ['', 'breakfast', 'lunch ', 'dinner']
         meal_type = '\'' + meal_typs[meals['mealTypeId']] + '\''
         days = ['Saturday', 'Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']
         day = '\'' + days[meals['day']] + '\''
         froms = '\'' + meals['from'] + '\''
         to = '\'' + meals['to'] + '\''
         dict_meals={'restaurant_id':restaurant_id,'meal_type':meal_type,'day':day,'froms':froms,'to':to }
         with open('D:\\restaurant_active_periods.csv', 'a', encoding="utf-8") as f_object:
            dictwriter_object = DictWriter(f_object, fieldnames=mea)
            dictwriter_object.writerow(dict_meals)


    for p in range(len(data_json[i][1]['categories'])):
        category = 'N\'' + data_json[i][1]['categories'][p]['title'] + '\''
        for food in data_json[i][1]['categories'][p]["sub"][0]['food']:
            id_food = food['id']
            food_name = 'N\'' + food['title'] + '\''
            price = food['price']
            discount_percentage = food['discountPercentage']
            ingredients_name = 'N\'' + food['ingredient'] + '\''
            dict_category={'restaurant_id':restaurant_id,'category': category,'id_food':id_food,'food_name':food_name,'price':price,'discount_percentage':discount_percentage,'ingredients_name':ingredients_name}
            with open('D:\\foods.csv', 'a', encoding="utf-8") as categories_object:
                categories_object = DictWriter(categories_object, fieldnames=category_dicta)
                categories_object.writerow(dict_category)


