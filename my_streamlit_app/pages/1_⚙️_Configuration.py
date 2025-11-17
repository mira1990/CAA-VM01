# configurations.py
"""
Module contenant les référentiels techniques.
Tu peux modifier ces listes ici si besoin.
"""

# Référentiel : Lst_BO_PTF
DEFAULT_LST_BO_PTF = ["05", "08", "18"]

# Référentiel : Lst_Pdt_Gar_EU
DEFAULT_LST_PDT_GAR_EU = [
    "HGICP1", "HGPAG1", "HGPCP1", "HGFPEL2", "HGPFL1", "HGPFP1",
    "UCIX 1",
    "UCPEP1", "UCPEP2", "UCPEP3", "UCPEP4", "UCPEP5", "UCPEP6", "UCPEP7",
    "UCDEC1", "UCMIN1", "UCTOP1", "UCSOL1", "UCMAD1",
]


def get_default_lst_bo_ptf():
    """Retourne une copie de la liste Lst_BO_PTF."""
    return DEFAULT_LST_BO_PTF.copy()


def get_default_lst_pdt_gar_eu():
    """Retourne une copie de la liste Lst_Pdt_Gar_EU."""
    return DEFAULT_LST_PDT_GAR_EU.copy()
