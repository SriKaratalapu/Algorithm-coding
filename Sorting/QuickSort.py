import random

def QuickSort(A):
    return QuickSortHelper(A,0,len(A)-1)

def Swap(A,index1,index2):
    A[index1],A[index2] = A[index2],A[index1]
    return A


def QuickSortHelper(A,start,end):

    if start >= end:
        return

    randindex =  random.randint(start,end)
    A = Swap(A,start,randindex)

    pivot = A[start]
    smaller =  start
    bigger = start

    for bigger in range(start+1,end+1):
        if A[bigger] <= pivot:
            smaller +=1
            A= Swap(A,smaller,bigger)

    A = Swap(A,start, smaller)

    QuickSortHelper(A,start,smaller-1)
    QuickSortHelper(A,smaller+1,end)
    return A


B = [4,1,3,0,8,8,9]
print(QuickSort(B))