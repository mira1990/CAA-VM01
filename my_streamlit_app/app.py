# app.py
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

    # ---- Inputs métier ----
    annee_choisie = st.number_input(
        "annee_choisie",
        min_value=1990,
        max_value=2100,
        value=2026,
    )

    AnneeBE = st.number_input(
        "AnneeBE",
        min_value=1990,
        max_value=2100,
        value=2026,
    )

    AnneePGP = st.number_input(
        "AnneePGP",
        min_value=1990,
        max_value=2100,
        value=2026,
    )

    debut_periode = st.text_input(
        "debut_periode (ex : 202601)",
        value="202601",
    )

    fin_periode = st.text_input(
        "fin_periode (ex : 202612)",
        value="202612",
    )

    Mois_choisi = st.number_input(
        "Mois_choisi",
        min_value=1,
        max_value=12,
        value=1,
    )

    st.markdown("---")

    # -------------------------
    # Bouton : Générer résultats
    # -------------------------
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

    # -------------------------
    # Bouton : Télécharger
    # -------------------------
    if st.session_state.df is not None:
        csv = st.session_state.df.to_csv(index=False)
        st.download_button(
            label="Télécharger le fichier CSV",
            data=csv,
            file_name="output.csv",
            mime="text/csv",
        )

# ==================================================================
# ONGLET 2 : RÉFÉRENTIEL TECHNIQUE  → Lst_BO_PTF & Lst_Pdt_Gar_EU
# ==================================================================
with tab_tech:
    st.title("⚙️ Référentiel technique")
    st.write("Configuration des listes de paramètres techniques.")

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
        # Mise à jour des listes en session à partir du texte saisi
        st.session_state.Lst_BO_PTF = [
            x.strip() for x in lst_bo_ptf_text.split(",") if x.strip()
        ]
        st.session_state.Lst_Pdt_Gar_EU = [
            x.strip() for x in lst_pdt_gar_eu_text.split(",") if x.strip()
        ]
        st.success("Référentiel technique mis à jour (en mémoire).")

    with st.expander("Voir les listes actuelles"):
        st.write("**Lst_BO_PTF :**", st.session_state.Lst_BO_PTF)
        st.write("**Lst_Pdt_Gar_EU :**", st.session_state.Lst_Pdt_Gar_EU)
