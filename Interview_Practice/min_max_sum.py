#!/bin/python3

import math
import os
import random
import re
import sys
from itertools import combinations

#
# Complete the 'miniMaxSum' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#
'''
Given five positive integers, find the minimum and maximum values 
that can be calculated by summing exactly four of the 
five integers. Then print the respective minimum and maximum values 
as a single line of two space-separated long integers.
'''
#My code below
def miniMaxSum(arr):
    combo_list = []
    for combo in combinations(arr, 4):
        combo_list.append(sum(combo))
    print(min(combo_list), max(combo_list))
#My code above
    

    

if __name__ == '__main__':

    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
