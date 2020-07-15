# -*- coding:utf:8 -*-
import re

print('请输入一组数字：')
values = input()
k = values.split(",")
k = re.findall(r'[0-9]+', values)
t = tuple(k)
print(k)
print(t)
