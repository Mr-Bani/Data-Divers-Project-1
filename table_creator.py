from sqlalchemy import create_engine
from sqlalchemy.sql import text

user = 'user_group10'
password = 'X$UubR^wQEn#KKg6'
host = '37.32.5.76:3306'
db = 'group10'
engine = create_engine(f'mysql+mysqlconnector://{user}:{password}@{host}/{db}')
queries = ("""CREATE TABLE `restaurants` (
  `id` int PRIMARY KEY,
  `restaurant_name` varchar(255),
  `delivery_time` varchar(255),
  `by_taxi` boolean,
  `delivery_duration` int,
  `cooking_duration` int,
  `created_at` datetime DEFAULT (now())
);
""", 
"""CREATE TABLE `addresses` (
  `id` int PRIMARY KEY,
  `restaurant_id` int NOT NULL,
  `full_address` varchar(255),
  `city` varchar(255),
  `area` varchar(255),
  `lat` varchar(255),
  `lng` varchar(255),
  `created_at` datetime DEFAULT (now())
);""",
"""CREATE TABLE `reviews` (
  `id` int PRIMARY KEY,
  `rate` float DEFAULT 0,
  `rate_count` int,
  `restaurant_id` int NOT NULL,
  `created_at` datetime DEFAULT (now())
);""",
"""CREATE TABLE `restaurant_active_periods` (
  `id` int PRIMARY KEY,
  `restaurant_id` int NOT NULL,
  `meal_type` varchar(30),
  `day` varchar(30),
  `from` time,
  `to` time
);""",  
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
  `id` int PRIMARY KEY,
  `food_id` int NOT NULL,
  `ingredient_name` varchar(255),
  `created_at` datetime DEFAULT (now())
);""", 
"""ALTER TABLE `addresses` ADD FOREIGN KEY (`restaurant_id`) REFERENCES `restaurants` (`id`);""", 
"""ALTER TABLE `restaurant_active_periods` ADD FOREIGN KEY (`restaurant_id`) REFERENCES `restaurants` (`id`);""",
"""ALTER TABLE `reviews` ADD FOREIGN KEY (`restaurant_id`) REFERENCES `restaurants` (`id`);""", 
"""ALTER TABLE `foods` ADD FOREIGN KEY (`restaurant_id`) REFERENCES `restaurants` (`id`);""", 
"""ALTER TABLE `ingredients` ADD FOREIGN KEY (`food_id`) REFERENCES `foods` (`id`);""")

with engine.connect() as con:
    for query in queries:
        con.execute(text(query))


