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
    Missing_name = st.text_input("Missing name")
    qty = st.number_input("Quantity", min_value=1, value=1)
    
    # Backend Logic 
    if st.button("Generate Bill"):
        
        st.divider()
        # Bill Format Output
        st.markdown("### 🧾 Notes")
        # Inga variable name-ah correct panniruken
        st.write(f"**Owner Name:** {My_heart_owner_name}")
        st.write(f"**Missing name:** {Missing_name}")
        st.write(f"**Quantity:** {qty}")
        st.markdown("---")
        st.info("I Love U!❤")

elif password != "":
    st.error("Incorrect Password! Please try again.")
