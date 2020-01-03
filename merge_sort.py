import numpy as np
Z = np.random.randint(0,100, size=18)
A = [8,5,9,2,6,3,7,1,10,4]
B = [1,3]
C = [1, 2, 4, 5,6]

counter = 0

def merge(left_list, right_list):
    l_num = len(left_list)
    r_num = len(right_list)
    res = []

    l, r = 0, 0
    while not (l == l_num and r == r_num):
        # print(l, r)
        if l < l_num and r < r_num:
            if left_list[l] < right_list[r]:
                res.append(left_list[l])
                l += 1
            else:
                res.append(right_list[r])
                r += 1
        elif l < l_num:
            res.append(left_list[l])
            l += 1
        elif r < r_num:
            res.append(right_list[r])
            r += 1
        print(res)
        global counter
        counter += 1
    
    return res


def merge_sort(L):
    n = len(L)
    if n <= 1:
        return L

    mid = n // 2
    left_list = merge_sort(L[:mid])
    right_list = merge_sort(L[mid:])

    return merge(left_list, right_list)

if __name__ == "__main__":
    # print(merge(B, C))
    print(merge_sort(A))
    print(counter)