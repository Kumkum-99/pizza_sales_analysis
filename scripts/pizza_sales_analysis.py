import pandas as pd
import os

# -------------------------------
# Load Data
# -------------------------------
pizzas = pd.read_csv("../data/raw/pizzas.csv")
order_details = pd.read_csv("../data/raw/order_details.csv")
orders = pd.read_csv("../data/raw/orders.csv")
pizza_types = pd.read_csv("../data/raw/pizza_types.csv", encoding="cp1252")

# -------------------------------
# Merge Datasets
# -------------------------------
df = (order_details
      .merge(pizzas, on="pizza_id", how="left")
      .merge(orders, on="order_id", how="left")
      .merge(pizza_types, on="pizza_type_id", how="left"))

# -------------------------------
# Revenue Calculations
# -------------------------------
df['revenue'] = df['quantity'] * df['price']
df['date'] = pd.to_datetime(df['date'])
df['time'] = pd.to_datetime(df['time'], format='%H:%M:%S')
df['hour'] = df['time'].dt.hour

# Total revenue 2015
total_revenue_2015 = df[df['date'].dt.year == 2015]['revenue'].sum()
print("Total Revenue 2015:", total_revenue_2015)

# Top pizza category by revenue
top_category = df.groupby('category')['revenue'].sum().idxmax()
print("Top Category by Revenue:", top_category)

# Most ordered pizza
top_pizza = df.groupby('name')['quantity'].sum().idxmax()
print("Most Ordered Pizza:", top_pizza)

# Peak order hour
peak_hour = df.groupby('hour')['revenue'].sum().idxmax()
print("Busiest Hour by Revenue:", peak_hour)

# Time of day classification
def get_time_of_day(hour):
    if 5 <= hour < 12:
        return "Morning"
    elif 12 <= hour < 17:
        return "Afternoon"
    elif 17 <= hour < 21:
        return "Evening"
    else:
        return "Night"

df['time_of_day'] = df['hour'].apply(get_time_of_day)
print(df.groupby('time_of_day')['revenue'].sum())
