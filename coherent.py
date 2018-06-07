from light import Light
import numpy


class Coherent(Light):

    def __init__(self):

        Light.__init__(self)

        self.phase = 0  # in general, this is complex

        # good for jones
