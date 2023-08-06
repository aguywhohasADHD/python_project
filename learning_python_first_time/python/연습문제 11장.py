print("E11-1")
class Calculator:
    a=10
    b=20
    def add(self):
        return self.a+self.b
c1=Calculator()
print(c1.add())
print("E11-3")
class Triangle:
    def __init__(self,width,height):
        self.width=width
        self.height=height
    def area(self):
        return (self.width*self.height)/2
w=int(input("삼각형 밑변의 길이를 입력하세요 : "))
h=int(input("높이를 입력하세요 : "))
t1=Triangle(w,h)
print("삼각형의 면적 : %.2f"% t1.area())
print("E11-4")
class Ladder:
    def __init__(self,width1,width2,height):
        self.width1=width1
        self.width2=width2
        self.height=height
    def area(self):
        return (self.width1+self.width2)/2*self.height
w1=int(input("사다리꼴 밑변의 길이를 입력하세요 : "))
w2=int(input("윗변의 길이를 입력하세요 : "))
h=int(input("높이를 입력하세요 : "))
ladder1=Ladder(w1,w2,h)
print("사다리꼴의 면적 : %.2f"%ladder1.area())
del w1,w2,h,ladder1,Ladder,Triangle,Calculator,t1,c1,w,h