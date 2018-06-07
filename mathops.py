from __future__ import division

import numpy


def jones2mueller(jones_matrix):
    # converts jones matrix to mueller matrix (if applicable)

    J = numpy.matrix(jones_matrix)

    r1 = numpy.array([1, 0, 0, 1])
    r2 = numpy.array([1, 0, 0, -1])
    r3 = numpy.array([0, 1, 1, 0])
    r4 = numpy.array([0, 1j, -1j, 0])

    A = numpy.matrix(numpy.array([r1, r2, r3, r4]))

    M = numpy.kron(J, J.H)
    M = numpy.matmul(M, 0.5*A.H)
    M = numpy.matmul(A, M)

    return M


def rotate_jones(jones_matrix, rotation_degrees_ccw):

    r2 = rotation_matrix2D(rotation_degrees_ccw)

    return numpy.matmul(r2.transpose(), numpy.matmul(jones_matrix, r2))


def rotate_mueller(mueller_matrix, rotation_degrees_ccw):

    m = numpy.eye(4)
    m[1:3, 1:3] = rotation_matrix2D(2*rotation_degrees_ccw)  # TODO 1 or 2*angle?

    mueller_matrix = numpy.matmul(m.transpose(), numpy.matmul(mueller_matrix, m))

    return mueller_matrix


def rotation_matrix2D(rotation_degrees_ccw):
    # canonical 2D rotation matrix

    rotm3 = rotation_matrix3D([0, 0, 1], rotation_degrees_ccw)

    return rotm3[0:2, 0:2]


def rotation_matrix3D(unit_axis_of_rotation, rotation_degrees_ccw):
    # canonical 3D rotation matrix

    rads = -rotation_degrees_ccw*numpy.pi/180

    # make sure unit_axis is normalized
    unit_axis_of_rotation = numpy.array(unit_axis_of_rotation)
    unit_axis_of_rotation = numpy.divide(unit_axis_of_rotation, numpy.linalg.norm(unit_axis_of_rotation))

    if not len(unit_axis_of_rotation) == 3:
        return None  # TODO better to throw a warning here
    else:

        wx, wy, wz = unit_axis_of_rotation
        skew = numpy.matrix(numpy.array([[0, -wz, wy], [wz, 0, -wx], [-wy, wx, 0]]))
        rotm = numpy.eye(3) + numpy.sin(rads)*skew + (1 - numpy.cos(rads))*numpy.matmul(skew, skew)

        return rotm

