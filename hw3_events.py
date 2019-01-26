import threading


even, odd = 0, 1


def counter(thread_name, x, event_for_wait, event_for_set):
    for i in range(101):
        event_for_wait.wait()
        event_for_wait.clear()
        if (i % 2) == x:
            print("{}\t- {}".format(thread_name, i))
        event_for_set.set()


if __name__ == "__main__":
    e1 = threading.Event()
    e2 = threading.Event()

    t1 = threading.Thread(target=counter, args=("ThreadEven", even, e1, e2))
    t2 = threading.Thread(target=counter, args=("ThreadOdd", odd, e2, e1))

    t1.start()
    t2.start()

    e1.set()

    t1.join()
    t2.join()
