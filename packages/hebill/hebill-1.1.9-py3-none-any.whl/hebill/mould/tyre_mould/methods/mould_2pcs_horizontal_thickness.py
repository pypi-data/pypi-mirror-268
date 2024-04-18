from ..constants import MOULD_2PCS_MIN_HOR_TK, MOULD_2PCS_HOR_TK_POWER_RATE
from ....tyre import Tyre


def mould_2pcs_horizontal_thickness(tyre: Tyre):
    tk = pow(tyre.diameter * tyre.diameter * tyre.section_width, MOULD_2PCS_HOR_TK_POWER_RATE)
    if tk < MOULD_2PCS_MIN_HOR_TK:
        return MOULD_2PCS_MIN_HOR_TK
    return round(tk, 0)
