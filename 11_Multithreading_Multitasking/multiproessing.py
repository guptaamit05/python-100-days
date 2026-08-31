import multiprocessing

## When to use it:
## 1) CPU bound task (heavy task)
## 2) parallel execution: multiple cores of CPU


import time
def square_numbers():
    for i in range(5):
        time.sleep(1)
        print(f"Square : {i*i}")

def cube_numbers():
    for i in range(5):
        time.sleep(1.5)
        print(f"Cubes : {i*i*i}")
    
if __name__ == '__main__':
    
    p1 = multiprocessing.Process(target=square_numbers)
    p2 = multiprocessing.Process(target=cube_numbers)

    t = time.time()
    ## start the process...
    p1.start()
    p2.start()

    ## wait for process to complete
    p1.join()
    p2.join()
    finished_time = time.time()- t
    print("finished time: ", finished_time)


