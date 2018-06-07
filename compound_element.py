from optical_element import OpticalElement

import numpy
import mathops
from mirror import Mirror


class CompoundElement(OpticalElement):

    def __init__(self, elements=[]):
        OpticalElement.__init__(self)

        self.elements = elements
        self._update()

    def _update(self):

        if len(self.elements) > 0:

            m = numpy.eye(4)
            j = numpy.eye(2)

            for element in self.elements[::-1]:  # order of operators is R-to-L
                if isinstance(element, Mirror):
                    m = numpy.matmul(m, m)
                    j = numpy.matmul(j, j)
                else:
                    m = numpy.matmul(element.mueller, m)
                    j = numpy.matmul(element.jones, j)

                #m = numpy.matmul(element.mueller, m)
                #j = numpy.matmul(element.jones, j)

            self.mueller = m
            self.jones = j

    def add_element(self, element):

        self.elements.append(element)
        self._update()


