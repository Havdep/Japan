import streamlit as st
import re  # for email validation
import requests


def contact_form():
    with st.form("Contact Form"):
        first = st.text_input("First Name")
        last = st.text_input("Last Name")
        email = st.text_input("Email")
        msg = st.text_area("Message")
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
            if not msg.strip():
                errors.append("Message cannot be empty.")

            # Show result
            if errors:
                for err in errors:
                    st.error(err)
            else:
                st.success("Thanks! Your message has been received.")
                # You can add email-sending logic here
                data = {
                    "first": first,
                    "last": last,
                    "email": email,
                    "msg": msg,
                }
                response = requests.post(
                    "https://connect.pabbly.com/workflow/sendwebhookdata/IjU3NjYwNTZiMDYzNDA0MzU1MjZkNTUzNDUxMzAi_pc",
                    json=data,
                )

                if response.status_code == 200:
                    print("✅ Webhook delivered successfully!")
                else:
                    print("❌ Failed:", response.status_code, response.text)
