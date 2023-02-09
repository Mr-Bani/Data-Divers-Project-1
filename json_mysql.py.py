import json
from sqlalchemy import create_engine
from sqlalchemy.sql import text


user = 'user_group10'
password = 'X$UubR^wQEn#KKg6'
host = '37.32.5.76:3306'
db = 'group10'
engine = create_engine(f'mysql+mysqlconnector://{user}:{password}@{host}/{db}')


id_food_table=[]
queries=(""" ALTER TABLE `ingredients` MODIFY  `ingredient_name` varchar(700) ;""",
"""ALTER TABLE `ingredients` DROP `id` ;""",
"""ALTER TABLE `restaurant_active_periods` DROP `id` ;""",
"""ALTER TABLE `reviews` DROP `id` ;""",
"""ALTER TABLE `addresses` DROP `id` ;""",
"""ALTER TABLE `ingredients` ADD id INT AUTO_INCREMENT PRIMARY KEY;""",
"""ALTER TABLE `restaurant_active_periods` ADD id INT AUTO_INCREMENT PRIMARY KEY;""",
"""ALTER TABLE `reviews` ADD id INT AUTO_INCREMENT PRIMARY KEY;""",
"""ALTER TABLE `addresses` ADD id INT AUTO_INCREMENT PRIMARY KEY;"""   )

con =  engine.connect()

with open("data.json","r") as file:
   data_json=json.load(file)


for query in queries:
  con.execute(text(query))



for i in range(len(data_json)):

    #insert TABLE `restaurants`

    restaurant_id = i
    restaurant_name = data_json[i][0]['name']
    delivery_time = data_json[i][0]['deliveryTime']
    if (restaurant_name != None):
        restaurant_name = '\'' + restaurant_name.replace('N\'', ' ') + '\''
    else:
        restaurant_name = '\'' + '' + '\''
    if (delivery_time != None):
        delivery_time = '\'' + delivery_time.replace('N\'', ' ') + '\''
    else:
        delivery_time = '\'' + '' + '\''

    delivery_duration = data_json[i][0]['deliveryDuration']
    cooking_duration = data_json[i][0]['cookingDuration']
    inRamadan = data_json[i][0]['inRamadan']
    con.execute(f'insert into restaurants (id,delivery_duration,cooking_duration,restaurant_name,delivery_time) values ({restaurant_id},{delivery_duration},{cooking_duration},{restaurant_name},{delivery_time});')
    engine.commit()

    #insert TABLE `reviews`
    rate = data_json[i][0]['rate']
    rate_count = data_json[i][0]['rateCount']
    con.execute(f'insert into reviews (rate,rate_count,restaurant_id) values ({rate},{rate_count},{restaurant_id});')
    engine.commit()


    #insert TABLE `addresses`
    full_address = 'N\'' + data_json[i][0]['fullAddress'] + '\''
    city = data_json[i][0]['cityId']
    area = data_json[i][0]['areaId']
    lat = data_json[i][0]['lat']
    lng =  data_json[i][0]['lng']
    if (city==None):city=0
    if(area==None):area=0
    if (lat!=None):lat = '\'' + lat + '\''
    else:lat ='\'' +''+ '\''
    if (lng!=None):lng = '\'' + lng + '\''
    else:lng = '\'' +''+ '\''
    con.execute(f'insert into addresses (restaurant_id,city,area,lat,full_address,lng) values ({restaurant_id},{city},{area},{lat},{full_address},{lng});')
    engine.commit()

    #insert TABLE `restaurant_active_periods`
    if data_json[i][2]['meals']!=None:
      for meals in data_json[i][2]['meals']:
        meal_typs = ['', 'breakfast', 'lunch ', 'dinner']
        meal_type = '\'' + meal_typs[meals['mealTypeId']] + '\''
        days = ['Saturday', 'Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']
        day = '\'' + days[meals['day']] + '\''
        froms = '\'' + meals['from'] + '\''
        to = '\'' + meals['to'] + '\''
        con.execute(f'insert into restaurant_active_periods ( restaurant_id,meal_type,`day`,`from`, `to`) values ({restaurant_id},{meal_type},{day},{froms},{to});')
        engine.commit()



    #insert TABLE `foods`
    #insert TABLE `ingredients`



    if(len(data_json[i][1]['categories'])>0):
      id_food = data_json[i][1]['categories'][0]['sub']

      for p in range(len(data_json[i][1]['categories'])):
        sub_category = 'N\'' + data_json[i][1]['categories'][p]['title'] + '\''
        for food in data_json[i][1]['categories'][p]["sub"][0]['food']:
            id_food = food['id']
            namefood=food['title'].replace('\'',' ')
            food_name = 'N\'' + namefood + '\''
            price = food['price']
            discount_percentage = food['discountPercentage']
            food_ingredient=food['ingredient'].replace('\'',' ')
            ingredients_name = 'N\'' + food_ingredient + '\''
            a = f'insert into foods (id,food_name,sub_category,price,discount_percentage,restaurant_id) values ({id_food},{food_name},'
            inser = (a + sub_category + f',{price},{discount_percentage},{restaurant_id});')
            print()
            if id_food not in id_food_table:
               con.execute(inser)
               id_food_table.append(id_food)
               con.execute(f'insert into ingredients (food_id,ingredient_name) values ({id_food},{ingredients_name});')
               engine.commit()
    engine.commit()
engine.close()




