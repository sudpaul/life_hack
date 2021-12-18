# -*- coding: utf-8 -*-
"""
Created on Thu Nov 25 10:10:48 2021

@author: Sudipta
"""
PETROL_PRICE_PER_LITRE = 1.59
print("*** Welcome to the fuel efficiency calculator! ***\n")

model_name = input("Enter your car model name: ")
distance_travelled = float(input("Enter distance travelled in km: "))
amount_paid = float(input("Enter the dollar value of fuel bought for the trip: AUD "))
fuel_consumed = amount_paid / PETROL_PRICE_PER_LITRE

efficency_l_per_100_km = fuel_consumed / distance_travelled * 100
efficency_km_per_l = distance_travelled / fuel_consumed

print(f'Your {model_name} performace')
print("*"*30)
print(f'\nYour car efficiency is {efficency_l_per_100_km:.2f} litres per 100 km.' )
print(f'Your {model_name} can travel {efficency_km_per_l:.2f} km on a litre of petrol')

print("\nThanks for using the program.")