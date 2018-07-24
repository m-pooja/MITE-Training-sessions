# -*- coding: utf-8 -*-
"""
Created on Wed Jul 11 14:12:10 2018

@author: pooja
"""
"""
define a function called plane_ride_cost that takes a string, 
city, as input.
The function should return a different price depending on 
the location.
Below are the valid destinations and their corresponding
 round-trip prices.
•	"Charlotte": 183
•	"Tampa": 220
•	"Pittsburgh": 222
•	"Los Angeles": 475
"""
def plane_ride_cost(city):
  if city == "Charlotte":
    return 183
  elif city == "Tampa":
    return 220
  elif city == "Pittsburgh":
    return 222
  elif city == "Los Angeles":
    return 475
"""
Hotel cost
"""
def hotel_cost(nights,typeR):
    tr=typeR.lower()
    if tr=='single':
        return nights*2000
    elif tr=='double':
        return nights*4000
    elif tr=='deluxe':
        return nights*6000
    elif tr=='luxury':
        return nights*8000

"""
Below your existing code, define a function called 
rental_car_cost with an argument called days.
Calculate the cost of renting the car:
•	Every day you rent the car costs INR40.
•	if you rent the car for 7 or more days, 
you get INR50 off your total.
•	Alternatively (elif), if you rent the car for 3 
or more days, you get $20 off your total.
•	You cannot get both of the above discounts.
Return that cost.

"""




