#%%
import numpy as np
from typing import List

def binary_fun(A: List[int], search_num: int):
    left = 0
    right = len(A)
    output_list = A[:]
    print(output_list)
    flag = False
    while left < right:
        mid = (left + right) // 2
        if A[mid] == search_num:
            return mid
        elif A[mid] < search_num:
            left = mid + 1
            output_list[0:left] = [-1]
            print(output_list)
        else:
            right = mid
            output_list[right:] = [-1]
            print(output_list)
    if flag == False:
        return -1

if __name__ == "__main__":
    print(binary_fun([1,2,3,4,5,7,8], 7))
    

#%%
