import time

def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)


for i in range(50, 55, 5):
    start = time.time()
    result = fibonacci(i)
    end = time.time()
    duration = end - start
    print(i, result, duration)
