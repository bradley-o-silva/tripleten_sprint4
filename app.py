import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib as plt
from scipy import stats
import streamlit as st
import plotly.express as px

df_og = pd.read_csv('vehicles_us.csv')

# display data frame
st.write(df_og)

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

# Create a histogram of vehicle prices
fig1 = px.histogram(df_a1, x='price',
                  title="Distribution of Used Vehicle Prices")

# Use this to show figure of plotly express histogram 
# in 'app.py' for the Render Dashboard
st.plotly_chart(fig1)