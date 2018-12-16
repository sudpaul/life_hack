# -*- coding: utf-8 -*-
"""
Created on Mon Dec 15 28:26:54 2018

@author: Sudipta
"""
def repayment(loan,rate, month):
    
    return loan*((rate*(1+rate)**month)/((1+rate)**month -1))

def lowest_payment(balance, interest_rate):

    monthlyPayment = 0
    monthlyInterestRate = interest_rate
    newbalance = balance

    while newbalance > 0:
        monthlyPayment += 100
        newbalance = balance

        for month in range(1,13):
            newbalance -= monthlyPayment
            newbalance += monthlyInterestRate * newbalance
      
    print (" Lowest Payment:", monthlyPayment)


balance = int(input("balance : "))
annualInterestRate = float(input("annualInterestRate :"))
