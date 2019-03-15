# Quicksort using Randomized method of Pivot selection.

# Input: Array which contains elements from Input.txt file
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
    i = randint(p, r)                               # randomly choose element from array. return index of random element.
    A[i], A[r] = A[r], A[i]
    return partition(A, p, r)

def partition(A, l, r):                             # Partition function to fix the pivot position
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
        quick.append(int(val))                           # Copy all numbers from Input.txt file into array quick.

    quick_copy = copy.deepcopy(quick)                   # make the copy of input array

    start = datetime.datetime.now()                         # Execution start time of randomized_quicksort
    randomized_quicksort(quick, 0, count - 1)
    finish = datetime.datetime.now()                     # Execution finish time of randomized_quicksort

    print("\n Overall Execution Time of QuickSort: ", (finish - start))

    fileOutput = open('Output.txt', 'w')
    for i in quick:
        fileOutput.write(str(i) + str("\n"))                        # Write sorted array in Output.txt file.

    start = datetime.datetime.now()                         # Execution start time of inbuit sort()
    quick_copy.sort()                                             # Inbuilt sort function.
    finish = datetime.datetime.now()                        # Execution finish time of inbuilt sort()

    print("\n Overall Execution Time of Inbuilt Sort: ", (finish - start))

    for index in range(len(quick)):                     # To check all numbers of an array quick is in sorted increasing order.
        if quick[index] != quick_copy[index]:            # Compared the sorted quick array with inbuilt sorted array.
            print(index)
    file.close()

