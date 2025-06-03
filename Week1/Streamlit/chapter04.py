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
