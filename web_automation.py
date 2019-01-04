# -*- coding: utf-8 -*-
"""
Created on Mon Dec 17 15:15:17 2018

@author: z3525552
"""


def login(file_name):
    
     
    with open(file_name) as f:
        contents = f.read().split('\n')
        username = contents[0]
        password = contents[1]

    
    return username, password


def web_browser(url):
    
    from selenium import webdriver
    from selenium.webdriver.common.keys import Keys

    chrome_driver = "C:/Users/z3525552/Downloads/chromedriver_win32/chromedriver.exe"
    
   



    driver = webdriver.Chrome(executable_path=chrome_driver)

    driver.get(url)

    user, passwd = login('scopus_login.txt')
    id_box = driver.find_element_by_name('username')
    id_box.send_keys(user)

    pass_box = driver.find_element_by_name('password')
    pass_box.send_keys(passwd)

    login_button = driver.find_element_by_id('login_submit_btn')
    login_button.click()

    benchmarking = driver.find_element_by_link_text('Benchmarking')
    benchmarking.click()


    overview = driver.find_element_by_link_text('Overview')
    overview.click()

    scopus = driver.find_element_by_class_name('external')
    scopus.click()

    driver.close()



url = 'https://www.scival.com/customer/authenticate/loginfull'