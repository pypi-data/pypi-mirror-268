from .features.tyre import Tyre as ObjectTPL
from .constansts import SIZE_DEFAULT_ASPECT_RATIOS, RATIO_NSD_TO_SW, RATIO_RW_TO_SW, SIZE_DEFAULT_ASPECT_RATIO


class Tyre(ObjectTPL):
    def __init__(self, size, dimensions: dict = None):
        self._primary = None
        self._secondary = None
        super().__init__(size, dimensions)
        if self.rim_size is None:
            if self.primary.rim_size is not None:
                self.rim_size = self.primary.rim_size
            elif self.secondary.rim_size is not None:
                self.rim_size = self.secondary.rim_size

        if self.rim_diameter is None:
            if self.rim_size is not None:
                self.rim_diameter = self.rim_size * 25.4
            elif self.primary.rim_diameter is not None:
                self.rim_diameter = self.primary.rim_diameter
            elif self.secondary.rim_diameter is not None:
                self.rim_diameter = self.secondary.rim_diameter
        if self.aspect_ratio is None:
            if self.diameter is not None and self.section_width is not None and self.rim_diameter is not None:
                self.aspect_ratio = round((self.diameter - self.rim_diameter) / 2 / self.section_width, 4) * 100
            elif self.primary.aspect_ratio is not None:
                self.aspect_ratio = self.primary.aspect_ratio
            elif self.secondary.aspect_ratio is not None:
                self.aspect_ratio = self.secondary.aspect_ratio
            else:
                self.aspect_ratio = SIZE_DEFAULT_ASPECT_RATIO

        if self.diameter is None:
            if self.section_width is not None and self.rim_diameter is not None:
                self.diameter = self.section_width * self.aspect_ratio * 2 / 100 + self.rim_diameter
            elif self.primary.diameter is not None:
                self.diameter = self.primary.diameter
            elif self.secondary.diameter is not None:
                self.diameter = self.secondary.diameter

        if self.section_width is None:
            if self.diameter is not None and self.rim_diameter is not None:
                self.section_width = (self.diameter - self.rim_diameter) / 2 / self.aspect_ratio * 100
            elif self.primary.section_width is not None:
                self.section_width = self.primary.section_width
            elif self.secondary.section_width is not None:
                self.section_width = self.secondary.section_width

        if self.section_width is not None:
            if self.non_skid_depth is None:
                self.non_skid_depth = round(self.section_width * RATIO_NSD_TO_SW, 2)
            if self.rim_width is None:
                self.rim_width = round(self.section_width * RATIO_RW_TO_SW)

    @property
    def size_formatted(self) -> str:
        if self.secondary.size:
            return '|'.join([self.primary.size, self.secondary.size])
        return self.primary.size

    def _primary_secondary(self):
        primary = self.parse_size(self.size)
        secondary = self.parse_size(self.size, 2)
        if primary['rim_size_perfect'] and not secondary['rim_size_perfect']:
            secondary['rim_size'] = primary['rim_size']
        if secondary['rim_size_perfect'] and not secondary['rim_size_perfect']:
            primary['rim_size'] = secondary['rim_size']
        if primary['aspect_ratio_perfect'] and not secondary['aspect_ratio_perfect']:
            secondary['aspect_ratio'] = primary['aspect_ratio']
        if secondary['aspect_ratio_perfect'] and not primary['aspect_ratio_perfect']:
            primary['aspect_ratio'] = secondary['aspect_ratio']

        def workout(d: ObjectTPL):
            if d.rim_diameter is None:
                if d.rim_size is not None:
                    d.rim_diameter = d.rim_size * 25.4
            if d.aspect_ratio is None:
                if d.diameter is not None and d.section_width is not None and d.rim_diameter is not None:
                    d.aspect_ratio = round((d.diameter - d.rim_diameter) / 2 / d.section_width, 2) * 100
                elif d.size in SIZE_DEFAULT_ASPECT_RATIOS:
                    d.aspect_ratio = SIZE_DEFAULT_ASPECT_RATIOS[d.size]
                else:
                    d.aspect_ratio = 96
            if d.diameter is None:
                if d.section_width is not None and d.rim_diameter is not None:
                    d.diameter = d.section_width * d.aspect_ratio * 2 / 100 + d.rim_diameter
            if d.section_width is None:
                if d.diameter is not None and d.rim_diameter is not None:
                    d.section_width = (d.diameter - d.rim_diameter) / 2 / d.aspect_ratio * 100
            if d.section_width is not None:
                d.non_skid_depth = round(d.section_width * RATIO_NSD_TO_SW, 2)
                d.rim_width = round(d.section_width * RATIO_RW_TO_SW)
        self._primary = ObjectTPL(primary['size'], primary)
        self._secondary = ObjectTPL(secondary['size'], secondary)
        workout(self.primary)
        workout(self.secondary)

    @property
    def primary(self) -> ObjectTPL:
        if self._primary is None:
            self._primary_secondary()
        return self._primary

    @property
    def secondary(self) -> ObjectTPL:
        if self._secondary is None:
            self._primary_secondary()
        return self._secondary
