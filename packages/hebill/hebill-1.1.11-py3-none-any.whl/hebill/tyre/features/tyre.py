import re
from ...dimensions.core import Dimensions as DimensionsTPL
from ...string.core import String
from ..constansts import (SIZE_SYMBOLS, SIZE_MAX_RIM_SIZE_INCH, SIZE_MAX_SECTION_WIDTH_INCH,
                          SIZE_MIN_ASPECT_RATIO, SIZE_MAX_ASPECT_RATIO, SIZE_MAX_DIAMETER_INCH)
from .tyre_dimensions import TyreDimensions


class Tyre(DimensionsTPL):
    names = ['diameter', 'section_width', 'non_skid_depth', 'aspect_ratio', 'rim_size', 'rim_diameter', 'rim_width']

    def __init__(self, size, dimensions: dict = None):
        super().__init__(dimensions)
        self._size = size
        self._error = ''

    @property
    def size(self):
        return self._size

    @property
    def diameter(self):
        return self['diameter']

    @diameter.setter
    def diameter(self, dim: float | int = None):
        self['diameter'] = dim

    @property
    def section_width(self):
        return self['section_width']

    @section_width.setter
    def section_width(self, dim: float | int = None):
        self['section_width'] = dim

    @property
    def non_skid_depth(self):
        return self['non_skid_depth']

    @non_skid_depth.setter
    def non_skid_depth(self, dim: float | int = None):
        self['non_skid_depth'] = dim

    @property
    def aspect_ratio(self):
        return self['aspect_ratio']

    @aspect_ratio.setter
    def aspect_ratio(self, dim: float | int = None):
        self['aspect_ratio'] = dim

    @property
    def rim_size(self):
        return self['rim_size']

    @rim_size.setter
    def rim_size(self, dim: float | int = None):
        self['rim_size'] = dim

    @property
    def rim_width(self):
        return self['rim_width']

    @rim_width.setter
    def rim_width(self, dim: float | int = None):
        self['rim_width'] = dim

    @property
    def rim_diameter(self):
        return self['rim_diameter']

    @rim_diameter.setter
    def rim_diameter(self, dim: float | int = None):
        self['rim_diameter'] = dim

    @staticmethod
    def parse_size(size, serial: int = 1):
        data = {
            'size': None,
            'left': None,
            'symbol1': None,
            'middle': None,
            'symbol2': None,
            'right': None,
            'diameter': None,
            'diameter_perfect': False,
            'section_width': None,
            'section_width_perfect': False,
            'aspect_ratio': None,
            'aspect_ratio_perfect': False,
            'rim_size': None,
            'rim_size_perfect': False
        }
        # 转换字符串为可读取型号
        size = size.upper()
        # 去除无用字符
        size = re.sub(r'[^._0-9A-Z()\[|/-]+', '', size)
        # 转换"("和"["为"|"
        size = size.replace('(', '|').replace('[', '|').replace('LL-', '-').replace('*', 'X').replace('_', '-')
        sizes = size.split('|')
        parsed = False
        if serial <= len(sizes):
            size = sizes[serial - 1]
            ####################################################################################################
            for symbols in SIZE_SYMBOLS:
                number_pattern = r'\d+(\.\d+)?'
                pattern = rf'{number_pattern}'
                pattern = rf'{pattern}\*' if symbols[0] == '*' else rf'{pattern}{symbols[0]}'
                if symbols[1] is None:
                    pattern = rf'{pattern}{number_pattern}'
                    if re.fullmatch(pattern, size):
                        parsed = True
                        data['size'] = size
                        data['left'], data['right'] = size.split(symbols[0])
                        data['symbol1'] = symbols[0]
                        break
                else:
                    pattern = rf'{pattern}{number_pattern}'
                    pattern = rf'{pattern}\*' if symbols[1] == '*' else rf'{pattern}{symbols[1]}'
                    pattern = rf'{pattern}{number_pattern}'
                    if re.fullmatch(pattern, size):
                        parsed = True
                        split = size.split(symbols[0])
                        data['size'] = size
                        data['left'] = split[0]
                        data['middle'], data['right'] = split[1].split(symbols[1])
                        data['symbol1'], data['symbol2'] = symbols
                        break
        if parsed:
            if isinstance(data['right'], str):
                rs = String(data['right']).digitize()
                data['rim_size_perfect'] = rs < SIZE_MAX_RIM_SIZE_INCH
                data['rim_size'] = rs if rs < SIZE_MAX_RIM_SIZE_INCH else round(rs / 25.4, 3)
            if data['symbol1'] == '/' or data['symbol1'] == '-':
                if isinstance(data['left'], str):
                    sw = String(data['left']).digitize()
                    data['section_width_perfect'] = sw > SIZE_MAX_SECTION_WIDTH_INCH
                    data['section_width'] = sw if sw > SIZE_MAX_SECTION_WIDTH_INCH else round(sw * 25.4, 3)
                if isinstance(data['middle'], str):
                    ar = String(data['middle']).digitize()
                    data['aspect_ratio_perfect'] = SIZE_MIN_ASPECT_RATIO <= ar <= SIZE_MAX_ASPECT_RATIO
                    if SIZE_MIN_ASPECT_RATIO <= ar <= SIZE_MAX_ASPECT_RATIO:
                        data['aspect_ratio'] = ar
            if data['symbol1'] == 'X':
                if isinstance(data['left'], str):
                    od = String(data['left']).digitize()
                    data['diameter_perfect'] = od > SIZE_MAX_DIAMETER_INCH
                    data['diameter'] = od if od > SIZE_MAX_DIAMETER_INCH else round(od * 25.4, 3)
                if isinstance(data['middle'], str):
                    sw = String(data['middle']).digitize()
                    data['section_width_perfect'] = sw > SIZE_MAX_SECTION_WIDTH_INCH
                    data['section_width'] = sw if sw > SIZE_MAX_SECTION_WIDTH_INCH else round(sw * 25.4, 3)
        return data

    @property
    def dimensions(self):
        return TyreDimensions({
            'diameter': self.diameter,
            'section_width': self.section_width,
            'non_skid_depth': self.non_skid_depth,
            'aspect_ratio': self.aspect_ratio,
            'rim_size': self.rim_size,
            'rim_diameter': self.rim_diameter,
            'rim_width': self.rim_width,
        })

    @property
    def dimensions_formatted(self):
        dimensions = self.dimensions
        for k, v in dimensions.items():
            if isinstance(v, float) and len(str(v).split('.')[1]) > 2:
                dimensions[k] = round(v, 2)
        return TyreDimensions(dimensions)
