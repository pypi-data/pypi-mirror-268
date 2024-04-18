from .components.bead_ring_upper.core import BeadRingUpper
from .components.bead_ring_middle.core import BeadRingMiddle
from .components.bead_ring_lower.core import BeadRingLower
from .components.clamp_ring_upper.core import ClampRingUpper
from .components.clamp_ring_lower.core import ClampRingLower
from ...tyre.core import Tyre


class Mould:
    def __init__(self, tyre: Tyre):
        self._tyre = tyre
        self._components = []
        self._upper_bead_rings = []
        self._middle_bead_rings = []
        self._lower_bead_rings = []
        self._upper_clamp_rings = []
        self._lower_clamp_rings = []

    @property
    def tyre(self) -> Tyre:
        return self._tyre

    @property
    def size(self):
        return self.tyre.size

    @property
    def components(self) -> list:
        return self._components

    def add_bead_ring_upper(self, dimensions: dict = None):
        component = BeadRingUpper(self, dimensions)
        self._components.append(component)
        self._upper_bead_rings.append(component)
        return component

    def add_bead_ring_middle(self, dimensions: dict = None):
        component = BeadRingMiddle(self, dimensions)
        self._components.append(component)
        self._middle_bead_rings.append(component)
        return component

    def add_bead_ring_lower(self, dimensions: dict = None):
        component = BeadRingLower(self, dimensions)
        self._components.append(component)
        self._lower_bead_rings.append(component)
        return component

    def add_clamp_ring_upper(self, dimensions: dict = None):
        component = ClampRingUpper(self, dimensions)
        self._components.append(component)
        self._upper_clamp_rings.append(component)
        return component

    def add_clamp_ring_lower(self, dimensions: dict = None):
        component = ClampRingLower(self, dimensions)
        self._components.append(component)
        self._lower_clamp_rings.append(component)
        return component

    @property
    def upper_bead_rings(self) -> list:
        return self._upper_bead_rings

    @property
    def middle_bead_rings(self) -> list:
        return self._middle_bead_rings

    @property
    def lower_bead_rings(self) -> list:
        return self._lower_bead_rings

    @property
    def upper_clamp_rings(self) -> list:
        return self._upper_clamp_rings

    @property
    def lower_clamp_rings(self) -> list:
        return self._lower_clamp_rings

    @property
    def upper_bead_ring(self) -> BeadRingUpper | None:
        return self._upper_bead_rings[0] if len(self._upper_bead_rings) > 0 else None

    @property
    def middle_bead_ring(self) -> BeadRingMiddle | None:
        return self._middle_bead_rings[0] if len(self._upper_bead_rings) > 0 else None

    @property
    def lower_bead_ring(self) -> BeadRingLower | None:
        return self._upper_clamp_rings[0] if len(self._upper_bead_rings) > 0 else None

    @property
    def upper_clamp_ring(self) -> ClampRingUpper | None:
        return self._upper_clamp_rings[0] if len(self._upper_bead_rings) > 0 else None

    @property
    def lower_clamp_ring(self) -> ClampRingLower | None:
        return self._lower_clamp_rings[0] if len(self._upper_bead_rings) > 0 else None

    @property
    def upper_bead_ring1(self) -> BeadRingUpper | None:
        return self._upper_bead_rings[1] if len(self._upper_bead_rings) > 1 else None

    @property
    def middle_bead_ring1(self) -> BeadRingMiddle | None:
        return self._middle_bead_rings[1] if len(self._upper_bead_rings) > 1 else None

    @property
    def lower_bead_ring1(self) -> BeadRingLower | None:
        return self._upper_clamp_rings[1] if len(self._upper_bead_rings) > 1 else None

    @property
    def upper_clamp_ring1(self) -> ClampRingUpper | None:
        return self._upper_clamp_rings[1] if len(self._upper_bead_rings) > 1 else None

    @property
    def lower_clamp_ring1(self) -> ClampRingLower | None:
        return self._lower_clamp_rings[1] if len(self._upper_bead_rings) > 1 else None

    @property
    def upper_bead_ring2(self) -> BeadRingUpper | None:
        return self._upper_bead_rings[2] if len(self._upper_bead_rings) > 2 else None

    @property
    def middle_bead_ring2(self) -> BeadRingMiddle | None:
        return self._middle_bead_rings[2] if len(self._upper_bead_rings) > 2 else None

    @property
    def lower_bead_ring2(self) -> BeadRingLower | None:
        return self._upper_clamp_rings[2] if len(self._upper_bead_rings) > 2 else None

    @property
    def upper_clamp_ring2(self) -> ClampRingUpper | None:
        return self._upper_clamp_rings[2] if len(self._upper_bead_rings) > 2 else None

    @property
    def lower_clamp_ring2(self) -> ClampRingLower | None:
        return self._lower_clamp_rings[2] if len(self._upper_bead_rings) > 2 else None

    def weight(self, margin: float = 0, density: float = 7.8):
        wt = 0
        for component in self.components:
            wt += component.weight(margin, density)
        return wt

    def primary_weight(self, margin: float = 0, density: float = 7.8):
        wt = 0
        for component in self.components:
            wt += component.primary.weight(margin, density)
        return wt
