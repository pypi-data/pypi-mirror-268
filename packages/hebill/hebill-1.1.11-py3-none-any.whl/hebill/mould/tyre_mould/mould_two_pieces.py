from .core import Mould
from ...tyre import Tyre
from .components.mould_2ps_half_upper.core import Mould2PsHalfUpper
from .components.mould_2ps_half_lower.core import Mould2PsHalfLower


class Mould2PS(Mould):
    def __init__(self, tyre: Tyre, dimensions: dict = None):
        """
        :param tyre:
        :param dimensions: {
            'diameter': float | None
            'height': float | None
            'upper_height': float | None
            'upper_cavity_depth': float | None
            'upper_inner_diameter': float | None
            'lower_inner_diameter': float | None
        }
        """
        super().__init__(tyre)
        self._upper_moulds = []
        self._lower_moulds = []
        upper_dims = {}
        lower_dims = {}
        if dimensions is not None:
            if 'diameter' in dimensions and dimensions['diameter'] is not None:
                upper_dims['diameter'] = dimensions['diameter']
                lower_dims['diameter'] = dimensions['diameter']
            if 'height' in dimensions and dimensions['height'] is not None:
                if 'upper_height' in dimensions and dimensions['upper_height'] is not None:
                    upper_dims['height'] = dimensions['upper_height']
                    lower_dims['height'] = dimensions['height'] - dimensions['upper_height']
                else:
                    upper_dims['height'] = dimensions['height'] / 2
                    lower_dims['height'] = dimensions['height'] / 2
            if 'upper_cavity_depth' in dimensions and dimensions['upper_cavity_depth'] is not None:
                upper_dims['cavity_depth'] = dimensions['upper_cavity_depth']
                lower_dims['cavity_depth'] = tyre.section_width - dimensions['upper_cavity_depth']
            if 'upper_inner_diameter' in dimensions and dimensions['upper_inner_diameter'] is not None:
                upper_dims['inner_diameter'] = dimensions['upper_inner_diameter']
            if 'lower_inner_diameter' in dimensions and dimensions['lower_inner_diameter'] is not None:
                lower_dims['inner_diameter'] = dimensions['lower_inner_diameter']
            if 'inner_diameter' not in upper_dims:
                if 'inner_diameter' in lower_dims:
                    upper_dims['inner_diameter'] = lower_dims['inner_diameter']
            if 'inner_diameter' not in lower_dims:
                if 'inner_diameter' in upper_dims:
                    lower_dims['inner_diameter'] = upper_dims['inner_diameter']
        self.add_mould_body_2_pieces_upper(upper_dims)
        self.add_mould_body_2_pieces_lower(lower_dims)

    def add_mould_body_2_pieces_upper(self, dimensions: dict = None):
        component = Mould2PsHalfUpper(self, dimensions)
        self._components.append(component)
        self._upper_moulds.append(component)
        return component

    def add_mould_body_2_pieces_lower(self, dimensions: dict = None):
        component = Mould2PsHalfLower(self, dimensions)
        self._components.append(component)
        self._lower_moulds.append(component)
        return component

    @property
    def upper_moulds(self) -> list:
        return self._upper_moulds

    @property
    def lower_moulds(self) -> list:
        return self._lower_moulds

    @property
    def upper_mould(self) -> Mould2PsHalfUpper | None:
        return self._upper_moulds[0] if len(self._upper_moulds) > 0 else None

    @property
    def lower_mould(self) -> Mould2PsHalfLower | None:
        return self._lower_moulds[0] if len(self._lower_moulds) > 0 else None

    @property
    def upper_mould1(self) -> Mould2PsHalfUpper | None:
        return self._upper_moulds[1] if len(self._upper_moulds) > 1 else None

    @property
    def lower_mould1(self) -> Mould2PsHalfLower | None:
        return self._lower_moulds[1] if len(self._lower_moulds) > 1 else None

    @property
    def upper_mould2(self) -> Mould2PsHalfUpper | None:
        return self._upper_moulds[2] if len(self._upper_moulds) > 2 else None

    @property
    def lower_mould2(self) -> Mould2PsHalfLower | None:
        return self._lower_moulds[2] if len(self._lower_moulds) > 2 else None

    @property
    def dimensions(self):
        from .features.mould_2ps_dimensions import Mould2PsDimensions
        dims = Mould2PsDimensions()
        if self.upper_mould is not None:
            dims['upper_mould_diameter'] = self.upper_mould.diameter
            dims['upper_mould_height'] = self.upper_mould.height
            dims['upper_mould_inner_diameter'] = self.upper_mould.inner_diameter
            dims['upper_mould_cavity_depth'] = self.upper_mould.cavity_depth
            dims['upper_mould_vertical_thickness'] = self.upper_mould.vertical_thickness
            dims['upper_mould_horizontal_thickness'] = self.upper_mould.horizontal_thickness
        if self.lower_mould is not None:
            dims['lower_mould_diameter'] = self.lower_mould.diameter
            dims['lower_mould_height'] = self.lower_mould.height
            dims['lower_mould_inner_diameter'] = self.lower_mould.inner_diameter
            dims['lower_mould_cavity_depth'] = self.lower_mould.cavity_depth
            dims['lower_mould_vertical_thickness'] = self.lower_mould.vertical_thickness
            dims['lower_mould_horizontal_thickness'] = self.lower_mould.horizontal_thickness
        return dims

    @property
    def dimensions_formatted(self):
        from .features.mould_2ps_dimensions import Mould2PsDimensions
        dimensions = self.dimensions
        for k, v in dimensions.items():
            if isinstance(v, float) and len(str(v).split('.')[1]) > 2:
                dimensions[k] = round(v, 2)
        return Mould2PsDimensions(dimensions)

    @property
    def primary_dimensions(self):
        from .features.mould_2ps_dimensions import Mould2PsDimensions
        dims = Mould2PsDimensions()
        if self.upper_mould is not None:
            dims['upper_mould_diameter'] = self.upper_mould.primary.diameter
            dims['upper_mould_height'] = self.upper_mould.primary.height
            dims['upper_mould_inner_diameter'] = self.upper_mould.primary.inner_diameter
            dims['upper_mould_cavity_depth'] = self.upper_mould.primary.cavity_depth
            dims['upper_mould_vertical_thickness'] = self.upper_mould.primary.vertical_thickness
            dims['upper_mould_horizontal_thickness'] = self.upper_mould.primary.horizontal_thickness
        if self.lower_mould is not None:
            dims['lower_mould_diameter'] = self.lower_mould.primary.diameter
            dims['lower_mould_height'] = self.lower_mould.primary.height
            dims['lower_mould_inner_diameter'] = self.lower_mould.primary.inner_diameter
            dims['lower_mould_cavity_depth'] = self.lower_mould.primary.cavity_depth
            dims['lower_mould_vertical_thickness'] = self.lower_mould.primary.vertical_thickness
            dims['lower_mould_horizontal_thickness'] = self.lower_mould.primary.horizontal_thickness
        return dims

    @property
    def primary_dimensions_formatted(self):
        from .features.mould_2ps_dimensions import Mould2PsDimensions
        dimensions = self.primary_dimensions
        for k, v in dimensions.items():
            if isinstance(v, float) and len(str(v).split('.')[1]) > 2:
                dimensions[k] = round(v, 2)
        return Mould2PsDimensions(dimensions)
