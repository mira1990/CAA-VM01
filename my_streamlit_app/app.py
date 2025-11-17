import streamlit as st
import pandas as pd

from configurations import (
    get_default_lst_bo_ptf,
    get_default_lst_pdt_gar_eu,
)

st.set_page_config(page_title="Vue Métier / Référentiel technique")

# ------------------------------------------------------------------
# Initialisation des référentiels en session
# ------------------------------------------------------------------
if "Lst_BO_PTF" not in st.session_state:
    st.session_state.Lst_BO_PTF = get_default_lst_bo_ptf()

if "Lst_Pdt_Gar_EU" not in st.session_state:
    st.session_state.Lst_Pdt_Gar_EU = get_default_lst_pdt_gar_eu()

# Variable pour stocker le DataFrame de résultats
if "df" not in st.session_state:
    st.session_state.df = None

# ------------------------------------------------------------------
# Onglets
# ------------------------------------------------------------------
tab_metier, tab_tech = st.tabs(["👁️ Vue métier", "⚙️ Référentiel technique"])

# ==================================================================
# ONGLET 1 : VUE MÉTIER  → inputs
# ==================================================================
with tab_metier:
    st.title("Vue Métier")

    annee_choisie = st.number_input("annee_choisie", 1990, 2100, 2026)
    AnneeBE = st.number_input("AnneeBE", 1990, 2100, 2026)
    AnneePGP = st.number_input("AnneePGP", 1990, 2100, 2026)
    debut_periode = st.text_input("debut_periode", "202601")
    fin_periode = st.text_input("fin_periode", "202612")
    Mois_choisi = st.number_input("Mois_choisi", 1, 12, 1)

    st.markdown("---")

    if st.button("Générer les résultats"):
        st.session_state.df = pd.DataFrame({
            "annee_choisie": [annee_choisie],
            "AnneeBE": [AnneeBE],
            "AnneePGP": [AnneePGP],
            "debut_periode": [debut_periode],
            "fin_periode": [fin_periode],
            "Mois_choisi": [Mois_choisi],
        })
        st.success("Résultats générés !")

    if st.session_state.df is not None:
        csv = st.session_state.df.to_csv(index=False)
        st.download_button(
            label="Télécharger le fichier CSV",
            data=csv,
            file_name="output.csv",
            mime="text/csv",
        )

# ==================================================================
# ONGLET 2 : RÉFÉRENTIEL TECHNIQUE
# ==================================================================
with tab_tech:
    st.title("⚙️ Référentiel technique")

    lst_bo_ptf_text = st.text_area(
        "Lst_BO_PTF (séparer par des virgules)",
        value=", ".join(st.session_state.Lst_BO_PTF),
    )

    lst_pdt_gar_eu_text = st.text_area(
        "Lst_Pdt_Gar_EU (séparer par des virgules)",
        value=", ".join(st.session_state.Lst_Pdt_Gar_EU),
        height=160,
    )

    if st.button("💾 Enregistrer le référentiel"):
        st.session_state.Lst_BO_PTF = [
            x.strip() for x in lst_bo_ptf_text.split(",") if x.strip()
        ]
        st.session_state.Lst_Pdt_Gar_EU = [
            x.strip() for x in lst_pdt_gar_eu_text.split(",") if x.strip()
        ]
        st.success("Référentiel mis à jour (en mémoire).")

    with st.expander("Voir les valeurs actuelles"):
        st.write("Lst_BO_PTF :", st.session_state.Lst_BO_PTF)
        st.write("Lst_Pdt_Gar_EU :", st.session_state.Lst_Pdt_Gar_EU)
