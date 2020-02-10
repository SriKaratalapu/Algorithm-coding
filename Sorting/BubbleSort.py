'''
Creating a Bubble sort algorithm using the while iterative for loop
'''

def BubbleForSort(A):
    for iter in range(0,len(A)):# No. of iterations is equal to the length of the array

        for  i in range(0,len(A)):# Scanning through the array to swap adjacent elements
            j = i + 1
            if j < len(A):
                # Scanning through the array to swap adjacent elements
                if  A[i] > A[j]:
                    temp = A[i]
                    A[i] = A[j]
                    A[j] = temp
    return A

'''
Creating a Bubble sort algorithm using the while iterative for loop
'''
def BubbleWhileSort(A):
    iter =0
    while iter  < len(A):# No. of iterations is equal to the length of the array
        i = 0
        while i < len(A): # Scanning through the array to swap adjacent elements
            j = i + 1
            if j < len(A):
                # Scanning through the array to swap adjacent elements
                if  A[i] > A[j]:
                    A[i],A[j] = A[j],A[i]
            i +=1
        iter +=1
    return A



B = [ 7,3,5,2,8]
print(BubbleWhileSort(B))