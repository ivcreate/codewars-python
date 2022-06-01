fib_arr = [0,1] + [0]*99

def fib(n):
    if n <= 1:
        return n
    return fib(n-1) + fib(n-2)


for i in range(2, 101):
    fib_arr[i] = fib_arr[i-1] + fib_arr[i-2]

def test():
    print("test #1: ", end="")
    if fib(4) == fib_arr[4]:
        print("OK")
    else:
        print("Fail")

    print("test #2: ", end="")
    if fib(10) == fib_arr[10]:
        print("OK")
    else:
        print("Fail")

test()
