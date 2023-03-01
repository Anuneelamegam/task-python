# constructor and method overloading
class test:
    def __init__(self, k):
        self.x1=k
    def __init__(self,l,k):
        self.x1=l
        self.x2=k
    def f(self):
        print("this is method")
        print(self.x1+self.x2)
ob1=test(1,5)
ob1.f()
