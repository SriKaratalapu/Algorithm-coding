
'''
Creating a Selecion sort algorithm using the for iterative loop
'''



def SelectionForSort(A):
    for i in range(0,len(A)):
        min = i # initialize the min index
        for j in range (i+1, len(A)):
            if A[min] > A[j]:
                min = j # Update new min index
        # Swap the current min value with the new min value
        A[i], A[min] = A[min], A[i]
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
        # Swap the current min value with the new min value
        A[i],A[min] = A[min],A[i]
        i += 1
    return A

'''
Creating a Selection sort algorith using recursion. Implementing the above iterative method using recursion.
Tail Recursion using the left most digit as the the min element.
'''

def SelectionRecurSort(A):
    SelectionHelperSort(A,0) # recursion helper function

def SelectionHelperSort(A,i):
    if i == len(A):
        print A
        return
    min = i
    j = i + 1
    while j < len(A):
        if A[min] > A[j]:
            min = j
        j += 1
    A[i],A[min] = A[min],A[i]
    SelectionHelperSort(A,i+1)


'''
Creating a Selection sort algorith using while. Implementing using the right most as the max element.
'''
def SelectionTDSort(A):
    i = len(A) - 1
    while i >= 0:
        max = i
        j = i - 1

        while j >= 0:
            if A[max] < A[j]:
                max = j
            j -= 1
        A[i], A[max] = A[max], A[i]
        i -= 1
    return A

'''
Creating a Selection sort algorithm using recursion. Implementing the above iterative method using recursion.
Tail Recursion using the right most digit as the the max element.
'''

def SelectionTDRecurSort(A):
    SelectionTDHelperSort(A,len(A) -1) #Recursion helper function

def SelectionTDHelperSort(A,n):
    if n == 0:
        print(A)
        return

    max = n
    j = n -1
    while j >= 0:
        if A[max] < A[j]:
            max = j
        j -= 1
    A[n], A[max] = A[max], A[n]
    SelectionTDHelperSort(A,n-1)
    return


B = [6,5,1,0]
SelectionForSort(B)