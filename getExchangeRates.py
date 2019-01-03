# -*- coding: utf-8 -*-
"""
Created on Tue Dec 18 14:44:57 2018

@author: z3525552
"""
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
    import requests
    
    key = api_key('fixer_io.txt')
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
    
def exchange_rate():
    
    
    return get_data('latest')
   
    
    
    
    
      
def historical_rate(date):
    
            
    return get_data(date)

def all_symbols():
    
    return get_data("symbols")