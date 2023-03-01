class SBI:
    def First(self):
        print("This is SBI Bank Class")
class ICICI:
    def Second(self):
        print("This is ICICI Bank Class")
class Bank(SBI,ICICI):
    def Third(self):
        print("This is Main Bank Class")

b1=Bank()
b1.Third()
b1.Second()
b1.First()
