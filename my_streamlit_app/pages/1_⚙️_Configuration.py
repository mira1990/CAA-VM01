import streamlit as st

st.title("⚙️ Configuration")

st.write("Modify application settings here.")
param = st.text_input("Parameter", "default_value")

if st.button("Save"):
    st.success("Saved!")
