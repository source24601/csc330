import os
import time

def fib(n):
    if n <= 1:
        return n
    return fib(n - 1) + fib(n - 2)

numbers = [35, 36, 37, 38, 39]

startTime = time.perf_counter()

children = []

for number in numbers:
    pid = os.fork()

    if pid == 0:
        result = fib(number)
        print(f"fib({number}) = {result}")
        os._exit(0)
    else:
        children.append(pid)

for c in children:
    os.wait()

endTime = time.perf_counter()
totalTime = endTime - startTime

print("Total time:", totalTime, "seconds")
