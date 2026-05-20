#!/usr/bin/python
# -*- coding: utf-8 -*-

#
# TEMAT: Instrukcje sterujące
#
# -----------------------------------------------------------------------------

def parity_str(n: int) -> str:
  
    if n%2==0:
        return "parzysta"
    return "nieparzysta"

    pass


def plf(x: float) -> float:
   
    if x<3:
        return 1
    elif x>=10:
        return 4
    return 1.5

    pass


def factorial(n: int) -> int:
    fact = 1
    for i in range(1, n+1):
        fact *= i
    return fact
    pass


def min_pow_2(n: int) -> int:
    p = 1
    while(n >= p):
        p *= 2
    return p
    pass
