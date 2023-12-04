import time

X6 = 10 ** 6
X7 = 10 ** 7

def worker(num, wait, amt=X6):
    """
    A function that allocates memory over time.
    """
    frame = []

    for idx in range(num):
        frame.extend([1] * amt)
        time.sleep(wait)

    del frame

if __name__ == '__main__':
    worker(5, 5, X6)
    worker(5, 2, X7)
    worker(5, 5, X6)
    worker(5, 2, X7)
