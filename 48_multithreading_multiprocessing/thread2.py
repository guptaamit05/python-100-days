import threading
import time



def prepare_chai(type, wait_time):
    print(f"Preparing for {type} chai")
    time.sleep(wait_time)
    print(f" End preparing Tea: {type}")
    
    
t1 = threading.Thread(target=prepare_chai,  args=('masala', 2,))
t2 = threading.Thread(target=prepare_chai,  args=('ginger', 3,))


starttime = time.time()
t1.start()
t2.start()

t1.join()
t2.join()
endtime = time.time()

print("End Process here: ", (endtime - starttime ))

