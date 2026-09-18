import streamlit as st

# Page Title
st.set_page_config(page_title="Propose parcel", page_icon="🧾", layout="centered")

st.title("❤ My personal property")

# Simple Login System
password = st.text_input("Enter Password to Login:", type="password")

# Password
CORRECT_PASSWORD = "Hari@2509"

if password == CORRECT_PASSWORD:
    st.success("Login Successful! Welcome my heart.")
    
    st.divider()
    st.header("Enter personal details Details")
    
    # Inputs from user
    My_heart_owner_name = st.text_input("Owner Name")
    Missing_notes = st.text_input("Missing notes")
    Missing_qty_of_hearts = st.number_input("Heart count", min_value=1, value=1)
    
    # Backend Logic 
    if st.button("Generate Bill"):
        
        st.divider()
        # Bill Format Output
        st.markdown("### 🧾 Notes")
        # Inga variable name-ah correct panniruken
        st.write(f"**Owner Name:** {My_heart_owner_name}")
        st.write(f"**Missing notes:** {Missing_notes}")
        st.write(f"**Heart count:** {Missing_qty_of_hearts}")
        st.markdown("---")
        st.info("I Love U!❤")

elif password != "":
    st.error("Incorrect Password! Please try again.")
