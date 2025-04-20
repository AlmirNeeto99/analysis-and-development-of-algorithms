from util import swap


def bubbleSort(A):
    A_len = len(A)
    for i in range(A_len - 1, 0, -1):
        for j in range(0, i):
            if A[j] > A[j + 1]:
                swap(A, j, j + 1)
