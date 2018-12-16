# -*- coding: utf-8 -*-
"""
Created on Sun Dec  9 19:17:48 2018

@author: Sudipta
"""
headers = ({'User-Agent':
            'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36'})
base_url = 'https://www.realestate.com.au/buy/property-house-in-sydney,+nsw+2000/list-1'
url = 'https://www.realestate.com.au/buy/property-house-in-kellyville,+nsw+2155/list-1'
parametes  

from requests import get

response = get(base_url)

from bs4 import BeautifulSoup

html_soup = BeautifulSoup(response.text, 'html.parser')

house_containers = soup.find_all('div', class_="residential-card__content-wrapper")
 
first =house_containers[0]
 
first.find_all('span')
 
 <--------------> output
 
 [<span class="property-price ">Auction - $1,475,000</span>,
 <span class="">28 Kingfield Road, Kellyville</span>,
 <span aria-label="House property type" class="residential-card__property-type" role="text">House</span>,
 <span class="residential-card__with-comma"></span>,
 <span class="general-features__icon general-features__beds"> <!-- -->6</span>,
 <span class="general-features__icon general-features__baths"> <!-- -->6</span>,
 <span class="general-features__icon general-features__cars"> <!-- -->2</span>,
 <span aria-hidden="true" class="property-size__icon property-size__land"> <!-- -->550</span>,
 <span aria-hidden="true"> <!-- -->m²</span>,
 <span aria-hidden="true" class="agent__photo"><img alt="Mark Tasovac" class="agent__photo-image" src="https://i2.au.reastatic.net/120x160/53b9bfdc40bbd0af6b1730c2c2526b964546fb172a179d3b2aa59fef8b228539/main.jpg"/></span>,
 <span class="save_icon__hollow"></span>,
 <span class="save_icon__filled"></span>,
 <span class="listing-bookmark__text">Save</span>,
 <span class="residential-card__details-button-text">Details</span>,
 <span class="residential-card__details-button-icon"></span>]
 
price = first.find_all('span', class_='property-price')[0].text
location = first.find_all('span', class_='')[1].text
property_type = first.find_all('span', class_="residential-card__property-type")[0].text
beds = first.find_all('span', class_="general-features__icon general-features__beds")[0].text
baths = first.find_all('span', class_="general-features__icon general-features__baths")[0].text
car_parking = first.find_all('span', class_="general-features__icon general-features__cars")[0].text
property_size = first.find_all('span', class_="property-size__icon property-size__land")[0].text                          