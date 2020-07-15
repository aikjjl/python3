# -*- coding:utf-8 -*-
# 可被7整除，但不是5的倍数，2000至3200(包括在内)。得到的数字应按逗号分隔的顺序打印在一行上。
a = []
for b in range(2000, 3201):
    if (b % 7 == 0) and (b / 5 != 0):
        a.append(str(b))
print(a)
