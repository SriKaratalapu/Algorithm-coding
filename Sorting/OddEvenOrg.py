"""
You are given an integer array arr, of size n. Group and rearrange them (in-place) into evens and odds in such a way that group of all even integers appears on the left side and group of all odd integers appears on the right side.

"""

def odd_even_reorg(arr):
    odd_even_helper(arr,0,len(arr)-1)
    return arr

def swap(arr,index1,index2):
    arr[index1],arr[index2] = arr[index2],arr[index1]

def odd_even_helper(arr,start,end):
    if start >= end :
        return
    while start <= end:
        if arr[start] % 2 == 0:
            start += 1
        elif arr[end]%2 ==1:
            end -= 1
        elif arr[start]%2 == 1 and arr[end]%2 == 0:
            swap(arr,start,end)
            start += 1
            end -= 1

arr = [1,3,5,7,8,9]
print(odd_even_reorg(arr))