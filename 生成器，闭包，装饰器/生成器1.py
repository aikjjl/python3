def w1(func):
    def inner():
        print("111正在验证")
        func()

    return inner

@w1
def f1():
    print("f1")

f1()