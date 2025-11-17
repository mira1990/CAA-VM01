import streamlit as st
import pandas as pd

st.title("Data Processing App")

year = st.number_input("Enter year", min_value=2000, max_value=2100, value=2024)
month = st.number_input("Enter month", min_value=1, max_value=12, value=1)

if st.button("Generate CSV"):
    df = pd.DataFrame({
        "year": [year],
        "month": [month],
        "value": [42]
    })
    df.to_csv("output.csv", index=False)
    st.success("CSV generated!")
