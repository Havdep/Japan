import streamlit as st
import re  # for email validation
import requests
from openai import OpenAI
from dotenv import load_dotenv  # for accessing API key

load_dotenv()
client = OpenAI()


def contact_form():
    with st.form("Contact Form"):
        first = st.text_input("First Name")
        last = st.text_input("Last Name")
        email = st.text_input("Email")
        query = st.text_area("Enter your Query")
        submitted = st.form_submit_button("提出")  # "Submit" in Japanese

        if submitted:
            errors = []

            # Check first name
            if not first.strip():
                errors.append("First name is required.")

            # Check last name
            if not last.strip():
                errors.append("Last name is required.")

            # Check valid email
            email_regex = r"^[\w\.-]+@[\w\.-]+\.\w+$"
            if not email.strip():
                errors.append("Email is required.")
            elif not re.match(email_regex, email):
                errors.append("Please enter a valid email address.")

            # Check message
            if not query.strip():
                errors.append("Query cannot be empty.")

            # Show result
            if errors:
                for err in errors:
                    st.error(err)
            else:
                st.success("Thanks! Your message has been received.")
                # You can add email-sending logic here
                form_data = f"""
                User Submission:
                Name: {first} {last}
                Email: {email}
                Query: {query}
                """
                response_1 = client.chat.completions.create(
                    model="gpt-4.1-nano-2025-04-14",
                    messages=[
                        {
                            "role": "user",
                            "content": f"Summarize the following user inquiry in 2–3 sentences as if you're writing a support ticket or CRM note:\n\n{form_data}",
                        }
                    ],
                )
                webhook_data = {
                    "first": first,
                    "last": last,
                    "email": email,
                    "gpt_response": response_1.choices[0].message.content,
                }
                if response_1:
                    response_2 = requests.post(
                        "https://connect.pabbly.com/workflow/sendwebhookdata/IjU3NjYwNTZiMDYzNDA0MzU1MjZkNTUzNDUxMzAi_pc",
                        json=webhook_data,
                    )
                else:
                    st.error("Failed to get response from AI. Try again")

                if response_2.status_code == 200:
                    print("✅ Webhook delivered successfully!")
                else:
                    print("❌ Failed:", response_2.status_code, response_2.text)
