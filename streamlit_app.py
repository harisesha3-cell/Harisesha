import streamlit as st

# Page Title
st.set_page_config(page_title="Brownny Billing system", page_icon="🧾", layout="centered")

st.title("💼 Company Billing Portal")

# Simple Login System
password = st.text_input("Enter Password to Login:", type="password")

# Password
CORRECT_PASSWORD = "Brownny@2509"

if password == CORRECT_PASSWORD:
    st.success("Login Successful! Welcome.")
    
    st.divider()
    st.header("Enter Bill Details")
    
    # Inputs from user
    customer_name = st.text_input("Customer Name")
    item_name = st.text_input("Product / Item Name")
    qty = st.number_input("Quantity", min_value=1, value=1)
    price = st.number_input("Price per Unit (Rs.)", min_value=0.0, value=100.0)
    
    # Backend Logic 
    if st.button("Generate Bill"):
        total_amount = qty * price
        
        st.divider()
        # Bill Format Output
        st.markdown("### 🧾 INVOICE / BILL")
        st.write(f"**Customer Name:** {customer_name}")
        st.write(f"**Item Purchased:** {item_name}")
        st.write(f"**Quantity:** {qty}")
        st.write(f"**Unit Price:** Rs. {price}")
        st.markdown("---")
        st.subheader(f"Total Amount: Rs. {total_amount}")
        st.markdown("---")
        st.info("Thank you for your business!")

elif password != "":
    st.error("Incorrect Password! Please try again.")
