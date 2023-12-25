#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'plusMinus' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#
'''
Given an array of integers, calculate the ratios of its 
elements that are positive, negative, and zero. 
Print the decimal value of each fraction on a 
new line with places after the decimal.
'''
# My Code below
def plusMinus(arr):
    pos = 0
    neg = 0
    zero = 0
    for integer in arr:
        if integer > 0:
            pos += 1
        elif integer < 0:
            neg += 1
        else:
            zero += 1
    print(f"{pos / len(arr)}\n{neg / len(arr)}\n{zero / len(arr)}")   
# My Code here above



if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
