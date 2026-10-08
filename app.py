import streamlit as st
import re
from datetime import datetime
from PIL import Image
import pytesseract


def mt_to_kg(mt_value):
    """
    Convert Metric Ton (MT) to Kilogram (kg)
    1 MT = 1000 kg
    """
    try:
        mt = float(mt_value)
        kg = mt * 1000
        return kg
    except (ValueError, TypeError):
        return None


def add_to_history(source, mt_value, kg_value):
    st.session_state.history.insert(0, {
        "Time": datetime.now().strftime("%d-%m-%Y %H:%M:%S"),
        "Source": source,
        "MT": mt_value,
        "KG": f"{kg_value:,.2f}",
    })


# ---------- Page Setup ----------
st.set_page_config(page_title="MT to KG Converter", page_icon="⚖️")
st.title("⚖️ MT to KG Converter")

if "history" not in st.session_state:
    st.session_state.history = []

tab1, tab2 = st.tabs(["⌨️ Manual Entry", "🖼️ Image Upload (OCR)"])

# ---------- Tab 1: Manual Entry ----------
with tab1:
    st.write("Metric Ton (MT) value ah Kilogram (kg) ah convert pannunga.")
    value = st.text_input("Enter value in MT (e.g. 1, 2, 0.5, 0.6):")

    if value:
        result = mt_to_kg(value)
        if result is None:
            st.error("Invalid input! Please enter a number.")
        else:
            st.success(f"{value} MT = {result:,.2f} kg")
            add_to_history("Manual", value, result)

    st.divider()
    st.caption("Quick examples")
    examples = [1, 2, 0.5, 0.6, 1.5]
    cols = st.columns(len(examples))
    for col, ex in zip(cols, examples):
        col.metric(f"{ex} MT", f"{mt_to_kg(ex):,.0f} kg")

# ---------- Tab 2: Image Upload (OCR) ----------
with tab2:
    st.write("MT value irukkura image upload pannunga - automatic ah detect panni convert pannidum.")
    uploaded_file = st.file_uploader("Choose an image", type=["png", "jpg", "jpeg"])

    if uploaded_file is not None:
        image = Image.open(uploaded_file)
        st.image(image, caption="Uploaded Image", use_container_width=True)

        with st.spinner("Reading image..."):
            extracted_text = pytesseract.image_to_string(image)

        st.text_area("Extracted text (OCR output)", extracted_text, height=100)

        # Find all numbers in the extracted text
        numbers = re.findall(r"\d+\.?\d*", extracted_text)

        if numbers:
            st.write("Detected number(s):")
            selected = st.selectbox("Confirm the MT value to convert:", numbers)
            if st.button("Convert selected value"):
                result = mt_to_kg(selected)
                st.success(f"{selected} MT = {result:,.2f} kg")
                add_to_history(uploaded_file.name, selected, result)
        else:
            st.warning("Image la irundhu number edhuvum detect aagala. Clear ah eduthu try pannunga.")

# ---------- History ----------
st.divider()
st.subheader("📜 History")

if st.session_state.history:
    st.dataframe(st.session_state.history, use_container_width=True, hide_index=True)
    if st.button("🗑️ Clear History"):
        st.session_state.history = []
        st.rerun()
else:
    st.caption("Innum edhum convert pannala.")
