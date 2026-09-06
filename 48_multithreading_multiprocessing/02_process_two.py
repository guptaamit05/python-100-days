from multiprocessing import Process
import time


def cpy_heavy():

    print(f"Crunching some values..")
    total = 0
    for i in range(100000000):
        total += i
    print("Process done..")



if __name__ == "__main__":
    
    starttime = time.time()
    processes = [Process(target=cpy_heavy) for _ in range(2)]
    [t11.start() for t11 in processes]
    [t11.join() for t11 in processes]
    endtime = time.time()
    print(f"Time diff = {(endtime - starttime):.2f}")
