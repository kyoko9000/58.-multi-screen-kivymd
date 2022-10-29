import threading


def run_threading():
    for i in range(5):
        t1 = threading.Thread(target=result_thread, args=(i, "ok"))
        t1.start()


def result_thread(thread_num, data):
    print(thread_num, data)


run_threading()
