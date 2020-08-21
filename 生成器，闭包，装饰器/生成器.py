
#生成器
#函数中出现yield，不能再当成普通函数，而是生成器

def CreateNum():
	print("start")
	a, b = 2, 1
	for i in range(5):
		print("1")
		yield b
		a, b = b, a+b
		print("2")
	print("stop")

a=CreateNum()
next(a)
next(a)
next(a)
