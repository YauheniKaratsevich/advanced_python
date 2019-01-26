from multiprocessing import Process
from multiprocessing import Value
import time


def counter(thread_name, parity, q):
    while q.value < 101:
        if (q.value % 2) == parity:
            print("{}\t- {}".format(thread_name, q.value))
            q.value = q.value + 1
        time.sleep(0.1)


if __name__ == "__main__":
    q = Value('i', 0)

    even, odd = 0, 1
    jobs = [Process(target=counter, args=("ProccesEven", even, q)),
            Process(target=counter, args=("ProcessOdd", odd, q))]

    for x in jobs:
        x.start()

    for x in jobs:
        x.join()
