from light import Light


class Incohrent(Light):

    def __init__(self):

        Light.__init__(self)

        self.stokes_vector = [1, 0, 0, 0]  # unpolarized state (I, M, C, S)
