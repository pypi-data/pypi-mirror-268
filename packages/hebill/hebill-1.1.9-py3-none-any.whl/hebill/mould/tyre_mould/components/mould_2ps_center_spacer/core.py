from ...features.ring_component import RingComponent


class MouldBodySpacer2Pieces(RingComponent):
    def __init__(self, mould, dimensions: dict | None = None):
        super().__init__(mould, dimensions)

