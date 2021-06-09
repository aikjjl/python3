from multiprocessing import Process
import time


def test():
    while True:
        print("start")
        time.sleep(1)

if __name__ == '__main__':
    p = Process(target=test)
    p.start()
    p.join()    #等p进程结束后才继续后面
    while True:
        print("s2")
    time.sleep(1)