import streamlit as st

# --- Landing Page Content ---
st.title("🚀 Welcome to Your Resume Screening Solution!")
st.markdown("## *Transforming recruitment with intelligent insights.*")

st.markdown("---")

st.write(
    """
    This platform helps you efficiently screen resumes, identify top candidates,
    and streamline your hiring process. Leverage powerful tools to quickly analyze
    resumes and focus on what truly matters.
"""
)

st.write(
    """
    Whether you're a recruiter, HR professional, or hiring manager, our intuitive
    interface provides the features you need to make informed decisions faster.
"""
)

# The "Get Started" button will appear, and Streamlit's multi-page navigation
# in the sidebar will handle the routing to 'Resume_Screening.py'.
st.markdown("---")

st.write("Ready to begin screening resumes?")
# No explicit button action needed to change route; sidebar handles it.
# However, you can add a button for aesthetic or direct link if needed:
# For direct navigation, you would typically use `st.switch_page("pages/Resume_Screening.py")`
# but for simplicity and letting Streamlit's sidebar handle it, we'll just have the user see the sidebar.
# If you REALLY want a button to switch pages, uncomment the below and ensure Streamlit version supports it.
# if st.button("GET STARTED"):
#     st.switch_page("pages/Resume_Screening") # Requires Streamlit >= 1.28

st.info(
    "Navigate to the 'Resume Screening Dashboard' page in the sidebar to get started!"
)

st.markdown(
    """
<p style='text-align: center; color: gray; margin-top: 3rem;'>
    Powered in Shinjuku | © 2025 Nipun APEX
</p>
""",
    unsafe_allow_html=True,
)
