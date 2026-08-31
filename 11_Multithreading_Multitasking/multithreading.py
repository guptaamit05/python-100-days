
import threading
import time

def print_numbers():
    for i in range(5):
        time.sleep(1)
        print("Number:",i)
        
def print_letters():
    for letter in 'abcdefghi':
        time.sleep(1)
        print("Letters:",letter)

# creating two thread...
t1 = threading.Thread(target=print_numbers)
t2 = threading.Thread(target=print_letters)
t = time.time()
# print_numbers()
# print_letters()
t1.start()
t2.start()

### wait thread to complete
t1.join()
t2.join()
finished_time = time.time() - t

print("Finished_ time: ", finished_time)