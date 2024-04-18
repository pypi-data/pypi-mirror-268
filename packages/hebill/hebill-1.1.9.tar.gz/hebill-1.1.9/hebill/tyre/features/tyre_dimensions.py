class TyreDimensions(dict):
    def __init__(self, dimensions):
        super().__init__(dimensions)

    @property
    def diameter(self):
        return self.get('diameter')

    @property
    def section_width(self):
        return self.get('section_width')

    @property
    def non_skid_depth(self):
        return self.get('non_skid_depth')

    @property
    def aspect_ratio(self):
        return self.get('aspect_ratio')

    @property
    def rim_size(self):
        return self.get('rim_size')

    @property
    def rim_diameter(self):
        return self.get('rim_diameter')

    @property
    def rim_width(self):
        return self.get('rim_width')
