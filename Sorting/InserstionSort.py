

def InserstionSort(A):
    for i in range(1,len(A)):
        point = A[i]
        j = i -1
        while j >=0 and A[j] > point:
            A[j+1] = A[j]
            j -= 1
        A[j + 1] = point

    return A




