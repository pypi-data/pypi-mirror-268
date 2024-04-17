import numpy as np


def calculate_distance(dot1, dot2):

    """
    It calculates the Euclidean distance between two points in a 2D plane.

    Args:
        dot1 (tuple): coordinates of the first point, e.g. (x1, y1)
        dot2 (tuple): coordinates of the second point, e.g. (x2, y2)

    Returns:
        float: Euclidean distance between the two points

    """
    x1, y1 = dot1
    x2, y2 = dot2
    distance = np.sqrt((x2 - x1)**2 + (y2 - y1)**2)
    return distance


def generate_4x4_matrix(val1, val2, val3):
    """
    Generate a 4x4 matrix with the same value on the diagonal and the same value on symmetric positions on the
    off-diagonal.

    Useful for generating the capacitance matrix of a 4-dot device with individual control gates. Useful for both
    dot-dot and dot-gate mutual capacitance matrices.


    Args:
        val1 (float): value on the diagonal
        val2 (float): value on the off-diagonal (nearest neighbours)
        val3 (float): value on the off-diagonal (next-nearest neighbours)

    Returns:
        np.array: 4x4 matrix with the same value on the diagonal and the same value on symmetric positions on the
                off-diagonal

    """
    if not isinstance(val1, (int, float)) or not isinstance(val2, (int, float)) or not isinstance(val3, (int, float)):
        raise ValueError("All input values must be numeric (int or float)")

    matrix = [
        [val1, val2, val2, val3],
        [val2, val1, val3, val2],
        [val2, val3, val1, val2],
        [val3, val2, val2, val1]
    ]
    return np.array(matrix)


def generate_3x3_matrix(val1, val2, val3):
    """
    Generate a 3x3 matrix with the same value on the diagonal and the same value on symmetric positions on the
    off-diagonal.

    Useful for generating the capacitance matrix of a 3-dot device with individual control gates. Useful for both
    dot-dot and dot-gate mutual capacitance matrices.

    Args:
        val1 (float): value on the diagonal
        val2 (float): value on the off-diagonal (nearest neighbours)
        val3 (float): value on the off-diagonal (next-nearest neighbours)

    Returns:

    """
    if not isinstance(val1, (int, float)) or not isinstance(val2, (int, float)) or not isinstance(val3, (int, float)):
        raise ValueError("All input values must be numeric (int or float)")

    matrix = [
        [val1, val2, val3],
        [val2, val1, val2],
        [val3, val2, val1]
    ]
    return np.array(matrix)
