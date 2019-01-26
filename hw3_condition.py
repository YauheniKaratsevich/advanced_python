import threading

i = 0


def consumer(cv, thread_name):
    global i
    while i < 101:
        with cv:
            print("{}\t- {}".format(thread_name, i))
            i = i + 1
            cv.notify_all()
            cv.wait(1)


if __name__ == "__main__":
    condition = threading.Condition()
    cs1 = threading.Thread(target=consumer, args=(condition, "ThreadEven",))
    cs2 = threading.Thread(target=consumer, args=(condition, "ThreadOdd",))

    cs1.start()
    cs2.start()
