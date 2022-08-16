#By Filipe Chagas
#Mar 2022

from typing import *

def natural_to_binary(x: int, n: int) -> List[bool]:
    """Returns x in the binary system.

    :param x: Natural (including zero) to convert.
    :type x: int
    :param n: Number of bits.
    :type n: int
    :return: List of bits. Each bit is a bool. Most significant bit last.
    :rtype: List[bool]
    """
    assert n > 0
    assert x >= 0
    assert x < 2**n
    return [bool((x//2**i)%2) for i in range(n)]

def binary_to_natural(x: List[bool]) -> int:
    """Returns x as a natural number (including zero).

    :param x: List of bits. Most significant bit last.
    :type x: List[bool]
    :return: Natural number (including zero).
    :rtype: int
    """
    n = len(x)
    return sum([(2**i)*int(x[i]) for i in range(n)])

def two_complement(x: List[bool]) -> List[bool]:
    """Returns the 2's complement for x.

    :param x: List of bits. Most significant bit last.
    :type x: List[bool]
    :return: 2's complement of x. List of bits. Most significant bit last.
    :rtype: List[bool]
    """
    n = len(x)
    one_complement = [not x_i for x_i in x]
    return natural_to_binary(binary_to_natural(one_complement) + 1, n)

def integer_to_binary(x: int, n: int) -> List[bool]:
    """Returns x in the binary system using 2's complement notation.

    :param x: Integer value to convert.
    :type x: int
    :param n: Number of bits.
    :type n: int
    :return: List of bits. Less significant bit fist. Sign bit last.
    :rtype: List[bool]
    """
    assert n > 0
    assert x < 2**(n-1)
    assert x >= -2**(n-1)
    return natural_to_binary(x, n) if x >= 0 else two_complement(natural_to_binary(-x, n))

def binary_to_integer(x: List[bool]) -> int:
    """Returns x as an integer number.

    :param x: List of bits. Less significant bit fist. Sign bit last.
    :type x: List[bool]
    :return: Integer number.
    :rtype: int
    """
    n = len(x)
    return binary_to_natural(x) if x[n-1] == False else -binary_to_natural(two_complement(x))