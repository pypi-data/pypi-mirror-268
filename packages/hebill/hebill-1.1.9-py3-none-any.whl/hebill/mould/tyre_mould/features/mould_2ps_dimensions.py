class Mould2PsDimensions(dict):
    def __init__(self, dimensions: dict = None):
        super().__init__(dimensions if dimensions is not None else {})

    @property
    def diameter(self):
        return max(self.upper_mould_diameter, self.lower_mould_diameter)

    @property
    def height(self):
        return self.upper_mould_height + self.lower_mould_height

    @property
    def upper_mould_diameter(self):
        return self.get('upper_mould_diameter')

    @property
    def upper_mould_height(self):
        return self.get('upper_mould_height')

    @property
    def upper_mould_inner_diameter(self):
        return self.get('upper_mould_inner_diameter')

    @property
    def upper_mould_cavity_depth(self):
        return self.get('upper_mould_cavity_depth')

    @property
    def upper_mould_vertical_thickness(self):
        return self.get('upper_mould_vertical_thickness')

    @property
    def upper_mould_horizontal_thickness(self):
        return self.get('upper_mould_horizontal_thickness')

    @property
    def lower_mould_diameter(self):
        return self.get('lower_mould_diameter')

    @property
    def lower_mould_height(self):
        return self.get('lower_mould_height')

    @property
    def lower_mould_inner_diameter(self):
        return self.get('lower_mould_inner_diameter')

    @property
    def lower_mould_cavity_depth(self):
        return self.get('lower_mould_cavity_depth')

    @property
    def lower_mould_vertical_thickness(self):
        return self.get('lower_mould_vertical_thickness')

    @property
    def lower_mould_horizontal_thickness(self):
        return self.get('lower_mould_horizontal_thickness')
