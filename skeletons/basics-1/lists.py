#!/usr/bin/python
# -*- coding: utf-8 -*-

#
# TEMAT: Listy
#
# -----------------------------------------------------------------------------

from typing import List, Any, Optional


def is_element_on_list(lst: List[Any], e: Any) -> bool:
    return e in lst
    pass


def element_xor(lst: List[Any], e1: Any, e2: Any) -> bool:
    return (e1 in lst) and (e2 not in lst)
    pass


def print_every_second_elem(lst: List[str]) -> None:
    for i in range(len(lst)):
        if i % 2 == 0:
            print(f"{i} -> {lst[i]}") 
        else: continue
    pass


def arg_condition(arg: Optional[List[Any]]) -> bool:
    return arg is None or len(arg) > 2
    pass


def list_condition_1(lst: List[int]) -> bool:
    return len(lst) >= 2 and lst[1] == 5
    pass


def list_condition_2(lst: List[int]) -> bool:
    return 2 <= len(lst) <= 4 and lst[-2] == 3
    pass


def remove_first_three_elements(lst: List[Any]) -> None:
    del(lst[:3])
    pass


def replace_last_two_elements(lst: List[int]) -> List[int]:
    if len(lst) >= 2:
        lst2 = lst[:-1]
        lst2[-1] = 9
        return lst2
    else:  
        lst2 = lst[:]
        return lst2
    pass


def merge_ends(lst: Optional[List[Any]] = None) -> List[Any]:
    if lst is None or len(lst) == 0:
        lst2 = []
    elif len(lst) >= 4:
        lst2 = lst[:2] + lst[-2:]
    else:
        lst2 = [lst[0], lst[0]]
    return lst2
    pass


def remove_element_if_exists(lst: List[Any], e: Any) -> List[Any]:
    lst2 = lst[:]
    if e in lst2:
        lst2.remove(e)
    return lst2
    pass


# [OPT]
def is_palindrome(s: str) -> bool:
    if len(s)%2==0:
        return s[:int(len(s)/2)] == s[-1:int(-len(s)/2)]
    else:
        return s[:int((len(s)-1)/2)] == s[-1:int(-(len(s)+1)/2):-1]
    pass
