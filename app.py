import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from utils import calculate_revenue, classify_customer

# Load data
customers = pd.read_csv('outputs/cleaned_customers.csv')
orders = pd.read_csv('data/orders.csv')
products = pd.read_csv('data/products.csv')

# Clean products.csv
products['price'] = products['price'].str.replace('₹', '').str.strip().astype(float)
products['rating'] = products['rating'].fillna(round(products['rating'].mean(), 1))
products['category'] = products['category'].astype('category')

# Merge data
full_df = pd.merge(orders, customers, on='customer_id')
full_df = pd.merge(full_df, products, on='product_id')
full_df['revenue'] = full_df.apply(lambda row: calculate_revenue(row['price'], row['quantity'], row['discount_pct']), axis=1)

# Streamlit app
st.title('🛒 RetailSense Analytics Dashboard')

# Sidebar
st.sidebar.title('Filters')
category = st.sidebar.selectbox('Category', ['All'] + list(products['category'].unique()))
min_rating = st.sidebar.slider('Minimum Product Rating', 1.0, 5.0, 3.0)

# Filter data
if category != 'All':
    full_df = full_df[full_df['category'] == category]
full_df = full_df[full_df['rating'] >= min_rating]

# Overview metrics
st.header('Overview Metrics')
col1, col2, col3 = st.columns(3)
col1.metric('Total Revenue', f'₹{full_df["revenue"].sum():,.2f}')
col2.metric('Total Orders', len(full_df))
col3.metric('Average Product Rating', f'{full_df["rating"].mean():.2f}')

# Data table
st.header('Data Table')
st.dataframe(full_df.head(50))

# Charts
st.header('Charts')
col1, col2 = st.columns(2)
with col1:
    st.subheader('Revenue by Age Group')
    age_group_revenue = full_df.groupby('age_group')['revenue'].sum().reset_index()
    sns.barplot(x='age_group', y='revenue', data=age_group_revenue)
    st.pyplot(plt.gcf())
with col2:
    st.subheader('Price Distribution')
    sns.boxplot(x='category', y='price', data=full_df)
    st.pyplot(plt.gcf())

# File uploader
st.header('Upload CSV')
uploaded_file = st.file_uploader('Choose a CSV file')
if uploaded_file:
    df = pd.read_csv(uploaded_file)
    st.write(df.head(10))
    st.write(df.describe())