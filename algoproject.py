#project

import os, sys



def median_quick(q, n):
    sublist = []
    median = []
    pivot = None
    if len(q) > 1:
        for i in range(0, n, 5):
            sublist.append(q[i:i + 5])
        print(sublist)
        for j in range(len(sublist)):
            s = sorted(sublist[j])
            median.append(s[(len(s) // 2)])
        print(median)
        if len(median) <= 5:
            sorted(median)
            pivot = median[len(median) // 2]
            #print ("pivot: %d" %pivot)
           #  return pivot
        else:
            sorted(median)
            pivot = median_quick(median, len(median) // 2)
    return pivot


def quicksort(A, p, r):

    if p < r:
        q = median_quick(A,len(A))
        print("pivot: %d" %(q))
        par = partition(A, p, r, q)
        print("i+1 index par: %d" %(par))
        print("r , p: %d %d" %(r,p))
        quicksort(A, p, par - 1)
        quicksort(A, par + 1, r)


def partition(A, l, r, pivot):

    for i in range(0, r+1):
        if A[i] == pivot:
            break
    A[i], A[r] = A[r], A[i]
    # A[r] = A[i]
    print(A)
    x = A[r]
    print("x: %d" %(x))
    i = l - 1
    for j in range(l, r - 1):
        if A[j] <= x:
            i += 1
            print("i : %d" %i)
            A[i], A[j] = A[j], A[i]
    A[i + 1], A[r] = A[r], A[i + 1]
    print(A)
    return i + 1

if __name__ == '__main__':
    quick = []
    n = int(input("enter number of elements: "))
    for i in range(n):
        v = input("enter element :")
        quick.append(int(v))
    print(quick)
    quicksort(quick, 0, n-1)
    for i in range(n):
        print ("%d" %quick[i])
    # print(median_quick([(i + 1) for i in range(11)], 11))
