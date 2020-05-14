def findZeroSum(arr):
    # Write your code here.
    arr.sort()
    n = len(arr)
    output = []
    for i, num in enumerate(arr):
        print(i,num)
        if i > 0 and arr[i] == arr[i - 1]:
            continue
        l = i + 1
        r = n - 1


arr =  [10, 3, -4, 1, -6, 9]
findZeroSum(arr)


