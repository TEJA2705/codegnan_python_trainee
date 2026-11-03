'''
A class contains attribute,variables, and methods or functions that can manipulate the
data

-> A class is blueprint of an object
-> An object is an initation of a class
-> Methods are functions defined inside the body of the class
'''
#Four Pillars of oops
'''
-> polymorphism
   1.Operator overlodaing
   2.operator overriding
   3.method overloading
   4.method overriding

-> Inheritance
   1.single
   2.mutlilevel
   3.hierarichal
   4.multiple
   5.hybrid
   and super()

-> Encpasulation
   1.public
   2.private
   3.protected data

-> Abstarction
   1.abstract clas
   2.abstract method
'''
#syntax
'''
class classname():
    #attribute

    def fun_name():
        #
a=classname()
a.fun_name()
'''

#class Declaration
'''class Details():
    name="teja"
    age=21
    place="nbr"
    def display(self):
        print(self.name,self.age,self.place)
d=Details()
print(dir(d))
d.display()'''

#object instatiation
'''class Details():
    def data(self,name,age,place):
        self.name=name
        self.age=age
        self.place=place
    def display(self):
        print(self.name,self.age,self.place)
a=Details()
print(dir(a))
a.data("teja",21,"vja")
a.display()'''

'''class Details():
    def data(self,name,age,place):
        self.name=name
        self.age=age
        self.place=place
    def display(self):
        print(self.name,self.age,self.place)
a=Details()
b=Details()
#print(dir(a))
a.data("teja",21,"vja")
a.display()
b.data("Durga",21,"gnt")
b.display()'''


'''class Details():
    def data(self,name,age,place):
        self.name=name
        self.age=age
        self.place=place
    def display(self):
        print(self.name,self.age,self.place)
a=Details()
#b=Details()
#print(dir(a))
a.data("teja",21,"vja")
a.display()
a.data("Durga",21,"gnt")
a.display()'''

#object Intilization
# __init__
'''class Details():
    def __init__(self,name,age,place):
        self.name=name
        self.age=age
        self.place=place
    def display(self):
        print(self.name,self.age,self.place)
a=Details("teja",21,"vja")
print(dir(a))
a.display()'''

'''class Details():
    def __init__(self,name,age,place):
        self.name=name
        self.age=age
        self.place=place
    def display(self):
        print(self.name,self.age,self.place)
name=input("Enter Name: ")
age=int(input("Enter age: "))
place=input("Enter Place: ")
a=Details(name,age,place)
#print(dir(a))
a.display()'''

#diff btw _ and __
'''
-> User wants to create a variable in python with '__ ' double leading underscore our
python interpreter treats as a special variable and avoid name conflicts with
methods and inner class
'''

'''class Employee1():
    def __init__(self):
        self.name="teja"
        self._mailid="vkdteja02@gamil.com"
        self.__salary=10000#private variable
a=Employee1()
print(dir(a))
print(a.name)
print(a._mailid)
#print(a.__salary)
print(a._Employee1__salary)'''


'''class Employee1():
    def __init__(self,name,mailid,salary):
        self.name=name
        self._mailid=mailid
        self.__salary=salary#private variable
    def display(self):
        print(f"{self.name}: {self.__salary}")
a=Employee1("Teja","vkd@gmail.com",10000)
b=Employee1("Durga","d@gmail.com",20000)
print(dir(a))
print(dir(b))
print(a._Employee1__salary)
print(b._Employee1__salary)
a.display()
b.display()'''


'''class Employee1():
    def __init__(self):
        self.name="teja"
        self._mailid="vkdteja02@gamil.com"
        self.__salary=10000#private variable
class Employee2():
    def __init__(self):
        self.name="Durga"
        self._mailid="dteja02@gamil.com"
        self.__salary=20000#private variable
a=Employee1()
b=Employee2()
print(dir(a))
print(dir(b))
print(a.name)
print(a._mailid)
#print(a.__salary)
print(a._Employee1__salary)
print(b.name)
print(b._mailid)
#print(b.__salary)
print(b._Employee2__salary)'''


#polymorphism
#Operator overloading->same operator behaves different based on data types of variable

'''a,b=2,4
print(a+b)
print(a.__add__(b))
print(a.__add__(8))
print(a.__sub__(1))
print(a.__mul__(5))
#print(a.__div__(2)) div operator not present
print(a.__pow__(4))
print(a.__ge__(10))
print(a.__le__(20))


a=[1,2,3,4,5];b=[6,7,8,9,10]
print(a.__add__(b))
print(a.__getitem__(3))
print(a.__getitem__(4))


a,b="code","gnan"
print(a.__add__(b))
a="python";b="course"
print(a.__add__(" "+b).title())
print("teja".__add__("v"))'''


#Operator Overriding
'''class A():
    def __init__(self,a):
        self.a=a
    def __add__(self,value):
        return self.a*value.b
class B():
    def __init__(self,b):
        self.b=b
x=A(10)
y=B(20)
print(x+y)'''

#method Overloading
'''class new():
    def sum(self,a=None,b=None,c=None):
        if a!=None and b!=None and c!=None:
            print("Sum: ",a+b+c)
        elif a!=None and b!=None:
            print("Product: ",a*b)
        else:
            print("Program ends..")
n=new()
n.sum()
n.sum(2,3,4)
n.sum(5,4)'''

'''class new():
    def sum(self,a=3,b=4,c=5):
        if a!=2 and b!=3 and c!=4:
            print("Sum: ",a+b+c)
        elif a!=5 and b!=6:
            print("Product: ",a*b)
        else:
            print("Program ends..")
n=new()
n.sum(2,3,4)
n.sum(5,4)
n.sum()'''

#method overriding
'''class Animal():
    def speak(self):
        print("Animal can make sounds")
class Dog():
    def speak(self):
        print("Dog Brakes")
a=Animal()
b=Dog()
a.speak()
b.speak()'''

'''class dream():
    def vehicle(self):
        print("Honda Dream Yuga 110")
class passion():
    def vehicle(self):
        print("Hero Passion Pro 110")
d=dream()
p=passion()
d.vehicle()
p.vehicle()'''


#Inheritance
'''
                               Inheritance
                                    |
        ----------------------------------------------------------
        |            |              |           |                |
        single    multiple      multilevel     hybrid       Hierarichal
        
        |            |              |           |                |
    one parent    Two Parent    grandparent   multiple,    one parent
    one child     one child    parent,child   hierarichal    more child

'''                              
                                  
#single-Inheritance
'''class RBI():
    cash=100000
    def available_cash(cls):
        print("available cash is",cls.cash)
        print("available cash is",RBI.cash)
class SBI(RBI):
    pass
class HDFC(RBI):
    cash=50000
    def new_cash(cls):
        print("new cash is",cls.cash+cls.cash)
        print("new cash is",cls.cash+RBI.cash)
a=HDFC()
a.available_cash()
a.new_cash()'''


#multiple Inheritance
'''class Father():
    height=6.0
    def hei(self):
        print("Height: ",self.height)
class Mother():
    weight=93
    def wei(self):
        print("Weight: ",self.weight)
class kid(Father,Mother):
    dob='02-07-2005'
a=kid()
a.wei()
a.hei()
print(a.dob)'''

#multilevel Inheritance
'''class GrandParent():
    acres=5
    def land(self):
        print("Acres: ",self.acres)
class Parent(GrandParent):
    sqt='2000sqt'
    def house(self):
        print("Sqt: ",self.sqt)
class Child(Parent):
    car="BMW"
    def name(self):
        print("Car Name: ",self.car)
c=Child()
c.name()
c.house()
c.land()'''


#hierarichal-> one parent class is inherited by more child classes
'''class Employee():
    company="Codegnan"
    def com(self):
        print("Comapny: ",self.company)
class Trainer(Employee):
    teacher="pooja"
    def tea(self):
        print("Comapny: ",self.teacher)
class Developer(Employee):
    dev="Teja"
    def deve(self):
        print("Comapny: ",self.dev)
t=Trainer()
d=Developer()
t.tea()
t.com()
d.deve()
d.com()'''

#hybrid Inheritance-> Hybrid Inheritance combining one or more than one type of
#inheritance example hierarichal + multiple
'''class Trainer():
    def teach(self):
        print("Teach Classes")
class Developer(Trainer):
    def code(self):
        print("Writing Code")
class Student(Trainer):
    def study(self):
        print("Learning Classes")
class Program_Manager(Developer,Student):
    def work(self):
        print("Managing the work")
p=Program_Manager()
d=Developer()
s=Student()
p.work()
p.code()
p.study()
p.teach()
d.code()
d.teach()
s.study()
s.teach()'''

#Library Mangement System-oops
'''
1.add book  -> adding books
2.list of books->Display
3.issue book -> Issue book
4.delete book -> delete book
5.Return Book -> exit

'''


#super() -> It refers to parent class methods and attribute
'''class parent():
    def __init__(self,name):
        self.name=name
        print("Parent Method")
class child(parent):
    def __init__(self,name,city):
        super().__init__(name)
        self.city=city
        print("Child Method")
a=child("Teja","Vja")
print(a.name)
print(a.city)'''


#Encapsulation -> combining multiple units into single unit
#public variable
'''class A():
    public=10
    def method1(self):
        print(self.public)
class B(A):
    def method2(self):
        print(self.public)
b=B()
b.method1()
b.method2()'''


#Protected variable
'''class A():
    _protect=100
    def method1(self):
        print(self._protect)
class B(A):
    def method2(self):
        print(self._protect)
b=B()
b.method1()
b.method2()
print(b._protect)'''


#private variable
'''class A():
    __private=20
    def method1(self):
        print(self.__private)
class B(A):
    def method2(self):
        print(self._A__private)
b=B()
b.method1()
b.method2()

a=A()
print(b._A__private)
print(a._A__private)'''


#Abstraction
'''
Hiding unnessary information from the user is called abstraction
'''
#Abstract Class
'''one or more abstract methods is called abstract class"

Abstract method -> a method is declared without implementation is called abstract method
'''

'''class A():
    def method1(self):
        pass
a=A()
a.method1()'''


'''class A():
    def method1(self):
        print("data")
a=A()
a.method1()'''



'''from abc import ABC,abstractmethod
class A(ABC):
    @abstractmethod
    def method1(self):
        print("python")
a=A()
a.method1()'''#error


'''from abc import ABC,abstractmethod
class A(ABC):
    @abstractmethod
    def method1(self):
        pass
    def method2(self):
        print("Method")
    @abstractmethod
    def method3(self):
        pass
class B(A):
    def method1(self):
        print("Method1 is implemeted")
    def method3(self):
        print("Method3 is implemeted")
a=B()
a.method1()
a.method2()
a.method3()'''
    
