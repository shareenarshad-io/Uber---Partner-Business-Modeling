#Given the operational scenarios and the provided dataset, answer the following questions:

import pandas as pd 
import numpy as np 

df = pd.read_csv('dataset_2.csv')
print(df.head(5))
print(df.info())
#How much would the total bonus payout be with Option 1?


# convert accept rate to float from string to force conditions later
df['Accept Rate'] = df['Accept Rate'].apply(lambda x: float(x[:-1]))
df

# filter by given condition
first_option_df = df[(df['Supply Hours'] >= 8) & (df['Trips Completed'] >= 10) & 
                     (df['Accept Rate'] >= 90) & (df['Rating'] >= 4.7)]
first_option_df

first_option_total_payout = 50 * len(first_option_df)
print('$'+str(first_option_total_payout))

#answer: $1050

#How much would the total bonus payout be with Option 2?


# filter by given condition
second_option_df = df[(df['Trips Completed'] >= 12) & (df['Rating'] >= 4.7)]
second_option_df

second_option_total_payout = 4 * second_option_df['Trips Completed'].sum()
print('$'+str(second_option_total_payout))

#$2976

#How many drivers would qualify for a bonus under Option 1 but not under Option 2?

# merge all and see if both dataset includes the driver from _merge column
df_all = first_option_df.merge(second_option_df, on=first_option_df.columns.to_list(), 
                   how='left', indicator=True)
df_all

# included by only option 1
print(df_all[df_all["_merge"] == 'left_only']) #answer

#What percentages of drivers online completed less than 10 trips, had an acceptance rate of less than 90%, and had a rating of 4.7 or higher?

# filter with given condition
less_trips_df = df[(df['Trips Completed'] < 10) & (df['Accept Rate'] < 90) & (df['Rating'] >= 4.7)]
less_trips_df
print(str(len(less_trips_df) / len(df) * 100)+"%") # answer turned to percentage

#How much money (after expenses) does the taxi driver make per year without partnering with Uber?

total_weeks_per_year = 52
weeks_off = 3
fare_per_day = 200 
workday_per_week = 6
total_months_per_year = 12
# expenses
gas_per_week = 200
insurance_per_month = 400
vehicle_rent_by_week = 500

total_expenses = (gas_per_week + vehicle_rent_by_week) * (total_weeks_per_year - weeks_off) + insurance_per_month * total_months_per_year
print("$"+str(total_expenses))

total_revenue = (total_weeks_per_year - weeks_off) * workday_per_week * fare_per_day
print("$"+str(total_revenue))

profit_margin = (total_revenue - total_expenses) / total_revenue
print(str(round(profit_margin * 100, 2)) + "%")

#You are convincing the same driver above to buy a Town Car and partner with Uber. Assuming the new car is $40,000, how much would the driver's gross fares need to increase per week to fully pay for the car in year 1 and maintain the same yearly profit margin as before?

# calculate new expenses
gas_per_week = gas_per_week * 1.05
insurance_per_month = insurance_per_month * 0.8
new_car = 40000

new_total_expenses = new_car + gas_per_week * (total_weeks_per_year - weeks_off) + insurance_per_month * total_months_per_year
print("$"+str(new_total_expenses))

# profit margin is the total revenue from previous question minus new expenses
new_profit_margin = (total_revenue - new_total_expenses) / total_revenue
print(str(round(new_profit_margin * 100, 2)) + "%")

# calculate the weekly fare increase
fare_increase = total_revenue * (profit_margin - new_profit_margin) / (total_weeks_per_year - weeks_off)
print("$"+str(round(fare_increase, 2)))