from ...features.mould_2ps_half import Mould2PsHalf


class Mould2PsHalfLower(Mould2PsHalf):
    @property
    def primary(self):
        return self._primary()
