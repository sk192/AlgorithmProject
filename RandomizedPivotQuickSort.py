# Quicksort using Randomized method of Pivot selection.

# Input: Input.txt file
# Output: Sorted array written in output.txt file

import os,sys,copy
from random import randint
import datetime

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

    file = open('Input.txt', 'r')
    for val in file.read().split():
        count += 1
        quick.append(int(val))

    quick_copy = copy.deepcopy(quick)

    start = datetime.datetime.now()
    randomized_quicksort(quick, 0, count - 1)
    finish = datetime.datetime.now()

    print("\n Overall Execution Time of QuickSort: ", (finish - start))

    fileOutput = open('Output.txt', 'w')
    for i in quick:
        fileOutput.write(str(i) + str("\n"))

    start = datetime.datetime.now()
    quick_copy.sort()
    finish = datetime.datetime.now()
    print("\n Overall Execution Time of Inbuilt Sort: ", (finish - start))

    for index in range(len(quick)):                     # To check the all number's are in sorted array. Compared the sorted quick array with inbuilt sorted array.
        if quick[index] != quick_copy[index]:
            print(index)
    file.close()

