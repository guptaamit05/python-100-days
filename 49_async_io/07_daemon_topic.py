import threading
import time

def monitoring_temp():
    while True:            
        print("Monitoring tea tempratrue...")
        time.sleep(3)


# t = threading.Thread(target=monitoring_temp, daemon=True)
t = threading.Thread(target=monitoring_temp)  # will run monitoring_temp code infinite...

t.start()

print("Main program is closed...")

