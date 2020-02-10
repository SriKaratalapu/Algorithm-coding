
def Fibonacci(n):
    #print(n)
    if n == 0 or n ==1:
        return 1
    else:
        return Fibonacci(n-1) + Fibonacci(n-2)


def FibonacciDyn(n):
    c1 = 0
    c2 = 1
    i = 0
    mem = [0,1]
    while i < n :
        sum =  c1 + c2
        c1 = c2
        c2 = sum
        print(sum)
        i += 1
    return(sum)


print(FibonacciDyn(3))
print(Fibonacci(3))
