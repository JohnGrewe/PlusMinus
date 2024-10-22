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

def plusMinus(arr):
    positive = 0
    negative = 0
    zero = 0
    

#This is my solved solution for plus minus
    for n in arr:
        if n>0:
            positive = positive+1
        elif n<0:
            negative = negative+1
        elif n == 0:
            zero = zero+1
        
    total = len(arr)
    positive_ratio = positive/total
    negative_ratio = negative/total
    zero_ratio = zero/total

    print(f"{positive_ratio:.6f}")
    print(f"{negative_ratio:.6f}")
    print(f"{zero_ratio:.6f}")
    
    # Write your code here

    if __name__ == '__main__':
        n = int(input().strip())
        arr = list(map(int, input().rstrip().split()))
        plusMinus(arr)

