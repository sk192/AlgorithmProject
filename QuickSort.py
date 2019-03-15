# Naive implementation of QuickSort

# Input: Array which contains elements from Input.txt file
# Output: Sorted array written in output.txt file

import os, sys
import copy
import datetime, random


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

    file = open('Input.txt', 'r')
    for val in file.read().split():
        count += 1
        quick.append(int(val))                      # Copy all numbers from Input.txt file into array quick.

    quick_copy = copy.deepcopy(quick)

    start = datetime.datetime.now()                 # Execution start time
    quicksort(quick, 0, count - 1)
    finish = datetime.datetime.now()                # Execution finish time

    print("\n Overall Execution Time of quick sort: ", (finish - start))

    fileOutput = open('Output.txt', 'w')
    for i in quick:
        fileOutput.write(str(i)+str("\n"))          # Write sorted array in Output.txt file.


    start = datetime.datetime.now()
    quick_copy.sort()                               # Inbuilt sort function.
    finish = datetime.datetime.now()

    print("\n Overall Execution Time of inbuilt sort: ", (finish - start))

    for index in range(len(quick)):                     # To check all numbers of an array quick is in sorted increasing order.
        if quick[index] != quick_copy[index]:           # Compared the sorted quick array with inbuilt sorted array.
            print(index)
    file.close()

