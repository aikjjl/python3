# https://www.cnblogs.com/finer/p/12846475.html

print("一行代码实现1--100之和")
print(sum(range(1, 101)))

print("如何在一个函数内部修改全局变量")
a = 5


def fn():
    global a
    a = 4


fn()
print(a)

print("列出5个python标准库")
# os：提供了不少与操作系统相关联的函数
# sys:   通常用于命令行参数
# re:   正则匹配
# math: 数学运算
# datetime:处理日期时间

print("#字典如何删除键和合并两个字典")

# del和update方法
dic = {"name": "zhs", "age": 18}
del dic["name"]
print(dic)
dic2 = {"name": "ls"}
dic.update(dic2)
print(dic)

print("#谈下python的GIL")

# GIL 是python的全局解释器锁，同一进程中假如有多个线程运行，一个线程在运行python程序的时候会霸占python解释器（加了一把锁即GIL），使该进程内的其他线程无法运行，
# 等该线程运行完后其他线程才能运行。如果线程运行过程中遇到耗时操作，则解释器锁解开，使其他线程运行。所以在多线程中，线程的运行仍是有先后顺序的，并不是同时进行。
# 多进程中因为每个进程都能被系统分配资源，相当于每个进程有了一个python解释器，所以多进程可以实现多个进程的同时运行，缺点是进程系统资源开销大


print("python实现列表去重的方法")
# 先通过集合去重，在转列表
lis = [1, 23, 43, 545, 4, 5, 5, 5, 5, 5]
a = set(lis)
a = [x for x in a]
print(a)
print(type(a))

print("fun(*args,**kwargs)中的*args,**kwargs什么意思？")

print("python2和python3的range（100）的区别")
# python2返回列表，python3返回迭代器，节约内存


print("简述面向对象中__new__和__init__区别")


class bike:
    def __init__(self, newNum, newcolor):  # __init__方法自动被调用，可以创建对象接收参数
        self.Num = newNum
        self.color = newcolor

    def move(self):
        print("车会跑")


a = bike(2, 'black')
print(a.Num)
print(a.color)

'''
1、__new__至少要有一个参数cls，代表当前类，此参数在实例化时由Python解释器自动识别
2、__new__必须要有返回值，返回实例化出来的实例，这点在自己实现__new__时要特别注意，可以return父类（通过super(当前类名, cls)）__new__出来的实例，或者直接是object的__new__出来的实例
3、__init__有一个参数self，就是这个__new__返回的实例，__init__在__new__的基础上可以完成一些其它初始化的动作，__init__不需要返回值

4、如果__new__创建的是当前类的实例，会自动调用__init__函数，通过return语句里面调用的__new__函数的第一个参数是cls来保证是当前类实例，
如果是其他类的类名，那么实际创建返回的就是其他类的实例，其实就不会调用当前类的__init__函数，也不会调用其他类的__init__函数。

'''
print(id(bike))


class A(object):
    def __init__(self):
        print("这是init方法", self)

    def __new__(cls, *args, **kwargs):
        print("这是cls的ID", id(cls))
        print("这是new方法", object.__new__(cls))
        return object.__new__(bike)


A()
print(id(A))

'''
print("简述with方法打开处理文件帮我我们做了什么？")
f=open("./test1.py","wb")
try:
    f.write("hello world")
except:
    pass
finally:
    f.close()
'''
'''
打开文件在进行读写的时候可能会出现一些异常状况，如果按照常规的f.open
写法，我们需要try,except,finally，做异常判断，并且文件最终不管遇到什么情况，都要执行finally f.close()关闭文件，with方法帮我们实现了finally中f.close

'''

print(
    "列表[1,2,3,4,5],请使用map()函数输出[1,4,9,16,25]，并使用列表推导式提取出大于10的数，最终输出[16,25],\nmap（）函数第一个参数是fun，第二个参数是一般是list，第三个参数可以写list，也可以不写，根据需求")

lis = [1, 2, 3, 4, 5]


def fn(x):
    return x ** 2


re = map(fn, lis)
re = [i for i in re if i > 10]
print(re)

print("python中生成随机整数、随机小数、0--1之间小数方法")
import random

print(random.randint(0, 1000))
import numpy as np

print(np.random.randn(5))  # 5个随机小数
print(random.random())  # 0-1随机小数

print("避免转义给字符串加哪个字母表示原始字符串？\nr , 表示需要原始字符串，不转义特殊字符")

print("用正则匹配出标签里面的内容（“中国”），其中class的类名是不确定的")
import re

str = '<div class="name">中国</div>'
res = re.findall(r'<div class=".*">(.*?)</div>', str)
print(res)

print("assert（）方法，断言成功，则程序继续执行，断言失败，则程序报错")
a = 1
assert (a > 0)
# assert (a>2)


print("列出python中可变数据类型和不可变数据类型，并简述原理")
print("不可变数据类型：数值型、字符串型string和元组tuple")
# 不允许变量的值发生变化，如果改变了变量的值，相当于是新建了一个对象，而对于相同的值的对象，在内存中则只有一个对象（一个地址）
a = 1
b = 1
print(id(a))
print(id(b))
b = 2
print(id(b))
# 可变数据类型：列表list和字典dict；
# 允许变量的值发生变化，即如果对变量进行append、+=等这种操作后，只是改变了变量的值，而不会新建一个对象，变量引用的对象的地址也不会变化，
# 不过对于相同的值的不同对象，在内存中则会存在不同的对象，即每个对象都有自己的地址，相当于内存中对于同值的对象保存了多份，这里不存在引用计数，是实实在在的对象。


print("s = ajldjlajfdljfddd，去重并从小到大排序输出adfjl")
# set去重，去重转成list,利用sort方法排序，reeverse=False是从小到大排
a = "ajldjlajfdljfddd"
a = set(a)
a = list(a)
print(type(a))
print(a)
a.sort(reverse=False)
print(a)
print("".join(a))

print("用lambda函数实现两个数相乘")
sum = lambda a, b: a * b
print(sum(5, 6))

print("字典根据键从小到大排序")
dic = {"name": "zs", "age": "18", "city": "深圳", "tel": "1111"}
print(dic.items())
lis = sorted(dic.items(), key=lambda i: i[0], reverse=False)
print(lis)
print(dict(lis))

print("利用collections库的Counter方法统计字符串每个单词出现的次数kjalfj;ldsjafl;hdsllfdhg;lahfbl;hl;ahlf;h")
from collections import Counter

a = "kjalfj;ldsjafl;hdsllfdhg;lahfbl;hl;ahlf;h"
res = Counter(a)
print(res)

print("正则")
# 字符串a = "not 404 found 张三 99 深圳"，每个词中间是空格，用正则过滤掉英文和数字，最终输出"张三  深圳"
import re

a = "not 404 found 张三 99 深圳"
lis = a.split(" ")
print(lis)
res = re.findall('\d+|[a-zA-Z]+', a)
print(res)
for i in res:
    if i in lis:
        lis.remove(i)

print("".join(lis))



print("filter方法求出列表所有奇数并构造新列表，a =  [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]")
a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#filter() 函数用于过滤序列，过滤掉不符合条件的元素，返回由符合条件元素组成的新列表。该接收两个参数，第一个为函数，第二个为序列，
# 序列的每个元素作为参数传递给函数进行判，然后返回 True 或 False，最后将返回 True 的元素放到新列表

def fn(a):
    return a % 2 == 1

newlis = filter(fn, a)
newlis = [i for i in newlis]
print(newlis)

res=[i for i in newlis if i%3==0]
print(res)



print("两个列表[1,5,7,9]和[2,2,6,8]合并为[1,2,2,3,6,7,8,9]")
lis1=[1,5,7,9]
lis2=[2,2,3,3,4,6,10]
lis1.extend(lis2)
print(lis1)
lis1.sort(reverse=False)
print(lis1)



'''for i in a ,每个i是【1,2】，【3,4】，【5,6】，for j in i，每个j就是1,2,3,4,5,6,合并后就是结果'''
a=[[1,2],[3,4],[5,6],[7,8]]
x=[j for i in a for j in i]
print(x)

#还有更骚的方法，将列表转成numpy矩阵，通过numpy的flatten（）方法
import numpy as np
b=np.array(a).flatten().tolist()
print(b)



#x="abc",y="def",z=["d","e","f"],分别求出x.join(y)和x.join(z)返回的结果,参考os.path.join()方法，拼接路径经常用到，也用到了join,和字符串操作中的join有什么区别
x="abc"
y="xyz"
print(x.join(y))
z=["d","e","f"]
print(x.join(z))




'''
48、提高python运行效率的方法

1、使用生成器，因为可以节约大量内存

2、循环代码优化，避免过多重复代码的执行

3、核心模块用Cython  PyPy等，提高效率

4、多进程、多线程、协程

5、多个if elif条件判断，可以把最有可能先发生的条件放到前面写，这样可以减少程序判断的次数，提高效率
'''
