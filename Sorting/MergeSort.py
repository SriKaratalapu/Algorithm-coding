
def MergeSort(A):
    return MergeHelperSort(A)

def Merge(A,left,right):
    i = 0
    j = 0
    aux = []

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            aux.append(left[i])
            i +=1
        else:
            aux.append(right[j])
            j +=1

    while i < len(left):
        aux.append(left[i])
        i +=1
    while j < len(right):
        aux.append(right[j])
        j +=1
    A = aux
    return A

def MergeHelperSort(A):

    if len(A) <= 1 :
        return A

    left = MergeHelperSort(A[:len(A)/2])
    right = MergeHelperSort(A[len(A)/2:])
    return Merge(A,left,right)

B = [6,5,1,0]
print(MergeSort(B))