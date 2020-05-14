'''
Creating a Bubble sort algorithm using the while iterative for loop
'''


'''
Creating a Bubble sort algorithm using the while iterative for loop
'''
def BubbleSort(A):
    if len(A) == 0 or len(A) ==1:
        return A
    for i in range(len(A)):
        j = 0
        while j < len(A)- i -1:
            print(i,A,j)
            if A[j] > A[j+1]:
                A[j],A[j+1] = A[j+1],A[j]
                j +=1
            else:
                j +=1
    return A







B = [ 7,3,5,2,8]
print(BubbleSort(B))