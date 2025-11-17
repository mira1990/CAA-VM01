# configurations.py

DEFAULT_LST_BO_PTF = ["05", "08", "18"]

DEFAULT_LST_PDT_GAR_EU = [
    "HGICP1", "HGPAG1", "HGPCP1", "HGFPEL2", "HGPFL1", "HGPFP1",
    "UCIX 1",
    "UCPEP1", "UCPEP2", "UCPEP3", "UCPEP4", "UCPEP5", "UCPEP6", "UCPEP7",
    "UCDEC1", "UCMIN1", "UCTOP1", "UCSOL1", "UCMAD1"
]


def get_default_lst_bo_ptf():
    return DEFAULT_LST_BO_PTF.copy()


def get_default_lst_pdt_gar_eu():
    return DEFAULT_LST_PDT_GAR_EU.copy()
