from ....dimensions.core import Dimensions as ObjectTPL
from ....math.ring_volume_weight import ring_volume_weight


class RingComponent(ObjectTPL):
    names = ['diameter', 'inner_diameter', 'height']

    def __init__(self, mould, dimensions: dict = None):
        super().__init__(dimensions)
        from ..core import Mould
        self._mould: Mould = mould

    @property
    def mould(self):
        return self._mould

    @property
    def tyre(self):
        return self.mould.tyre

    @property
    def diameter(self):
        return self['diameter']

    @diameter.setter
    def diameter(self, dim: float | int = None):
        self['diameter'] = dim

    @property
    def inner_diameter(self):
        return self['inner_diameter']

    @inner_diameter.setter
    def inner_diameter(self, dim: float | int = None):
        self['inner_diameter'] = dim

    @property
    def height(self):
        return self['height']

    @height.setter
    def height(self, dim: float | int = None):
        self['height'] = dim

    def weight(self, margin: float = 0, density: float = 1):
        inner_diameter = self.inner_diameter if self.inner_diameter > 2 * margin else self.inner_diameter - 2 * margin
        wt = ring_volume_weight(self.diameter + 2 * margin, self.height + 2 * margin, inner_diameter)
        return wt * density / 1000000
