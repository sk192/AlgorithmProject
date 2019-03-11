# QuickSort using median-of-median group 7 as a pivot.

import os, sys
import copy
import datetime


def median_quick(q, n):
    sublist = []
    median = []
    pivot = None
    if len(q) >= 1:
        for i in range(0, n, 7):
            sublist.append(q[i:i + 7])

        for j in sublist:
            s = sorted(j)
            if len(s) > 0:
                median.append(s[(len(s) // 2)])
        if len(median) <= 7:
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

    file = open('Input.txt', 'r')
    for val in file.read().split():
        count += 1
        quick.append(int(val))

    quick_copy = copy.deepcopy(quick)

    start = datetime.datetime.now()
    quicksort(quick, 0, count - 1)
    finish = datetime.datetime.now()

    print("\n Overall Execution Time of QuickSort: ", (finish - start))

    fileOutput = open('Output.txt', 'w')
    for i in quick:
        fileOutput.write(str(i) + str("\n"))

    start = datetime.datetime.now()
    quick_copy.sort()
    finish = datetime.datetime.now()

    print("\n Overall Execution Time of Inbuilt Sort: ", (finish - start))

    for index in range(len(quick)):                         # To check the all number's are in sorted array. Compared the sorted quick array with inbuilt sorted array.
        if quick[index] != quick_copy[index]:
            print(index)
    file.close()


