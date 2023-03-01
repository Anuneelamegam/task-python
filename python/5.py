class Demo:#overloading
    def fun1(self):#no arguments to be passed
        print("Hello Besant Technologies")
    def fun1(self,a):#one argument to be passed
        print("The value of a is",a)
    def fun1(self,x,y):#two arguments to be passed
        print("The value of x and y",x," ",y)
d1=Demo()
d1.fun1(3,4)
d1.fun1(5,3)
d1.fun1(45,78)
#Overriding
class Car:
    def run(self):
        print("Car is Running")
class Bike(Car):
    def run(self):
        print("Bike is Running")
b1=Bike()
b1.run()
b1.run()
