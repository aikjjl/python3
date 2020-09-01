print("斐波拉契数列,除了前2个，其他数等于前两个数之和")


# 函数中出现yield，不能再当成普通函数，而是生成器

def CreateNum():
    print("start")
    a, b = 1, 1
    for i in range(20):
        yield b
        a, b = b, a + b
    print("stop")


a = CreateNum()
# 调用方式
print(next(a))
print(a.__next__())

print("------send和next对比-------------")
print("第一次调用，不能用send，或者send(None)")

def test1():
    i = 0
    while i < 5:
        temp = yield i
        print(temp)
        i += 1


t = test1()
print(next(t))         #第一次yield，暂停，返回i=0
print(t.__next__())    #从第一次暂停开始，temp未接收任何值，故为None，i=1,返回i=1
print(t.__next__())    #从第二次暂停开始，temp未接收任何值，故为None，i=1,返回i=2
print(t.send("haha"))  #temp接收haha
print(t.send("aaa"))



print("-----------------多任务，协程-----------")
def test2():
	while True:
		print("1")
		yield None

def test3():
	while True:
		print("2")
		yield None

t2=test2()
t3=test3()
while True:
	t2.__next__()
	t3.__next__()