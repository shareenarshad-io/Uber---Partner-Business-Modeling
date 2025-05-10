#Given the operational scenarios and the provided dataset, answer the following questions:

import pandas as pd 
import numpy as np 

df = pd.read_csv('dataset_2.csv')
print(df.head(5))
print(df.info())
#How much would the total bonus payout be with Option 1?

#How much would the total bonus payout be with Option 2?

#How many drivers would qualify for a bonus under Option 1 but not under Option 2?

#What percentages of drivers online completed less than 10 trips, had an acceptance rate of less than 90%, and had a rating of 4.7 or higher?

#How much money (after expenses) does the taxi driver make per year without partnering with Uber?

#You are convincing the same driver above to buy a Town Car and partner with Uber. Assuming the new car is $40,000, how much would the driver's gross fares need to increase per week to fully pay for the car in year 1 and maintain the same yearly profit margin as before?