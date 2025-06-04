from numpy import size
import streamlit as st
from forms.contact_forms import contact_form


@st.dialog("Fill your Details")
def show_contact_form():
    contact_form()


st.title("私について")

col1, col2 = st.columns(2, gap="medium", vertical_alignment="center")


with col1:
    st.image(
        "https://github.com/Havdep/Japan/blob/main/Week1/MultipageApp/assets/WIN_20210515_23_58_42_Pro.jpg?raw=true",
        width=300,
    )


with col2:
    st.title("Nipun KUMAR")
    st.write(
        "Associate Software Enginner working in TOKYO. Actively looking for job opportunies in the AI space"
    )
    if st.button("ご連絡"):
        show_contact_form()

# --- Professional Experience ---
st.header("Professional Experience")

st.subheader("🔹 Accenture Japan — Associate Software Engineer")
st.caption("Nov 2024 – Present | Tokyo, Japan")
st.write(
    """
    - Worked with cross-functional teams on enterprise-level backend systems for a major Japanese client (Toshiba).
    - Gained experience working directly at the client site in Japan, adapting to local business practices and expectations.
    - Transferred from Accenture India to Accenture Japan under global assignment.
    - Gained hands-on experience in Japanese work culture and communication.
    """
)
st.subheader("🔹 Accenture India — Associate Software Engineer")
st.caption("Feb 2024 – Nov 2024 | Bangalore, India")
st.write(
    """
    - Developed scalable PL/SQL data pipelines and contributed to mission-critical systems for Toshiba.
    - Supported Japanese client operations and led integration testing during monthly releases.
    - Received formal training in **SAP MM (Material Management)** modules.
    """
)

st.subheader("🔹 React Developer Intern — Remote")
st.caption("Nov 2024 – Present | Delhi, India")
st.write(
    """
    - Built responsive UI components using React.js for a startup dashboard product.
    - Integrated REST APIs and improved performance by optimizing state management.
    """
)

# --- Skills ---
st.header("Skills")

skills = [
    "⚙️ Python (Streamlit, FastAPI, pandas)",
    "🧠 AI Tools (OpenAI API, Prompt Engineering)",
    "🌐 Web Development (React.Js, HTML, CSS)",
    "🗃️ PL/SQL & Database Design",
    "🧪 Software Testing & Debugging",
    "🧭 Japanese Communication (Business Level - JLPT N3)",
]

for skill in skills:
    st.write(skill)
