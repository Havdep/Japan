import streamlit as st
import pandas as pd
import pdfplumber
import time
import io
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()
client = OpenAI()

# st.header("Chai Data")
st.title("PDF → GPT → Sheets + History")
file = st.file_uploader("Upload File", type=["csv", "pdf"])
print(f"file: {file}")

if file:
    try:
        with pdfplumber.open(file) as pdf:
            st.success("PDF opened successfully!")
            all_text = ""  # Store all text here
            for page_num, page in enumerate(pdf.pages):
                st.write(f"\n--- Content from Page {page_num + 1} ---")
                text = page.extract_text()
                st.write(text)

                if text:
                    all_text += text + "\n"
                else:
                    st.warning(f"No text found on Page {page_num + 1}.")

            st.write("✅ All pages processed")
            # response = client.chat.completions.create(
            #     model="gpt-4.1-nano-2025-04-14",
            #     messages=[
            #         {
            #             "role": "user",
            #             "content": f"Summarize the {all_text} of PDF in 5 lines",
            #         }
            #     ],
            # )
            # st.write("for loop end and restarts")

            # else:
            #     print(f"No text found on Page {page_num + 1}.")
            # st.success(f"Open AI response is: {response.choices[0].message.content}")
    except Exception as e:
        st.error(f"Error processing PDF: {e}")
        st.info("Please ensure the uploaded file is a valid PDF.")
