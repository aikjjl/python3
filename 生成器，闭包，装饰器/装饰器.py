def w1(func):
    def inner():
        print("111正在验证")
        func()

    return inner


def w2(func):
    def inner2():
        print("222正在验证")
        func()

    return inner2


# 装饰器,执行顺序：先进行w2的装饰
@w1
@w2
def f1():
    print("f1")


def f2():
    print("f2")


# innerfunc = w1(f1)
# innerfunc()
#
# print("-------------")
# #为了保证调用f1名称不变,不修改f1代码的前提下，修改了功能
# f1=w1(f1)
# f1()

print("-------------")
# 等价于在f1()函数前加@w1------第8行添加@w1
f1()

# 装饰器的执行时间，因为f1=w1(f1)等价于@w1,所以代码执行到@w1时已经开始执行了


print("-----------------2.有参数和不定长参数的装饰")


def fc(func):
    # def fun_in(a,b):
    #     print(a+1,b+1)
    def fun_in(*args, **kwargs):
        func(*args, **kwargs)

    return fun_in


@fc
def test(a, b, c):
    print("a=%d,b=%d,c=%d" % (a, b, c))


test(1, 2, 3)

print("--------------------3.带返回值的装饰")


def fc1(func):
    def func_in():
        # func()
        a = func()
        return a

    return func_in


@fc1
def test2():
    print("test2")
    return "test2-------"


test = test2()
print(test)  # test=None是因为test指向了func_in()，但是func_in()没有返回值return,所以test=None,修改看66,67行

print("-------------------------4.通用装饰器")


def fc4(func):
    def func_in(*args, **kwargs):
        a = func(*args, **kwargs)
        return a

    return func_in


# 无参数无返回值
@fc4
def test4_1():
    print("test4_1")


# 无参数有返回值
@fc4
def test4_2():
    print("test4_2")
    return "test4_2-------"


# 有参数无返回值
@fc4
def test4_3(a):
    print("test4_3=%d" % a)


# 有参数有返回值
@fc4
def test4_4(a):
    print("test4_4=%d" % a)
    return "4444"


test4_1()

test4_2()  # 因为没有接收return值，所以无报错

test4_3(1)

a = test4_4(4)
print(a)

print("-------------------------5.带参数的装饰器")


def fcc5(arg):
    def fc5(func):
        def func_in():
            print("arg=%s" % arg)
            if arg=="haha":
                func()
                func()
            else:
                func()

        return func_in

    return fc5


@fcc5("haha")
def test5():
    print("22")

@fcc5("h")
def test6():
    print("22")

test5()
test6()
#先执行fcc5("haha")函数，然后return成fc5()的引用
#@fc5
#使用@fc5对test5进行装饰

