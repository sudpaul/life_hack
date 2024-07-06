# -*- coding: utf-8 -*-
"""
Created on Tue Dec 18 14:44:57 2018

@author: z3525552
"""
import requests
def api_key(file_name):
    
    '''Input is api file and return the access key
   
    Parameters
    ----------
    file_name : str 
               api file name
    Returns
    ----------
     key : str
           api access key
           
    '''
        
    with open(file_name) as f:
        key = f.read().strip()
    
    return key



def get_data(date):
    
    '''
    
    Parameters
    ----------
    date : str 
           date format YYYY-MM-DD
    Returns
    ----------
    status_code : str
                http respone status code for unsuccessful request  
           
    data  : str 
            successful response json data 
    
    error : int
            http failure 0
            
    '''
        
    key = api_key('../fixer_io.txt')
    base_url ="http://data.fixer.io/api/{find}?access_key={k}".format(find=date,k=key)
    
        
    try:
        response = requests.get(url=base_url)
        
        if not response.status_code == 200:
            
            return response.status_code
        else:
       
            response_data = response.json()       
            
                      
            return response_data
        
    except:
          return 0
    
def exchange_rate(base='AUD'):
    '''Return latest exchange rate of 168 currencies base currency ERU'''
    currency = get_data('latest')
    usd = currency['rates']['USD']
    rate = currency['rates'][base]/usd
    return f'1 USD change to {base} {rate:.3f}' 
   
    
def convert_currency(base,change_currency, amount):
    currency = get_data('latest').get('rates')
    base_currency = currency[base]
    dest_currency  = currency[change_currency]
    return round((dest_currency/base_currency)*amount,2)

    
    
      
def historical_rate(date):
    '''Input is date and return historical rate exchange rate of 168 currencies
    base currency ERU
    Parameters
    ----------
    date : str 
           date format YYYY-MM-DD
    Returns
    ----------
    data : str
           json response data
    '''    
    return get_data(date)

def all_symbols():
    '''Return all 168 currency symbols from the api call'''
    return get_data("symbols")