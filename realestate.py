# -*- coding: utf-8 -*-
"""
Created on Sun Dec  9 19:17:48 2018

@author: Sudipta

"""

def get_data(location, post_code):
    
    from requests import get
    from bs4 import BeautifulSoup
    import pandas as pd
    from time import sleep
    from random import randint
    from collections import defaultdict
    
    data  = defaultdict(list)
    headers = ({'User-Agent':'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36'})
    url = 'https://www.realestate.com.au/buy/property-house-in-{loc},+nsw+{code}/list-'.format(loc=location, code=post_code)
    
    n_pages = 0

    for page in range(0,40):
        n_pages += 1
        response = get(url+str(n_pages), headers= headers)
        html_soup = BeautifulSoup(response.text, 'html.parser')

        house_containers = html_soup.find_all('div', class_="residential-card__content")
        if house_containers != []:       
           for house in house_containers:   
               try:
                   data["price"].append(house.find_all('span', class_='property-price')[0].text)
               except:
                   data["price"].append(None)
            
               try:
                   data["location"].append(house.find_all('span', class_='')[1].text)
               except:
                   data["location"].append(None)
             
               try:
                   data["property_type"].append(house.find_all('span', class_="residential-card__property-type")[0].text)
               except:
                   data["property_type"].append(None)
             
               try:
                   data["beds"].append(house.find_all('span', class_="general-features__icon general-features__beds")[0].text)
               except:
                   data["beds"].append(None)
               try:
                   data["baths"].append(house.find_all('span', class_="general-features__icon general-features__baths")[0].text)
               except:
                   data["baths"].append(None)
            
               try:
                   data["parking"].append(house.find_all('span', class_="general-features__icon general-features__cars")[0].text)
               except:
                   data["parking"].append(None)
                            
               try:
                   data["size_m2"].append(house.find_all('span', class_="property-size__icon property-size__land")[0].text)   
               except:
                   data["size_m2"].append(None)
        else:
              break
    
        sleep(randint(1,2))       

    df = pd.DataFrame.from_dict(data)
 
    print('You scraped {} pages containing {} properties.'.format(n_pages, df.shape[0]))
    
    return df

def get_price(series):
     
    import re
    import numpy as np    
    #Million dollors string check
    #Price Guide $1.5M, $1.19 million, For Sale $1,35M - $1,45M,$1.05 million
    #Price Guide $1.6Mil-$1.7Mil, JUST $1.95Mil, $ 1.228 Mil 
    #re.findall(r'\$\d+\,?\d?\.?\d?', million_mask
    #To do add '0000000 or ./, 000000 concat string 
    #Finally clean price value
    def clean_price(string):
            
          num = re.sub('[^\d]','', string)
          
          return int(num.strip())
        
    if '$' in series:
        match = re.findall(r'\$.*',series)
        value = match[0]
          
        if '-' in value:     
            p1, p2 = value.split('-')
            price = round((clean_price(p1) + clean_price(p2))/2, 0)
            return int(price)
            
        else:
            return clean_price(value)
             
    return np.nan
   

def clean_data(df):
    
    import pandas as pd
    
    df['beds'] = pd.to_numeric(df['beds'], errors='coerce')
    df['baths'] = pd.to_numeric(df['baths'], errors='coerce')
    df['parking'] = pd.to_numeric(df['parking'], errors='coerce')
    df['size_m2'] = pd.to_numeric(df['size_m2'], errors = 'coerce')
    
    df['price'] = df['price'].apply(get_price)
    

def get_lat_lon(location):
    
    import requests
    with open('../google_geocode_api.txt') as f:
        token = f.read().strip()
    
    if location.startswith('Address available on request'):
        location = location.replace('Address available on request,', '')
      
    try:
        location = location + ' NSW, Australia' 
        url = f'https://maps.googleapis.com/maps/api/geocode/json?address={location}&key={token}'
        response = requests.get(url)
        if not response.status_code == 200:
            return response.status_code, 0
        data = response.json()
        lat = data['results'][0]['geometry']['location']['lat']
        lng = data['results'][0]['geometry']['location']['lng']
    
        return lat, lng
    except:
        return 0.0, 0.0
    
     
   
        
        
    
    