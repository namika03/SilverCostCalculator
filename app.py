import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import streamlit as st
# Load dataset
df=pd.read_csv('statewise.csv')
df = pd.read_csv('historical.csv')
# Streamlit app
st.title("Silver Cost Calculator and Historical Price Chart")   
st.sidebar.title("Input Parameters")
def user_input_features():
    weight = st.sidebar.number_input("Enter weight of silver", min_value=0.0, step=0.1)
    weight_unit = st.sidebar.selectbox("Select weight unit", ("grams", "kilograms"))
    price_per_gram = st.sidebar.number_input("Enter current price of silver per gram (INR)", min_value=0.0, step=0.1)
    currency = st.sidebar.selectbox("Select currency for conversion", ("INR", "USD"))
    return weight, weight_unit, price_per_gram, currency
weight, weight_unit, price_per_gram, currency = user_input_features()
#weight to grams
if weight_unit == "kilograms":
    weight_in_grams = weight * 1000
else:
    weight_in_grams = weight
# cost in INR   
total_cost_inr = weight_in_grams * price_per_gram
# Currency conversion rates
conversion_rates = {
    "INR": 1,
    "USD": 91  # Example conversion rate
}
# Convert total cost to selected currency
total_cost = total_cost_inr * conversion_rates[currency]
st.subheader("Total Cost of Silver")
st.write(f"The total cost of {weight} {weight_unit} of silver is: {total_cost:.2f} {currency}")
# Historical Price Chart
st.subheader("Historical Silver Price Chart")
price_filter = st.selectbox("Filter historical prices by:", 
                            ("All Prices", "≤ 20,000 Silver_Price_INR_per_kg", "Between 20,000 and 30,000 Silver_Price_INR_per_kg", "≥ 30,000Silver_Price_INR_per_kg"))
if price_filter == "≤ 20,000 Silver_Price_INR_per_kg":
    filtered_df = df[df['Silver_Price_INR_per_kg'] <= 20000]
elif price_filter == "Between 20,000 and 30,000 Silver_Price_INR_per_kg":
    filtered_df = df[(df['Silver_Price_INR_per_kg'] > 20000) & (df['Silver_Price_INR_per_kg'] <= 30000)]
elif price_filter == "≥ 30,000 Silver_Price_INR_per_kg":
    filtered_df = df[df['Silver_Price_INR_per_kg'] >= 30000]
else:
    filtered_df = df
# Plotting the historical price chart
plt.figure(figsize=(10,5))
plt.plot(filtered_df['Month'], filtered_df['Silver_Price_INR_per_kg'], marker='o')
plt.title('Historical Siver Prices')
plt.xlabel('Month')
plt.ylabel('Silver Price (INR per kg)')
plt.xticks(rotation = 45)
plt.grid()
st.pyplot(plt)

