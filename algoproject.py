#Algorithm Project
# QuickSort using median-of-median group 5 as a pivot.

import os, sys
import copy


def median_quick(q, n):
    sublist = []
    median = []
    pivot = None
    if len(q) >= 1:
        for i in range(0, n, 5):
            sublist.append(q[i:i + 5])
        #print(sublist)
        for j in sublist:
            s = sorted(j)
            if len(s) > 0:
                median.append(s[(len(s) // 2)])
        #print("median array is: %s" % (median))
        #print("array s is:  %s " % (s))

        if len(median) <= 5:
            sorted(median)
            pivot = median[len(median) // 2]
        else:
            sorted(median)
            pivot = median_quick(median, len(median) // 2)
    return pivot


def quicksort(A, p, r):

    if p < r:
        q = median_quick(A[p: r+1], len(A))
        par = partition(A, p, r, q)
        quicksort(A, p, par - 1)
        quicksort(A, par + 1, r)


def partition(A, l, r, pivot):

    for i in range(0, r+1):
        if A[i] == pivot:
            break
    A[i], A[r] = A[r], A[i]
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

    #print("Quick : %s" % (quick))
    quick_copy = copy.deepcopy(quick)
    quicksort(quick, 0, count - 1)
    print("mycode : %s" % (quick))
    quick_copy.sort()
    print("inbuilt : %s" % (quick_copy))
    file.close()

    ''' n = int(input("enter number of elements: "))
        for i in range(n):
            v = input("enter element :")
            quick.append(int(v))
        print(quick)
        quick_copy = copy.deepcopy(quick)
        quicksort(quick, 0, n-1)

        print("mycode : %s" % (quick))
        # print(quick_copy)
        quick_copy.sort()
        print("inbuilt : %s" % (quick_copy))'''