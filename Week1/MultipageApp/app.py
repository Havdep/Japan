import streamlit as st

about_page = st.Page(
    page="views/about_me.py",
    title="ABOUT 私",
    icon=":material/person_add:",
    default=True,
)
projtect_1_page = st.Page(
    page="views/sales_dashboard.py",
    title="セールス Dashboard",
    icon=":material/campaign:",
)
projtect_2_page = st.Page(
    page="views/chat_bot.py",
    title="CHAT BOT",
    icon=":material/smart_toy:",
)

pg = st.navigation(
    {"Info": [about_page], "Projects": [projtect_1_page, projtect_2_page]}
)

st.logo("assets/images.png", size="medium")
st.sidebar.text("Made with Love")

pg.run()
