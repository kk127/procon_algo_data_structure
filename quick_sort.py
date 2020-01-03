import partition
import numpy as np

def quick_sort(A):
    if len(A) <= 1:
        pass
    else:
        index = partition.partition(A)

        quick_sort(A[:index])
        quick_sort(A[index+1:])

# A = [1, 3,  6, 7, 9, 3,1]
Z = np.random.randint(0,1000, size=1000)
print(Z)
quick_sort(Z)
print(Z)