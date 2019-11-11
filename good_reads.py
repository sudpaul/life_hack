# -*- coding: utf-8 -*-
"""
Created on Thu Dec  6 11:26:57 2018

@author: z3525552
"""
import requests

def api_key(file_name):
     
    with open(file_name) as f:
        key = f.read().strip()
    return key

def api_query(api_file, isbn13): 
     
    key = api_key(api_file)
    base_url ="https://www.goodreads.com/book/review_counts.json"
    query = {"key":key,"isbns": isbn13}
    try:
        response = requests.get(url=base_url, params=query)
        if not response.status_code == 200:
            return response.status_code
        else:
       
            response_data = response.json()       
            return response_data
    except:
          return 0