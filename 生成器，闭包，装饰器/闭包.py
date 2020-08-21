def test(number1):
    print("--1--")

    def test_in(number2):
        print("--2--")
        print(number1 + number2)

    print("--3--")
    return test_in


ret = test(100) #ret指向test_in
ret(1)    #1赋值给number2
ret(100)