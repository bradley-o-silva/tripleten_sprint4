import pandas as pd
import numpy as np
import matplotlib as plt
from scipy import stats
import streamlit as st
import plotly.express as px

df_og = pd.read_csv('vehicles_us.csv')

# fork original data frame into one that will be modified
df_a1 = df_og

# create make_n_model column from model column
df_a1['make_n_model'] = df_a1['model']

# remove original model column
df_a1 = df_a1.drop(['model'], axis=1)

# new data frame with split value columns
new = df_a1['make_n_model'].str.split(" ", n=1, expand=True)
 
# making separate make column from new data frame
df_a1['make'] = new[0]
 
# making separate model column from new data frame
df_a1['model'] = new[1]

# create separate make_n_type column using .agg()
df_a1['make_n_type'] = df_a1[['make', 'type']].agg(' '.join, axis=1)

# Create condition map to rank conditions numerically
conditions_map = {
    'new': 5,
    'like new': 4,
    'excellent': 3,
    'good': 2,
    'fair': 1,
    'salvage': 0,
}

# Define new function for condition map
def map_condition(condition: str) -> int:
    return conditions_map[condition]

df_a1['condition_rank'] = df_a1['condition'].apply(map_condition)

# Create map to catagorize each car brand by country
make_country_map = {
    'acura': 'japanese',
    'bmw': 'german',
    'buick': 'american',
    'cadillac': 'american',
    'chevrolet': 'american',
    'chrysler': 'american',
    'dodge': 'american',
    'ford': 'american',
    'gmc': 'american',
    'honda': 'japanese',
    'hyundai': 'korean',
    'jeep': 'american',
    'kia': 'korean',
    'mercedes-benz': 'german',
    'nissan': 'japanese',
    'ram': 'american',
    'subaru': 'japanese',
    'toyota': 'japanese',
    'volkswagen': 'german',
}

# Define new function for make country map
def map_make_country(make: str) -> str:
    return make_country_map[make]

df_a1['make_country'] = df_a1['make'].apply(map_make_country)

# Create subset of only sedans
df_sedan = df_a1.loc[df_a1['type'] == 'sedan']

# Create subset with only the columns we are interested in
df_sedan = df_sedan[['price', 'model_year', 'condition', 'odometer', 'condition_rank', 'make_country']].copy()

# Drop rows where 'model_year' and 'odometer' have missing values

# axis = 0 indicates rows are being dropped (axis = 1 would indicated columns are being dropped)
# how = "any" indicates to drop all rows with one or more missing values
df_sedan = df_sedan.dropna(axis = 0, how = "any")



st.header('DataFrame of Sedans', divider='blue')

st.dataframe(df_sedan, use_container_width=True)



st.header('Distribution of Sedan Prices', divider='blue')

fig3 = px.histogram(df_sedan, 
                    x='price', 
                    color='make_country',
                    nbins=65)

# Use this to show figure of plotly express histogram 
st.plotly_chart(fig3)



st.header('Average Sedan Price by Condition', divider='blue')

fig4 = px.histogram(df_sedan, x='condition_rank', y='price',
             color='make_country', barmode='group',
             histfunc='avg', height=400,
             labels={'condition_rank': '0 = salvage, 1 = fair, 2 = good, 3 = excellent, 4 = like new, 5 = new'})

# Use this to show figure of plotly express histogram 
st.plotly_chart(fig4)



st.header('Model Year vs. Odometer Reading for Sedans', divider='blue')

fig5 = px.scatter(df_sedan, x='model_year', 
                  y='odometer', color='make_country', 
                  size='condition_rank',
                  labels={'model_year': 'Model Year', 
                      'odometer': 'Odometer Reading (in Miles)'})

# Use this to show figure of plotly express histogram 
st.plotly_chart(fig5)



# Group the average 'price' of a vehicle by 'model_year' and 'make_country'
df_sedan_price_avg_by_year = df_sedan.groupby(['model_year', 'make_country'])['price'].mean().reset_index() 



st.header('Average Sedan Price by Model Year', divider='blue')

fig6 = px.line(df_sedan_price_avg_by_year, 
              x='model_year', y='price', 
              color='make_country',
              labels={'model_year': 'Model Year', 
                      'price': 'Average Price'})

# Use this to show figure of plotly express histogram 
st.plotly_chart(fig6)



st.header('Did you find this data interesting, informative, and well presented?', divider='blue')

yes = st.checkbox("Yes") 

if yes: 
    st.write("Thank you for engaging!")

no = st.checkbox("No") 

if no: 
    st.write("Please let me know where I can improve!")