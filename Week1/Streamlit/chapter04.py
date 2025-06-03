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
st.title("Resume Translator AI")
file = st.file_uploader("Upload File", type=["csv", "pdf"])
print(f"file: {file}")

st.subheader("Choose Language")
tar_lang = st.selectbox("", ["Japanese", "French", "German", "Russian"])

if file:
    try:
        with pdfplumber.open(file) as pdf:
            st.success("PDF opened successfully!")
            for page_num, page in enumerate(pdf.pages):
                st.write(f"\n--- Content from Page {page_num + 1} ---")
                text = page.extract_text()

                if text:
                    lines = text.strip().split()
                    first_four_lines = lines[:17]
                    result = "\n".join(first_four_lines)
                    st.write(result)
                    response = client.chat.completions.create(
                        model="gpt-4.1-nano-2025-04-14",
                        messages=[
                            {
                                "role": "user",
                                "content": f"Translate in {tar_lang}: {result}",
                            }
                        ],
                    )
                    st.write("Sending Data to OpenAI")
                    st.success(
                        f"Open AI response is: {response.choices[0].message.content}"
                    )
                else:
                    print(f"No text found on Page {page_num + 1}.")

    except Exception as e:
        st.error(f"Error processing PDF: {e}")
        st.info("Please ensure the uploaded file is a valid PDF.")


# if file:
#     df = pd.read_csv(file)
#     print(df)
#     st.subheader(f"File: {file.name}")
#     st.dataframe(df)
#     st.write(f"The file size is {file.size / 1024:.2f} KB")

# if file:
# cities = df["City"].unique()
# selected_city = st.selectbox("Filter data by city", cities)
# filtered_city = df[df["City"] == selected_city]
# st.dataframe(filtered_city)
