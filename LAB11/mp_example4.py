## multi_processing_example.py

import time
import numpy as np
from concurrent.futures import ProcessPoolExecutor

def very_slow_random_generator():
    time.sleep(5)
    arr1 = np.random.randint(1,100, size=(1000,1000))
    avg = arr1.mean()
    return avg

def slow_random_generator():
    time.sleep(2)
    arr1 = np.random.randint(1,100, size=(1000,1000))
    avg = arr1.mean()
    return avg

def fast_random_generator():
    time.sleep(1)
    arr1 = np.random.randint(1,100, size=(1000,1000))
    avg = arr1.mean()
    return avg

def main_func():
    ppe = ProcessPoolExecutor(max_workers=3)
    futures = []

    futures.append(ppe.submit(fast_random_generator))
    futures.append(ppe.submit(slow_random_generator))
    futures.append(ppe.submit(very_slow_random_generator))

    print([future.result() for future in futures])

if __name__ == '__main__':
    main_func()
    
    
