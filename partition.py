A = [13,19, 9, 5, 12, 8, 7, 4, 21, 2, 6, 11]

def partition(A):
    x = A[-1]
    i = -1
    for j in range(len(A)):
        if A[j] <= x:
            i += 1
            A[j], A[i] = A[i], A[j]
    
    for k in range(len(A)):
        if k == i:
            print("[{}]".format(A[k]), end=" ")
        else:
            print(A[k], end=" ")
    print()

    return i

partition(A)