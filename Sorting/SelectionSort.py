
'''
Creating a Selecion sort algorithm using the for iterative loop
'''


def SelectionForSort(A):
    for i in range(0,len(A)):
        min = i # initialize the min index
        for j in range (i+1, len(A)):
            if A[min] > A[j]:
                min = j # Update new min index
        temp = A[i] # Save Current min value in a temporary variable
        # Swap the current min value with the new min value
        A[i] = A[min]
        A[min] = temp

    return A

'''
Creating a Selecion sort algorithm using the while iterative for loop
'''

def SelectionWhileSort(A):
    i = 0
    while i < len(A):
        min = i # initialize the min index
        j = i+1
        while j < len(A):
            if A[min] > A[j]:
                min = j # Update new min index
            j += 1
        temp = A[i]# Save Current min value in a temporary variable
        # Swap the current min value with the new min value
        A[i] = A[min]
        A[min] = temp
        i += 1
    return A




