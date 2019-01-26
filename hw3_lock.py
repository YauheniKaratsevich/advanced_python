import threading
import time


thread_lock = threading.Lock()

i = 0
even, odd = 0, 1


def counter(thread_name, parity):
    global i
    while i < 100:
        thread_lock.acquire()
        if (i % 2) == parity:
            print("{} - {}".format(thread_name, i))
            i = i + 1
            time.sleep(0.1)
        thread_lock.release()


if __name__ == "__main__":
    th1 = threading.Thread(target=counter, args=("ThreadEven", even,))
    th2 = threading.Thread(target=counter, args=("ThreadOdd", odd,))

    th1.start()
    th2.start()
