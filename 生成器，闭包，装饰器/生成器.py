#斐波拉契数列,除了前2个，其他数等于前两个数之和

#函数中出现yield，不能再当成普通函数，而是生成器

def CreateNum():
	print("start")
	a, b = 1, 1
	for i in range(20):
		yield b
		a, b = b, a+b
	print("stop")

a=CreateNum()
print(next(a))
print(next(a))
print(next(a))
print(next(a))
print(next(a))
print(next(a))