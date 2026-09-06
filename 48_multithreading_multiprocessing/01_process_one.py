import threading
import time


def cpy_heavy():
    
    print(f"Crunching some values..")
    total = 0
    for i in range(100000000):
        total +=i
    
    print("Process done..")

starttime = time.time()

t1 = [threading.Thread(target=cpy_heavy) for _ in range(2)]
    

[t11.start() for t11 in t1]
[t11.join() for t11 in t1]

endtime = time.time()


print( f"Time diff = {(endtime- starttime):.2f}")

        