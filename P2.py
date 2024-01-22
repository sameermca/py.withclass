# Demostrate different mathematical functions.

class mathop:
    def add(self,a,b):
        self.c=a+b
        print('Addition is',self.c)


    def sub(self,a,b):
        self.c=a-b
        print('Subtraction is',self.c)

    def mul(self,a,b):
        self.c=a*b
        print('Multiplication is',self.c)

    def div(self,a,b):
        self.c=a/b
        print('Division is',self.c)

    def divf(self,a,b):
        c=a//b
        print('Division Floor is',c)

    def mod(self,a,b):
        c=a%b
        print('Modolus is',c)

    def powe(self,a,b):
        c=a**b
        print('Power is',c)

m1 = mathop()
x=int(input('Enter the 1st Number - '))
y=int(input('Enter the 2nd Number - '))
m1.add(x,y)
m1.sub(x,y)
m1.mul(x,y)
m1.div(x,y)
m1.divf(x,y)
m1.mod(x,y)
m1.powe(x,y)