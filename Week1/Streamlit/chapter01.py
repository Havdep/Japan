import streamlit as st

st.title("Hello Chai app")
st.subheader("Brewed with StreamLit")
st.badge("This ia a badge in stramlit")
st.write ("Choose your favourite sex position:")
position = st.selectbox("Your fav position:",["Doggy","Missionary","Cowgirl","Sixty-Nine"])

st.write(f"You chose {position}, EXCELLENT choice")
st.success("Your position has been recorded!😈")