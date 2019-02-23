# Quicksort using Randomized method of Pivot selection.

import os,sys,copy
from random import randint

def randomized_quicksort(A, p, r):
    if p < r:
        q = randomized_partition(A, p, r)
        randomized_quicksort(A, p, q-1)
        randomized_quicksort(A, q+1, r)

def randomized_partition(A, p, r):
    i = randint(p, r)
    A[i], A[r] = A[r], A[i]
    return partition(A, p, r)

def partition(A, l, r):
    x = A[r]
    i = l - 1
    for j in range(l, r):
        if A[j] <= x:
            i += 1
            A[i], A[j] = A[j], A[i]
    A[i + 1], A[r] = A[r], A[i + 1]
    return i + 1

if __name__ == '__main__':

    quick = []
    count = 0
    theFile = os.path.join(os.path.expanduser('~'), 'PycharmProjects', 'AlgoProject', 'ArrayInput.txt')
    file = open(theFile, 'r')
    for val in file.read().split():
        count += 1
        quick.append(int(val))
    print("quick array: %s" % (quick))
    randomized_quicksort(quick, 0, count - 1)
    print("Sorted Array : %s" % (quick))


    file.close()
