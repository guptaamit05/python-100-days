import time

def speed_calc_decorator(func):
    
    def wrapper():
        before_exe = time.time()
        result = func()
        after_exe = time.time()
        print(f"fast_function run speed: {after_exe-before_exe}")
        return result
    return wrapper
        

@speed_calc_decorator
def fast_function():
  for i in range(1000000):
    i * i
        
@speed_calc_decorator
def slow_function():
  for i in range(10000000):
    i * i


fast_function()
slow_function()