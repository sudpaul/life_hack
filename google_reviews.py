# -*- coding: utf-8 -*-
"""
Created on Tue Mar  5 13:47:54 2019

@author: z3525552
"""
import requests
import json
import time

def api_key(file_name):
    
     
    with open(file_name) as f:
        key = f.read().strip()
    
    return key

class GooglePlaces(object):
    
    def __init__(self, apiKey):
        super(GooglePlaces, self).__init__()
        self.apiKey = apiKey
 
    def search_places_by_coordinate(self, location, radius, types):
        base_url = "https://maps.googleapis.com/maps/api/place/nearbysearch/json"
        places = []
        params = {
            'location': location,
            'radius': radius,
            'types': types,
            'key': self.apiKey
        }
        res = requests.get(base_url, params = params)
        results =  json.loads(res.content)
        places.extend(results['results'])
        time.sleep(2)
        while "next_page_token" in results:
            params['pagetoken'] = results['next_page_token'],
            res = requests.get(base_url, params = params)
            results = json.loads(res.content)
            places.extend(results['results'])
            time.sleep(2)
        return places
 
    def get_place_setails(self, place_id, fields):
        base_url = "https://maps.googleapis.com/maps/api/place/details/json"
        params = {
            'placeid': place_id,
            'fields': ",".join(fields),
            'key': self.apiKey
        }
        res = requests.get(base_url, params = params)
        place_details =  json.loads(res.content)
        return place_details




if __name__ == '__main__':
    

    token = api_key('../google_geocode_api')
    google = GooglePlaces(token)
    places = google.search_places_by_coordinate("151.1,-33.87", "10", "restaurant")
    fields = ['name', 'formatted_address', 'international_phone_number', 'website', 'rating', 'review']
    
    
    for place in places:
        details = google.get_place_setails(place['place_id'], fields)
        try:
            website = details['result']['website']
        except KeyError:
            website = ""
 
        try:
            name = details['result']['name']
        except KeyError:
            name = ""
 
        try:
            address = details['result']['formatted_address']
        except KeyError:
            address = ""
 
        try:
            phone_number = details['result']['international_phone_number']
        except KeyError:
            phone_number = ""
 
        try:
            reviews = details['result']['reviews']
        except KeyError:
            reviews = []
        print("===================PLACE===================")
        print("Name:", name)
        print("Website:", website)
        print("Address:", address)
        print("Phone Number", phone_number)
        
        print("==================REWIEVS==================")
        for review in reviews:
            author_name = review['author_name']
            rating = review['rating']
            text = review['text']
            time = review['relative_time_description']
            profile_photo = review['profile_photo_url']
            print("Author Name:", author_name)
            print("Rating:", rating)
            print("Text:", text)
            print("Time:", time)
            print("Profile photo:", profile_photo)
            print("-----------------------------------------")
            
            
