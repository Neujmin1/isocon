

class Light:

    def __init__(self, wavelength=550):

        '''
        It may be possible to do some neat things with a broadband spectrum, but for now
        i'm just going to model a single wavelength
        '''

        self.c = 299792458  # m/s in vacuum (source: https://physics.nist.gov/cgi-bin/cuu/Value?c)
        self.wavelength = wavelength  # nm



