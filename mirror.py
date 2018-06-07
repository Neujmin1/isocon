from optical_element import OpticalElement


class Mirror(OpticalElement):  # just changes phase by pi

    def __init__(self):
        OpticalElement.__init__(self)