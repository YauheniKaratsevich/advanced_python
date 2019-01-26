import threading
import time


sem = threading.Semaphore()

even, odd = 0, 1
i = 0


def counter(thread_name, parity):
    global i
    while i < 100:
        sem.acquire()
        if (i % 2) == parity:
            print("{}\t- {}".format(thread_name, i))
            i = i + 1
            time.sleep(0.1)
        sem.release()


if __name__ == "__main__":
    cs1 = threading.Thread(target=counter, args=("ThreadEven", even,))
    cs1.start()
    cs2 = threading.Thread(target=counter, args=("ThreadOdd", odd,))
    cs2.start()
