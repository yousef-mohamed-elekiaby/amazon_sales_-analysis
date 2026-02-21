import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.title("Amazon Sales Data Analysis")

df = r"C:\Users\Ekiaby\OneDrive\Desktop\amazon_sales_dataset.csv"

st.subheader("Dataset Preview")
st.dataframe(df.head())

st.subheader("Revenue by Category")
revenue = df.groupby("Product_Category")["Revenue"].sum()
st.bar_chart(revenue)