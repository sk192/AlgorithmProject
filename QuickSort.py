
import os, sys
import copy

def quicksort(A, p, r):

    if p < r:
        q = partition(A, p, r)
        quicksort(A, p, q - 1)
        quicksort(A, q + 1, r)

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
    quick_copy = copy.deepcopy(quick)
    quicksort(quick, 0, count - 1)
    print("Sorted Array : %s" % (quick))
    quick_copy.sort()
    print("inbuilt : %s" % (quick_copy))
    file.close()