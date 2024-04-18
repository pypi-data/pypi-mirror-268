from ..constants import MOULD_INNER_DIAMETER_TO_RIM_DIAMETER
from ..methods.mould_2pcs_horizontal_thickness import mould_2pcs_horizontal_thickness
from ..methods.mould_2pcs_vertical_thickness import mould_2pcs_vertical_thickness
from ....dimensions.core import Dimensions as ObjectTPL
from ..core import Mould
from ....math.ring_volume_weight import ring_volume_weight


class Mould2PsHalf(ObjectTPL):
    names = [
        'diameter',
        'height',
        'inner_diameter',
        'cavity_depth'
        ]

    def __init__(self, mould: Mould, dimensions: dict = None, is_primary: bool = False):
        super().__init__(dimensions)
        self._mould = mould
        self._primary_obj = None
        self._is_primary = is_primary
        if self.diameter is None:
            self.diameter = self.tyre.diameter + mould_2pcs_horizontal_thickness(self.tyre) * 2
        if self.inner_diameter is None:
            self.inner_diameter = self.tyre.rim_diameter * MOULD_INNER_DIAMETER_TO_RIM_DIAMETER
        if self.height is None:
            self.height = self.tyre.section_width / 2 + mould_2pcs_vertical_thickness(self.tyre)
        if self.cavity_depth is None:
            self.cavity_depth = self.tyre.section_width / 2

    def _primary(self) -> ObjectTPL:
        if self._primary_obj is None:
            self._primary_obj = Mould2PsHalf(self.mould, {
                'diameter': self.tyre.primary.diameter + mould_2pcs_horizontal_thickness(self.tyre.primary) * 2,
                'inner_diameter': self.tyre.primary.rim_diameter * MOULD_INNER_DIAMETER_TO_RIM_DIAMETER,
                'height': self.tyre.primary.section_width / 2 + mould_2pcs_vertical_thickness(self.tyre.primary),
                'cavity_depth': self.tyre.primary.section_width / 2
            }, True)
        return self._primary_obj

    @property
    def mould(self) -> Mould:
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

    @property
    def cavity_depth(self):
        return self['cavity_depth']

    @cavity_depth.setter
    def cavity_depth(self, dim: float | int = None):
        self['cavity_depth'] = dim

    def weight(self, margin: float = 0, density: float = 1):
        out_diameter = self.diameter
        height = self.height
        inner_diameter = self.inner_diameter
        wt = ring_volume_weight(out_diameter, height, inner_diameter, margin, density)
        if self._is_primary:
            out_diameter = self.tyre.primary.diameter - 2 * self.tyre.primary.non_skid_depth
            height = self.cavity_depth
            inner_diameter = self.inner_diameter
        else:
            out_diameter = self.tyre.diameter - 2 * self.tyre.non_skid_depth
            height = self.cavity_depth
            inner_diameter = self.inner_diameter
        wt -= ring_volume_weight(out_diameter, height, inner_diameter, margin, density)
        return wt * density

    @property
    def dimensions(self):
        return {
            'diameter': self.diameter,
            'height': self.height,
            'inner_diameter': self.inner_diameter,
            'cavity_depth': self.cavity_depth,
            'vertical_thickness': self.vertical_thickness,
            'horizontal_thickness': self.horizontal_thickness,
        }

    @property
    def dimensions_formatted(self):
        dimensions = self.dimensions
        for k, v in dimensions.items():
            if isinstance(v, float) and len(str(v).split('.')[1]) > 2:
                dimensions[k] = round(v, 2)
        return dimensions

    @property
    def vertical_thickness(self):
        return self.height - self.cavity_depth

    @property
    def horizontal_thickness(self):
        return (self.diameter - self.tyre.diameter) / 2
