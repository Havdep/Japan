import streamlit as st

st.title("Chai Maker App")


sugar_qty = st.slider("Sugar Level", 0, 5, 2)
if sugar_qty:
    st.write(f"Sugar level selected is {sugar_qty}")

if st.button("Chai"):
    st.success("Your Chai is being brewed")

cups = st.number_input("How many cups", min_value=1, max_value=5, step=1)
st.write(f"Cups are {cups}")

dob = st.date_input("Select your DOB is:")
st.write(f"Your DoB is {dob}")
