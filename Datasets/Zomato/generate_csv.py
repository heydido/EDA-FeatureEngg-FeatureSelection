import os
import json
import pandas as pd

master_data_all_restaurants = []
for file in os.listdir('Datasets/Zomato/'):
    if file.endswith('.json'):
        with open('Datasets/Zomato/' + file) as f:
            responses = json.load(f)
            for response in responses:
                try:
                    restaurants_data = response['restaurants']
                except Exception as e:
                    pass
                for restaurant_data in restaurants_data:
                    master_data_all_restaurants.append(restaurant_data['restaurant'])

useful_data_all_restaurants = []
for master_data_a_restaurant in master_data_all_restaurants:
    useful_info = {
        'id': master_data_a_restaurant['id'],
        'name': master_data_a_restaurant['name'],
        'address': master_data_a_restaurant['location']['address'],
        'locality': master_data_a_restaurant['location']['locality'],
        'latitude': master_data_a_restaurant['location']['latitude'],
        'longitude': master_data_a_restaurant['location']['longitude'],
        'cuisines': master_data_a_restaurant['cuisines'],
        'currency': master_data_a_restaurant['currency'],
        'average_cost_for_two': master_data_a_restaurant['average_cost_for_two'],
        'has_online_delivery': master_data_a_restaurant['has_online_delivery'],
        'url': master_data_a_restaurant['url'],
        'photos_url': master_data_a_restaurant['photos_url'],
        'price_range': master_data_a_restaurant['price_range'],
        'aggregate_rating': master_data_a_restaurant['user_rating']['aggregate_rating'],
        'rating_text': master_data_a_restaurant['user_rating']['rating_text'],
        'rating_color': master_data_a_restaurant['user_rating']['rating_color'],
        'votes': master_data_a_restaurant['user_rating']['votes'],
        'is_delivering_now': master_data_a_restaurant['is_delivering_now'],
        'menu_url': master_data_a_restaurant['menu_url'],
        'switch_to_order_menu': master_data_a_restaurant['switch_to_order_menu']
    }
    useful_data_all_restaurants.append(useful_info)

pd.DataFrame(useful_data_all_restaurants).to_csv('Datasets/Zomato/zomato_dataset.csv', index=False,
                                                 columns=list(useful_data_all_restaurants[0].keys()))
