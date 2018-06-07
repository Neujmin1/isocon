from optical_element import OpticalElement


class CompoundElement(OpticalElement):
    def __init__(self):
        OpticalElement.__init__(self)

    def add_element(self, element):
        pass