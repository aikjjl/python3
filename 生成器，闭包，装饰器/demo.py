from collections import Iterator
print(isinstance([],Iterator))

a=[1,2,3,4]
b=iter(a)
print(next(b))