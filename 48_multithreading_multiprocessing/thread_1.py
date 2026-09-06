import threading
import time


def boiling_milk():
    print("Boiling milk")
    time.sleep(2)
    print("milk boiled...")


def toasting_bun():
    print("toasting start..")
    time.sleep(3)
    print("done with toasting bun...")
    
    
thread1 = threading.Thread(target=boiling_milk, name="Boiling..")
thread2 = threading.Thread(target=toasting_bun, name="Toasting..")


starttime= time.time()
print("Time started: ", starttime)
thread1.start()
thread2.start()

thread1.join()
thread2.join()

endtime= time.time()
print("End Thread process. ", endtime)


print("Process taken time: === ", endtime-starttime)
