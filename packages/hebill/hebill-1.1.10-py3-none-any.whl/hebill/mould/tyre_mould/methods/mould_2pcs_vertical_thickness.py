from ..constants import MOULD_2PCS_MIN_VER_TK, MOULD_2PCS_VER_TK_POWER_RATE
from ....tyre import Tyre


def mould_2pcs_vertical_thickness(tyre: Tyre):
    tk = pow(tyre.diameter * tyre.diameter * tyre.section_width, MOULD_2PCS_VER_TK_POWER_RATE)
    if tk < MOULD_2PCS_MIN_VER_TK:
        return MOULD_2PCS_MIN_VER_TK
    return round(tk, 0)
