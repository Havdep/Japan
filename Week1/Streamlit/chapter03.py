import streamlit as st

col1, col2 = st.columns(2)

with col1:
    coffee = st.image(
        "https://images.pexels.com/photos/885021/pexels-photo-885021.jpeg?auto=compress&cs=tinysrgb&w=600",
        width=200,
    )
    result1 = st.button("Coffee")
    if result1:
        st.success("You love Coffee")
with col2:
    chai = st.image(
        "https://images.pexels.com/photos/31141291/pexels-photo-31141291/free-photo-of-classic-indian-chai-on-wooden-table.jpeg?auto=compress&cs=tinysrgb&w=600",
        width=200,
    )
    result2 = st.button("Chai")
    if result2:
        st.success("You love Chai")

sidebar_name = st.sidebar.text_input("Enter NAME")
if sidebar_name:
    st.write(f"{sidebar_name} ")
