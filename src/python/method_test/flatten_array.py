# No Shebang line. This file is meant to be imported

__all__ = ["flatten_array"]


def _deep_flatten(array):
    """
    Recursive function to extract integers from a nested list
    :param array: list of elements types
    :return: generator object
    """
    for i in array:
        if isinstance(i, list):
            for x in _deep_flatten(i):
                yield x
        # explicitly checking for ints
        elif isinstance(i, int):
            yield i
        # An else without checking for instance would return other types of data
        # else:
        #     yield i


def flatten_array(array=[]):
    """
     Flattens an array of arbitrarily nested arrays of integers into a flat array of integers.
     e.g. [[1,2,[3]],4] -> [1,2,3,4].
    :param array: list
    :return: list flattened list of integers
    """
    if not isinstance(array, list):
        raise TypeError("Input variable of type {0} not supported".format(type(array)))

    return list(_deep_flatten(array))
