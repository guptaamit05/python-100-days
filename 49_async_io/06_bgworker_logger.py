import asyncio
import threading
import time


def bg_worker():
    while True:
        time.sleep(1)
        print(f"Logging  the system health...")


async def fetch_order():
    
    await asyncio.sleep(4)
    print("I have able to fetch the order... Order Fetched..")


t = threading.Thread(target=bg_worker, daemon=True)
t.start()


asyncio.run(fetch_order())

    
    
