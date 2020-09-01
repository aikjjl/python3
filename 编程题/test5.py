class Input(object):
    def __init__(self):
        self.i=''

    def getString(self):
        self.s=input()

    def printString(self):
        a=self.s.upper()
        print(a)

a=Input()
a.getString()
a.printString()