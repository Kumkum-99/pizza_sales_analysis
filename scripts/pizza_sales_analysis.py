#!/usr/bin/env python
# coding: utf-8

# In[57]:


import pandas as pd

# Load CSVs (use encoding fix if needed)
pizzas = pd.read_csv("../data/pizzas.csv")
order_details = pd.read_csv("../data/order_details.csv")
orders = pd.read_csv("../data/orders.csv")
pizza_types = pd.read_csv("../data/pizza_types.csv", encoding="cp1252")




# In[58]:


order_details.head()


# In[59]:


pizza_types.head()


# In[60]:


pizzas.head()


# In[61]:


pizza_types.head()


# In[62]:


#Merging all table


# Merge: order_details + pizzas
df = order_details.merge(pizzas, on="pizza_id", how="left")

# Merge: add order timestamps
df = df.merge(orders, on="order_id", how="left")

# Merge: add pizza type info
df = df.merge(pizza_types, on="pizza_type_id", how="left")

df



# 📊 Sales & Revenue
# 
# What was the total revenue generated in 2015?
# 
# Which pizza generated the highest revenue?
# 
# Which pizza category (Classic, Chicken, Veggie, Supreme) earned the most revenue?
# 
# What is the average order value (AOV) across all orders?

# In[63]:


# Compute revenue
df["revenue"] = df["quantity"] * df["price"]
total_revenue=df['revenue'].sum()
# Revenue by category (e.g., Chicken, Classic, Veggie)
revenue_by_category=(
                  df.groupby('category')['revenue']
                  .sum()
                  .sort_values(ascending=False)
    
)
revenue_by_category
   


# In[64]:


#What was the total revenue generated in 2015?
df['date']=pd.to_datetime(df['date'])
total_revenue_2015=df[df['date'].dt.year == 2015]['revenue'].sum()
total_revenue_2015
df['name']



# In[ ]:





# In[45]:


#Which pizza category (Classic, Chicken, Veggie, Supreme) earned the most revenue?
#.idxmax() → returns the index label (here, the category) of the maximum value.
#.max() → returns the value itself.
top_category=revenue_by_category.idxmax()
Revenue=revenue_by_category.max()
print("Top category:",top_category)
print("Revenue:",Revenue)


# In[46]:


#What is the average order value (AOV) across all orders?
#AOV=Number of OrdersTotal/ Revenue per Order​
revenue_per_order = df.groupby("order_id")["revenue"].sum()
aov=revenue_per_order.mean()
print("AOV:",aov)


# Which pizza was ordered the most times (by quantity)?
# 
# Which size (S, M, L, XL, XXL) sold the most units?
# 
# Which size contributed the most revenue?
# 
# What are the top 5 pizzas by total quantity sold?

# In[47]:


# Which pizza was ordered the most times (by quantity)
pizza_sales=df.groupby('name')['quantity'].sum()
top_pizza_sales=pizza_sales.idxmax()
top_quantity = pizza_sales.max()

print("most order_pizza:",top_quantity)
print("Most ordered pizaa:",top_pizza_sales)
pizza_sales


# In[48]:


#Which size (S, M, L, XL, XXL) sold the most units?
pizza_size=df.groupby('size')['quantity'].sum()

top_sale_pizza_size=pizza_size.idxmax()
print("Most sale pizza size:",top_sale_pizza_size)






# In[49]:


#Which size contributed the most revenue?
revenue_contribution_based_on_size=df.groupby('size')['revenue'].sum()
cont=revenue_contribution_based_on_size.idxmax();
print(revenue_contribution_based_on_size)
print("Most contribution on pizza sales by pizza size:",cont)



# In[50]:


#What are the top 5 pizzas by total quantity sold?
pizza_sales=df.groupby('name')['quantity'].sum()
top_5=pizza_sales.sort_values(ascending=False).head()
top_5


# In[51]:


df["date"] = pd.to_datetime(df["date"])
df["month"] = df["date"].dt.month
df['day']=df['date'].dt.day

monthly_revenue=df.groupby('month')['revenue'].sum()
max_month_revenue=monthly_revenue.max()
month=monthly_revenue.idxmax()

print("monthly_revenue:",monthly_revenue)
print('Month in which most revenue has:',month)


    


# In[52]:


df['weekday']=df['date'].dt.day_name()
revenue_by_weekday = df.groupby("weekday")["revenue"].sum().sort_values(ascending=False)

# Best day
best_day = revenue_by_weekday.idxmax()
best_revenue = revenue_by_weekday.max()

print("Revenue by weekday:\n", revenue_by_weekday)
print("Best day:", best_day, "with revenue:", best_revenue)


# In[55]:


#What are the peak order hours of the 
df["time"] = pd.to_datetime(df["time"], format="%H:%M:%S")

df["hour"] = df["time"].dt.hour
orders_by_hour = df.groupby("hour")["order_id"].nunique()
pizzas_by_hour = df.groupby("hour")["order_id"].count()
revenue_per_hour=df.groupby('hour')['revenue'].sum()
busiest_hour=revenue_per_hour.idxmax()
busiest_revenue=revenue_per_hour.max()
print("Unique orders per hour:\n", orders_by_hour)
print("Total pizzas sold per hour:\n", pizzas_by_hour)
print("Revenue by hour:\n", revenue_per_hour)
print("Busiest hour:", busiest_hour, "with revenue:", busiest_revenue)



# In[56]:


def get_time_of_day(hour):
    if 5 <= hour < 12:
        return "Morning"      # 5 AM - 11 AM
    elif 12 <= hour < 17:
        return "Afternoon"    # 12 PM - 4 PM
    elif 17 <= hour < 21:
        return "Evening"      # 5 PM - 8 PM
    else:
        return "Night"        # 9 PM - 4 AM

# Apply function
df["time_of_day"] = df["hour"].apply(get_time_of_day)

# Revenue by time of day
revenue_by_tod = df.groupby("time_of_day")["revenue"].sum().sort_values(ascending=False)
print(revenue_by_tod)

       
    


# In[ ]:





# In[ ]:





# In[ ]:




