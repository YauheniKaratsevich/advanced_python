import threading


even, odd = 0, 1
i = 0


def counter(thread_name, parity):
    global i
    if i > 100:
        return
    print("{}\t- {}".format(thread_name, i))
    i = i + 1
    if parity == even:
        cs2 = threading.Timer(0.1, counter, args=["ThreadOdd", odd])
        cs2.start()
    else:
        cs1 = threading.Timer(0.1, counter, args=["ThreadEven", even])
        cs1.start()


if __name__ == "__main__":
    counter("TreadEven", even)
