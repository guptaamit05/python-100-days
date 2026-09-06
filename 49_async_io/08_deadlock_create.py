import threading
import time

lock_1 = threading.Lock()
lock_2 = threading.Lock()


def task1():
    with lock_1:
        print("TASK_1 taking lock 1111")
        with lock_2:
            print("TASK_1 taking lock 2222")


def task2():
    with lock_2:
        print("TASK_2 taking lock 2222222222222222")
        with lock_1:
            print("TASK_2 taking lock 111111")


t1 = threading.Thread(target=task1)
t2 = threading.Thread(target=task2)


t1.start()
t2.start()