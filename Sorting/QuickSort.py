import random

def quick_sort(A):
    quick_sort_helper(A,0,len(A)-1)
    return A

def swap(A,index1,index2):
    A[index1],A[index2] = A[index2],A[index1]
    return A

'''
Quick Sort using Lomuto's partitioning
'''
# def quick_sort_helper(A,start,end):
#
#     if start >= end:
#         return
#
#     randindex =  random.randint(start,end)
#     A = swap(A,start,randindex)
#
#     pivot = A[start]
#     smaller =  start
#     bigger = start
#
#     for bigger in range(start+1,end+1):
#         if A[bigger] <= pivot:
#             smaller +=1
#             A= swap(A,smaller,bigger)
#
#     A = swap(A,start, smaller)
#
#     quick_sort_helper(A,start,smaller-1)
#     quick_sort_helper(A,smaller+1,end)



'''
Quick Sort using hoare's partitioning
'''

def quick_sort_helper(A,start,end):
    if start >= end:
        return

    randindex = random.randint(start,end)
    #print(A)
    A = swap(A,start,randindex)
    #print(randindex)
    pivot = A[start]
    i = start + 1
    j = end

    print(pivot)
    #print(A)
    while i <= j:
        #print(i,j)
        if A[i] < pivot:
            #print("hello")
            i += 1

        elif A[j] >= pivot:
            j -=1

        else :
            swap(A,i,j)
            i += 1
            j -= 1
    print(i,j)


        #print(i, j)

    A = swap(A,j,start)
    print(A)
    quick_sort_helper(A,start,j-1)
    quick_sort_helper(A,j+1,end)


B = [5,1,1,2,0,0]
#B = []
quick_sort(B)