"""
Implement pow(x, n), which calculates x raised to the power n (x^n).
"""

def myPow(x, n):
    """
    :type x: float
    :type n: int
    :rtype: float
    """

    if n < 0:
        return 1/(myPow(x, -n))

    if n == 0:
        return 1

    
