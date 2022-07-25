# import packages
import json
import requests

# set up internal integration key
# set up database id (integration must have access to database)
# set up authorisation key
token = 'secret_******************************'

database_id = '*******************************'

headers = {
    "Authorization": f"Bearer {token}",
    "Notion-Version": "2022-06-28"
}

# define function to get full list of restaurants
def get_restaurants():
    url = f'https://api.notion.com/v1/databases/{database_id}/query'
    r = requests.post(url, headers={headers})
    result_dict = r.json()
    restaurant_result = result_dict['results']
    restaurants = []
    for restaurant in restaurant_result:
        restaurant_dict = restaurants_helper(restaurant)
        restaurants.append(restaurant_dict)
        return restaurants

# helper function for clarity
def restaurants_helper():
    restaurant_name = property['Restaurant']
    location = property['Location']
    dist = property['Walking distance (mins)']

    return {
        'restaurant_name': restaurant_name,
        'location': location,
        'dist': dist
    }

