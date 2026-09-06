chais = {"ginger": 22.34, "cold-coffee": 45.33, "hot-chocolage": 100}


# try:
#     print("Chai found...", chais['testy'])
# except KeyError:
#     print("KeyError: The key that you are trying to access not exist..")
# ----------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------


# class InvalidChaiError(Exception):
#     pass


# def bill(flavor, cups):

#     menu = {"ginger": 12.3, "masala": 45}
#     try:
#         if flavor not in menu:
#             raise InvalidChaiError("That chai is not avaialble")

#         if not isinstance(cups, int):
#             raise TypeError("Number of cups must be an integer.")

#         total = cups * menu[flavor]
#         print(f"Your bill for you cup of order {cups}*{menu[flavor]} = {total} : ")

#     except Exception as e:
#         print("Error: ", e)


# bill("ginger", 10)
# bill("testy cold", "two")
# bill("masala", "three")
# ----------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------

# try:
#     file = open("abc.txt", 'r')
#     content = file.read()
#     print(content)

# except NameError as e:
#     print("Error:",e)
# except FileNotFoundError as e:
#     print("File not found", e)

# finally:
#     file.close()

# ----------------------------------------------------------------------------------------
# ----------------------------MultiThreding and Multiprocessing------------------------------


# # MultiThreding
# from threading import Thread
# import time

# def take_order():
#     for i in range(1,5):
#         print(f"Taking order or {i} user")
#         # complex task do...
#         time.sleep(1)

# def brew_tea():
#     for i in range(1,5):
#         print(f"Brewing chai {i} user")
#         time.sleep(2)

# t1 = Thread(target=take_order)
# t2 = Thread(target=brew_tea)

# t1.start()
# t2.start()

# t1.join()
# t2.join()

# print("all thread done now...")
# =========================================================
# Multiprocessing

from multiprocessing import Process
import time


def serve_tea(name):
    print(f"Serving the tea...{name}")
    time.sleep(2)
    print(f"Start tea preparint.. for {name}")

chai_makers = [
    Process(target=serve_tea, args=(f"Chai Maker  #{i + 1}",)) for i in range(3)
]

for p in chai_makers:
    p.start()

for p in chai_makers:
    p.join()

print("All proces has been completed..")
