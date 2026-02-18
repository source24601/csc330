from multiprocessing import Process
import time

def fib(n):
    if n <= 1:
        return n
    return fib(n - 1) + fib(n - 2)


def results(n):
    value = fib(n)
    print(f"fib({n}) = {value}")


if __name__ == "__main__":

    numbers = [35, 36, 37, 38, 39]
    tasks = []
    start_time = time.time()


    for n in numbers:
        process = Process(target=results, args=(n,))
        tasks.append(process)
        process.start()

    for process in tasks:
        process.join()


    end_time = time.time()
    final_time = end_time - start_time
    print(f"Total time: {final_time}")

