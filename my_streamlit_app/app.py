import streamlit as st
import pandas as pd
from io import StringIO

st.title("Vue Metier")

year = st.number_input("Saisir l'année", min_value=1990, max_value=2100, value=2026)
month = st.number_input("Saisir le mois", min_value=1, max_value=12, value=1)

# Variable pour stocker le DataFrame
if "df" not in st.session_state:
    st.session_state.df = None

# -------------------------
# Bouton : Générer résultats
# -------------------------
if st.button("Générer les résultats"):
    st.session_state.df = pd.DataFrame({
        "year": [year],
        "month": [month],
        "value": [42]
    })
    st.success("Résultats générés !")

# -------------------------
# Bouton : Télécharger
# -------------------------
if st.session_state.df is not None:
    # Conversion en CSV dans un buffer mémoire
    csv = st.session_state.df.to_csv(index=False)
    
    st.download_button(
        label="Télécharger le fichier CSV",
        data=csv,
        file_name="output.csv",
        mime="text/csv"
    )
