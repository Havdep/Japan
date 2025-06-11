import streamlit as st

project_page_1 = st.Page(
    page="Pages/about_me.py",
    title="Information",
    icon=":material/campaign:",
    default=True,
)
project_page_2 = st.Page(
    page="Pages/Resume_Screening.py",
    title="Resume Screneer",
    icon=":material/campaign:",
)
pg = st.navigation({"Info": [project_page_1], "Screening": [project_page_2]})

st.sidebar.text("Made in Shinjuku")

pg.run()
