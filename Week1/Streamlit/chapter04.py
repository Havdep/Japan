import streamlit as st
import pandas as pd

st.header("Chai Data")

file = st.file_uploader("Upload File", type=["csv"])
print(file)

if file:
    df = pd.read_csv(file)
    print(df)
    st.subheader(f"File: {file.name}")
    st.dataframe(df)
    st.write(f"The file size is {file.size / 1024:.2f} KB")

if file:
    cities = df["City"].unique()
    selected_city = st.selectbox("Filter data by city", cities)
    filtered_city = df[df["City"] == selected_city]
    st.dataframe(filtered_city)
