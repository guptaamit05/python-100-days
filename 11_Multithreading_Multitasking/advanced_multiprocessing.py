## Multiprocessin with ProcessPoolExecutor.


from concurrent.futures import ProcessPoolExecutor

import time
def print_number(num):
    time.sleep(1)
    return f"Square of {num}: {num*num}"


numbers = [1,2,3,4,5]

if __name__ == '__main__':
    
    with ProcessPoolExecutor(max_workers=3) as executor:
        results =  executor.map(print_number, numbers)

    for r in results:
        print(r)