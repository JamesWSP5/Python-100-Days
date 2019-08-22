import threading, multiprocessing


def loop():
    x = 0
    while True:
        x = x ^ 1
        print(x)


# print(multiprocessing.cpu_count())

for i in range(2):
    t = threading.Thread(target=loop)
    t.start()
