import json
import pymysql

my=pymysql.connect(host="localhost",user="root",password="password",db="data")
database=my.cursor()

with open("data.json","r") as file:
   data_json=json.load(file)
for i in range(len(data_json)):
    """CREATE TABLE `restaurants` (
      `id` int PRIMARY KEY,
      `restaurant_name` varchar(255),
      `delivery_time` varchar(255),
      `by_taxi` boolean,
      `delivery_duration` int,
      `cooking_duration` int,
      `created_at` datetime DEFAULT (now())
    );
    """

    restaurant_id = i
    restaurant_name = 'N\'' + data_json[i][0]['name'] + '\''
    delivery_time = 'N\'' + data_json[i][0]['deliveryTime'] + '\''
    delivery_duration = data_json[i][0]['deliveryDuration']
    cooking_duration = data_json[i][0]['cookingDuration']
    print(f"insert into restaurants (id,delivery_duration,cooking_duration,restaurant_name,delivery_time) values ({restaurant_id},{delivery_duration},{cooking_duration},{restaurant_name},{delivery_time});")
    database.execute( f'insert into restaurants (id,delivery_duration,cooking_duration,restaurant_name,delivery_time) values ({restaurant_id},{delivery_duration},{cooking_duration},{restaurant_name},{delivery_time});')

    """CREATE TABLE `reviews` (
      `id` int AUTO_INCREMENT PRIMARY KEY,
      `rate` float DEFAULT 0,
      `rate_count` int,
      `restaurant_id` int NOT NULL,
      `created_at` datetime DEFAULT (now())
    );""",
    rate = data_json[i][0]['rate']
    rate_count = data_json[i][0]['rateCount']

    database.execute(f'insert into reviews (rate,rate_count,restaurant_id) values ({rate},{rate_count},{restaurant_id});')

    """CREATE TABLE `addresses` (
      `id` int AUTO_INCREMENT PRIMARY KEY,
      `restaurant_id` int NOT NULL,
      `full_address` varchar(255),
      `city` varchar(255),
      `area` varchar(255),
      `lat` varchar(255),
      `lng` varchar(255),
      `created_at` datetime DEFAULT (now())
    );""",
    full_address = '\'' + data_json[i][0]['fullAddress'] + '\''
    city = data_json[i][0]['cityId']
    area = data_json[i][0]['areaId']
    lat = '\'' + data_json[i][0]['lat'] + '\''
    lng = '\'' + data_json[i][0]['lng'] + '\''

    database.execute(f'insert into addresses (restaurant_id,city,area,lat,full_address,lng) values ({restaurant_id},{city},{area},{lat},{full_address},{lng});')

    """CREATE TABLE `restaurant_active_periods` (
      `id` int AUTO_INCREMENT PRIMARY KEY,
      `restaurant_id` int NOT NULL,
      `meal_type` varchar(30),
      `day` varchar(30),
      `from` time,
      `to` time
    );""",

    for meals in data_json[i][2]['meals']:
        meal_typs = ['', 'breakfast', 'lunch ', 'dinner']
        meal_type = '\'' + meal_typs[meals['mealTypeId']] + '\''
        days = ['Saturday', 'Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']
        day = '\'' + days[meals['day']] + '\''
        froms = '\'' + meals['from'] + '\''
        to = '\'' + meals['to'] + '\''
        database.execute(f'insert into restaurant_active_periods ( restaurant_id,meal_type,`day`,`from`, `to`) values ({restaurant_id},{meal_type},{day},{froms},{to});')

    """CREATE TABLE `foods` (
      `id` int PRIMARY KEY,
      `food_name` varchar(255),
      `category` varchar(255),
      `sub_category` varchar(255),
      `restaurant_id` int NOT NULL,
      `price` int,
      `discount_percentage` int,
      `created_at` datetime DEFAULT (now())
    );""",

    """CREATE TABLE `ingredients` (
      `id` int AUTO_INCREMENT PRIMARY KEY,
      `food_id` int NOT NULL,
      `ingredient_name` varchar(255),
      `created_at` datetime DEFAULT (now())
    );""",

    id_food = data_json[i][1]['categories'][0]['sub']

    for p in range(len(data_json[i][1]['categories'])):
        sub_category = 'N\'' + data_json[i][1]['categories'][p]['title'] + '\''
        for food in data_json[i][1]['categories'][p]["sub"][0]['food']:
            id_food = food['id']
            food_name = 'N\'' + food['title'] + '\''
            price = food['price']
            discount_percentage = food['discountPercentage']
            ingredients_name = 'N\'' + food['ingredient'] + '\''
            a = f'insert into foods (id,food_name,sub_category,price,discount_percentage,restaurant_id) values ({id_food},{food_name},'
            inser = (a + sub_category + f',{price},{discount_percentage},{restaurant_id});')
            database.execute(inser)
            database.execute(f'insert into ingredients (food_id,ingredient_name) values ({id_food},{ingredients_name});')

    my.commit()
my.close()