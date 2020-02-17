

def InsertionSort(A):
    for i in range(1,len(A)):
        point = A[i]
        j = i -1
        while j >=0 and A[j] > point:
            A[j+1] = A[j]
            j -= 1
        A[j + 1] = point

    return A


def InsertionRecurSort(A):
    InsertionRecurHelperSort(A,1)

def InsertionRecurHelperSort(A,i):
    if i == len(A):
        print A
        return
    Temp = A[i]
    j = i - 1
    while j >=0 and A[j] > Temp:
        A[j+1] = A[j]
        print(A)
        j -= 1
    A[j+1] = Temp
    InsertionRecurHelperSort(A,i+1)

B = [7,2,4,1,5,3]
InsertionRecurSort(B)