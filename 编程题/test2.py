# -*- coding:utf-8 -*-
# 问题:编写一个可以计算给定数的阶乘的程序。结果应该以逗号分隔的顺序打印在一行上。假设向程序提供以下输入:8
a = int(input("请输入一个数"))
num = 1
for b in range(1, a + 1):
    num *= b
print(num)


def fact(x):
    if x == 0:
        return 1
    return x * fact(x - 1)


print("请输入一个数")
x = int(input())
print(fact(x))
