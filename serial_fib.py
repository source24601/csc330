import time

def fib(n):
    if n <= 1:
        return n
    return fib(n - 1) + fib(n - 2)

numbers = [35, 36, 37, 38, 39]

startTime = time.perf_counter()

for number in numbers:
    fib_value = fib(number)
    print("fib(" + str(number) + ") =", fib_value)

endTime = time.perf_counter()
totalTime = endTime - startTime

print()
print("Total time:", totalTime, "seconds")
