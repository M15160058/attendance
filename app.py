import streamlit as st
import gspread
from google.oauth2.service_account import Credentials
from datetime import datetime

# -------------------
# PAGE HEADER
# -------------------
st.title("Event Attendance Form")

st.markdown("""
Developed by **Arif Hossin**  
[LinkedIn](https://www.linkedin.com/in/arif-hossin-7ab23952/) | [GitHub](https://github.com/M15160058)
""")

# -------------------
# GOOGLE SHEETS CONNECTION
# -------------------
scope = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive"
]

creds_dict = st.secrets["gcp_service_account"]
creds = Credentials.from_service_account_info(creds_dict, scopes=scope)
client = gspread.authorize(creds)

sheet = client.open("Event Attendance").sheet1


# -------------------
# FORM
# -------------------
with st.form("attendance_form"):

    name = st.text_input("Name")
    email = st.text_input("Email")
    speaker = st.text_input("Speaker Name")
    question = st.text_area("Your Question")

    submitted = st.form_submit_button("Submit")

    if submitted:

        if name and email:
            sheet.append_row([
                datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                name,
                email,
                speaker,
                question
            ])

            st.success("✅ Attendance recorded successfully!")
        else:
            st.error("Please enter Name and Email.")
