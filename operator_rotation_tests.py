from __future__ import division

import numpy
from polarizer import Polarizer
from waveplate import WavePlate

# reference mueller matrices from Shurcliff

c1 = lambda theta: numpy.cos(theta)
s1 = lambda theta: numpy.sin(theta)
c2 = lambda theta: c1(2*theta)
s2 = lambda theta: s1(2*theta)


def qwp_M(theta):
    # mueller waveplate, retardance = 90

    r1 = [1, 0, 0, 0]
    r2 = [0, c2(theta)**2, c2(theta)*s2(theta), -s2(theta)]
    r3 = [0, c2(theta)*s2(theta), s2(theta)**2,  c2(theta)]
    r4 = [0, s2(theta), -c2(theta), 0]

    return numpy.matrix([r1, r2, r3, r4])


def hwp_M(theta):
    #  mueller waveplate, retardance = 180

    r1 = [1, 0, 0, 0]
    r2 = [0, c2(theta) ** 2 - s2(theta) ** 2, 2 * c2(theta) * s2(theta), 0]
    r3 = [0, 2 * c2(theta)*s2(theta), s2(theta)**2 - c2(theta)**2, 0]
    r4 = [0, 0, 0, -1]

    return numpy.matrix([r1, r2, r3, r4])


def polarizer_M(theta):
    # mueller polarizer

    r1 = [1, c2(theta), s2(theta), 0]
    r2 = [c2(theta), c2(theta)**2, c2(theta)*s2(theta), 0]
    r3 = [s2(theta), c2(theta)*s2(theta), s2(theta)**2, 0]
    r4 = [0, 0, 0, 0]

    return 0.5*numpy.matrix([r1, r2, r3, r4])


def polarizer_J(theta):
    # jones polarizer

    r1 = [c1(theta)**2, c1(theta)*s1(theta)]
    r2 = [c1(theta)*s1(theta), s1(theta)**2]

    return numpy.matrix([r1, r2])


def hwp_J(theta):
    # jones waveplete, retardance = 180

    r1 = [c2(theta),  s2(theta)]
    r2 = [s2(theta), -c2(theta)]

    return 1j*numpy.matrix([r1, r2])


def qwp_J(theta):
    # jones waveplate, retardance = 90

    p = numpy.exp(numpy.pi * (0 + 1j) / 4)
    q = numpy.exp(numpy.pi * (0 - 1j) / 4)

    r1 = [p*c1(theta)**2 + q*s1(theta)**2, c1(theta)*s1(theta)*numpy.sqrt(2)*1j]
    r2 = [c1(theta)*s1(theta)*numpy.sqrt(2)*1j, q*c1(theta)**2 + p*s1(theta)**2]

    return numpy.matrix([r1, r2])


if __name__ == '__main__':

    random_radians = 2*numpy.pi*numpy.random.rand(100)

    QWP = WavePlate(degrees_retardance=90)
    HWP = WavePlate(degrees_retardance=180)
    POL = Polarizer()

    test_passed = True

    for radians in random_radians:

        degrees = radians*180/numpy.pi

        qwp = qwp_M(radians)
        QWP.absolute_rotate(degrees)

        pol = polarizer_M(radians)
        POL.absolute_rotate(degrees)

        hwp = hwp_M(radians)
        HWP.absolute_rotate(degrees)

        # first round, test mueller matrices
        if not numpy.allclose(pol, POL.mueller.real):
            test_passed = False
            break

        if not numpy.allclose(qwp, QWP.mueller.real):
            test_passed = False
            break

        if not numpy.allclose(hwp, HWP.mueller.real):
            test_passed = False
            break

        qwp = qwp_J(radians)
        pol = polarizer_J(radians)
        hwp = hwp_J(radians)

        # second round, test jones matrices
        if not numpy.allclose(pol, POL.jones):
            test_passed = False
            break

        if not numpy.allclose(qwp, QWP.jones):
            test_passed = False
            break

        if not numpy.allclose(hwp, HWP.jones):
            test_passed = False
            break

    if test_passed:
        print('All rotation tests were equivalent')
    else:
        print('Rotation tests not equivalent!')
