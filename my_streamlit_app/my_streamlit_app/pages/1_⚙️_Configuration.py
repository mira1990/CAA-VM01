import streamlit as st

st.title("⚙️ Référentiel technique")

st.write("Modification de la configuration du référentiel technique.")
param = st.text_input("Paramètres", "Valeur")

if st.button("Save"):
    st.success("Saved!")
