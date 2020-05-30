import random as _random
import time as _time
from typing import Tuple as _Tuple


_random.seed(_time.time())


def sum_between_min_max(array: _Tuple[float]) -> float:
    """Counts sum of elements between min and max elements

    If there is empty, raises exception. If there are only two elements, return zero.
    If all element are equal return zero. In other cases, return sum of elements between first min and first max
    elements, regardless of the order of min and max.

    Args:
        array: tuple with float elements

    Returns:
        sum of elements between min and max

    Raises:
        TypeError: an error occurred when array type is not tuple or element type not str
        ValueError: an error occurred if array is empty
    """

    if type(array) != tuple:
        raise TypeError(f'Expected array type - tuple, got - {type(array)}')

    for element in array:
        if type(element) not in (int, float):
            raise TypeError(f'Expected type of all array elements - float, got - {type(array)}')

    if not array:
        raise ValueError('Array is empty')

    index_min = min(range(len(array)), key=array.__getitem__)
    index_max = max(range(len(array)), key=array.__getitem__)

    if len(array) <= 2:
        return 0

    start = min(index_min, index_max) + 1
    stop = max(index_min, index_max) - 1

    return sum(array[start:stop+1])


if __name__ == '__main__':
    print('App for find sum of elements in 1-dimension array between min and max element')
