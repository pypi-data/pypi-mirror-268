from ...features.ring_component import RingComponent
from ...constants import CLAMP_RING_DIAMETER_TO_RIM_DIAMETER, CLAMP_RING_INNER_DIAMETER_TO_RIM_DIAMETER, \
    CLAMP_RING_HEIGHT_TO_TYRE_WIDTH


class ClampRingLower(RingComponent):
    def __init__(self, mould, dimensions: dict | None = None):
        super().__init__(mould, dimensions)
        self._primary = None
        if self.diameter is None:
            self.diameter = self.tyre.rim_diameter * CLAMP_RING_DIAMETER_TO_RIM_DIAMETER
        if self.inner_diameter is None:
            self.inner_diameter = self.tyre.rim_diameter * CLAMP_RING_INNER_DIAMETER_TO_RIM_DIAMETER
        if self.height is None:
            self.height = self.tyre.section_width * CLAMP_RING_HEIGHT_TO_TYRE_WIDTH

    @property
    def primary(self):
        if self._primary is None:
            self._primary = RingComponent(self.mould, {
                'diameter': self.tyre.primary.rim_diameter * CLAMP_RING_DIAMETER_TO_RIM_DIAMETER,
                'inner_diameter': self.tyre.primary.rim_diameter * CLAMP_RING_INNER_DIAMETER_TO_RIM_DIAMETER,
                'height': self.tyre.primary.section_width * CLAMP_RING_HEIGHT_TO_TYRE_WIDTH
            })
        return self._primary

