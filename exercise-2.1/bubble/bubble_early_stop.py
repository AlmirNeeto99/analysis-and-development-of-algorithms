from util import swap

def bubbleSortEarlyStop(A):
    A_len = len(A)
    for i in range(A_len - 1, 0, -1):
        swaped = False
        for j in range(0, i):
            if A[j] > A[j + 1]:
                swap(A, j, j + 1)
                swaped = True
        if not swaped:
            break
