import streamlit as st
import fitz
import io
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

client = OpenAI()

# --- Main Application Layout ---
# Header Section
st.title("✨ **AI Resume Screener** ✨")
st.write("---")
st.markdown(
    "##### *Streamlining your recruitment process with intelligent resume analysis.*"
)

# Resume Upload Section
st.header("Upload Candidate Resume(s) 📤")
st.write("Please upload the resume files (PDF, DOCX) below.")

uploaded_file = st.file_uploader(
    "Choose a file", type=["pdf", "docx"], accept_multiple_files=False
)

if uploaded_file is not None:
    file_details = {
        "filename": uploaded_file.name,
        "filetype": uploaded_file.type,
        "filesize": uploaded_file.size,
    }
    st.success(f"**Successfully uploaded:** `{file_details['filename']}`")
    st.info(
        f"File Type: `{file_details['filetype']}` | Size: `{round(file_details['filesize'] / 1024, 2)} KB`"
    )

    # You would typically process the file here
    if uploaded_file.type == "application/pdf":
        # Read file into bytes
        pdf_bytes = uploaded_file.read()

        # Open with PyMuPDF
        doc = fitz.open(stream=pdf_bytes, filetype="pdf")

        text = ""
        for page in doc:
            text += page.get_text()

        # st.subheader("Extracted Resume Text")
        # st.text_area("Resume Content", text, height=400)

    # For now, just a placeholder message
    st.markdown("---")
    st.write("File ready for processing! (Future: AI analysis will happen here)")
else:
    st.info("No file uploaded yet. Please select a resume.")

# print(uploaded_file)
st.markdown("---")

# --- Original App Functionality (Integrated with improved styling) ---
st.header("Basic Interaction Demo 📝")
user_name = st.text_input(
    "Enter your name:",
)
job_description = st.text_input("Enter the Job Description:")
if user_name:
    st.write(f"Hello there, **{user_name}**!")
else:
    st.write("Hello there")

if uploaded_file and job_description and user_name and st.button("Initiate Process"):
    st.success(f"Process initiated for {user_name}! Stay tuned for updates.")

    # Now send text data to OpenAI and get response
    response = client.chat.completions.create(
        model="gpt-4.1-nano-2025-04-14",
        messages=[
            {
                "role": "user",
                "content": f"""
Analyze this resume vs. job description. Perform a rigorous, highly accurate fit analysis. Apply deep reasoning to evaluate candidate suitability.

Resume:
{text}

Job Description:
{job_description}

Return the result in the following format:

Summary: <brief analysis>
Score: <score out of 100>
Verdict: <Yes / No / Maybe>
Notes: <specific reasons for verdict>
""",
            }
        ],
    )

    # Extract the response text
    evaluation = response.choices[0].message.content
    print(evaluation)
    print(response)
    st.subheader("AI analysis")
    st.text_area("Evaluation", evaluation)
    if evaluation:  # Only show the download button if evaluation has content
        st.download_button(
            label="Download Report",
            data=evaluation,
            file_name="report.txt",
            mime="text/txt",
            icon=":material/download:",
        )
    else:
        st.text("No Report generated. Try Again")
else:
    if not uploaded_file:
        st.warning("Please upload a resume.")
    if not job_description:
        st.warning("Please enter a job description.")
    if not user_name:
        st.warning("Please enter your name.")

st.markdown("---")
# Footer
st.markdown(
    """
<p style='text-align: center; color: gray;'>
    Handcrafted in Shinjuku!
</p>
""",
    unsafe_allow_html=True,
)
