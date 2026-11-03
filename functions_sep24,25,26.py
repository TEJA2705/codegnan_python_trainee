'''
Functions
*A function is block of organised , reusable code that is used to to perform single
or multiple task
*Python gives in built functions like print , you can make your own
function also and this are called user-defined function
*Function block begins with keyword 'def' followed by the function name and
paranthesis(())
'''


'''a,b=10,20
print("Sum: ",a+b)
print("Sub: ",a-b)
print("Mul: ",a*b)
a,b=100,200
print("Sum: ",a+b)
print("Sub: ",a-b)
print("Mul: ",a*b)
a,b=1000,2000
print("Sum: ",a+b)
print("Sub: ",a-b)
print("Mul: ",a*b)'''


'''def calculation(a,b):
    print("Sum: ",a+b)
    print("Sub: ",a-b)
    print("Mul: ",a*b)
calculation(10,20)
calculation(100,200)
calculation(1000,2000)'''


'''def calculation(a,b):
    print("Int Division: ",a//b)
    print("Power: ",a**b)
    print("Modulus Divison: ",a%b)
calculation(3,2)
calculation(30,20)
calculation(23,25)'''


'''def add(a,b):
    c=a+b
    print(c)
add(2,3)'''


'''while True:
    def add():
        a=int(input("A Value: "))
        b=int(input("B Value: "))
        print(a+b)
    add()'''


'''def add():
    a=int(input("A Value: "))
    b=int(input("B Value: "))
    print(a+b)
    add()
add()'''

'''def fullname():
    fname=input("Fname: ")
    lname=input("Lname: ")
    print((fname+" "+lname).title())
fullname()'''

'''
Note:
*print just shows the human user in a console
*return is used to terminate the function and gives back the value from the
function'''

'''def mul(a,b):
    print(a*b)
mul(3,4)'''


'''def mul(a,b):
    return a*b
print(mul(5,2))'''


#print vs return
'''def cal(a,b):
    print(a+b)
    print(a-b)
    print(a*b)
cal(2,3)'''


'''def cal(a,b):
    #return a+b
    #return a-b
    #return a*b
    return a+b,a-b,a*b    
print(cal(2,3))'''


#Task
'''def calc(a,b,opt):
    if opt==1:
        print("Sum: ",a+b)
    elif opt==2:
        print("Sub: ",a-b)
    elif opt==3:
        print("Mul: ",a*b)

a=int(input("Enter A Value: "))
b=int(input("Enter B Value: "))
opt=int(input("1.Add\n2.Sub\n3.Mul\nEnter Valid Option:"))
calc(a,b,opt)'''

'''def add():
    print(a+b)
def sub():
    print(a-b)
def mul():
    print(a*b)
a=int(input("Enter A Value: "))
b=int(input("Enter B Value: "))
opt=int(input("1.Add\n2.Sub\n3.Mul\nEnter Valid Option:"))
if opt==1:
    add()
elif opt==2:
    sub()
elif opt==3:
    mul()'''


#Task
'''def func():
    person=int(input("Enter No Of Persons: "))
    amount=int(input("Enter the Amount: "))
    res=amount//person
    return res
print("Amount Per Person is: ",func())'''


'''def func():
    person=int(input("Enter No Of Persons: "))
    amount=int(input("Enter the Amount: "))
    res=amount//person
    print(f"Amount per head: {res}")
    print("Amount per person: {}".format(res))
func()'''


#keyword and positional arguments
'''def Details(id ,name,mailid):
    id,name,mailid=10,"Teja","t@codegnan.com"
    print(id,name,mailid)
Details(id="id",name="name",mailid="mailid")'''


'''def Details(id,name,mailid):
    print(id,name,mailid)
Details(id="id",name="name",mailid="mailid")
Details(id=20,name="Teja",mailid="t@codegnan.com")
Details(id=30,name="Durga",mailid="d@codegnan.com")
Details(40,"chandu",mailid="chandu@codegnan.com")
Details("teja","teja@codegnan.com",23)
Details(name="Teja",mailid="teja@codegnan.com",id=64)'''


#employee->name,salary,designation
'''def employee(name,salary,designation):
    print(name,salary,designation)
employee(name="name",salary="salary",designation="designation")
employee(name="Teja",salary=25000,designation="Manager")
employee(name="Durga",salary=30000,designation="Developer")
employee(salary=45000,name="chandu",designation="Team Lead")
employee("vijay",50000,"HR")'''

#defalut arguments
'''def grocery(item,price):
    print("item id %s"%item)
    print("price is %.2f"%price)
grocery("rice",1800)'''

'''def grocery(item="sugar",price=100):
    print("item id %s"%item)
    print("price is %.2f"%price)
grocery()'''

'''def grocery(item,price=200):
    print("item id %s"%item)
    print("price is %.2f"%price)
grocery("rice")'''

'''def grocery(item="dal",price):
    print("item id %s"%item)
    print("price is %.2f"%price)
grocery(1800)'''

#task bakery->cake,price,qty
'''def bakery(cake,price,qty):
    print("cake id %s"%cake)
    print("price is %.2f"%price)
    print("quantity %d"%qty)
grocery("choclate",1800,2)'''

'''def bakery(cake="choco lava",price=200,qty=2):
    print("item id %s"%item)
    print("price is %.2f"%price)
    print("quantity %d"%qty)
grocery()'''

'''def bakery(cake,price=500,qty=3):
    print("item id %s"%item)
    print("price is %.2f"%price)
    print("quantity %d"%qty)
grocery("lava choco")'''

'''def bakery(cake,price=200,qty):
    print("item id %s"%item)
    print("price is %.2f"%price)
    print("quantity %d"%qty)
grocery("choco")'''


#*args * -> * means unpack the values
'''a=[1,2,3,4,5,6,7]
print(a)
print(*a)'''

'''a=(1,2,3,6,78,9)
print(a)
print(*a)'''

'''a={1,2,3,4,5,6,7}
print(a)
print(*a)'''

'''a={"name":"Teja","age":21}
print(a)
print(*a)'''

'''a="codegnan"
print(a)
print(*a)'''

'''a,b,c=2,3,4,5,6,7,8,9,10
print(a)
print(b)
print(c)'''#error


'''a,b,c=2,3,4
print(a)
print(b)
print(c)'''


'''a,*b,c=2,3,4,5,6,7,8,9
print(a)
print(*b)
print(b)
print(c)'''


'''a,b,*c=2,3,4,5,6,7,8,9
print(a)
print(b)
print(*c)
print(c)'''

'''a,*b,*c=2,3,4,5,6,7,8,9
print(a)
print(*b)
print(b)
print(c)'''#multiple * won't accept

'''*a,b,c="codegnan"
print(a)
print(*a)
print(c)
print(b)'''

#variable length arguments are automatically stores in tuple and we use * argumnets
'''def check(*a):
    print(a)
    print(type(a))
check()
b=[4,5,6,7,8,9]
check(*b)
check(b)
c=(3,4,5,7)
check(*c)
d={6,7,8,9}
check(*d)
e={"year":2026,"month":"sep"}
check(*e)'''

'''def check(*a):
    d=1
    print(a)
    print(type(a))
    for i in a:
        if type(i)==str:
            continue
        d=d+i
        print(d)
check()
check(2,3,4,5,6,7)
check(2,3,4,3.4,4.2,5.3)
check(3,4,5,2,3.2,4.4,"Teja")'''


#kwargs(**)
'''def details(**a):
    print(a)
    print(type(a))
details()
d={"name":["Kanaka","Durga","Teja"],
   "marks":[70,71,72],"status":["R","M","R"]}
details(**d)'''


'''def details(**a):
    print(a)
    print(type(a))
    for i in a:
        print(i)
    for i in a.keys():
        print(i)
    for i in a:
        print(a[i])
    for i in a.values():
        print(i)
    for i in a:
        print(i,a[i])
    for i,j in a.items():
        print(i,j)
        print(a[i][0])
details()
d={"name":["Kanaka","Durga","Teja"],
   "marks":[70,71,72],"status":["R","M","R"]}
details(**d)'''

#both * and **
def final(*a,**b):
    d=2
    print(a)
    print(b)
    print(type(a))
    print(type(b))
    for i in a:
        d=d+i
        print(d)
    for i,j in b.items():
        print("Key is: ",i)
        print("Value is: ",j)
final()
data=(2,3,4,5,6,7)
final(*data)
d={"name":["Kanaka","Durga","Teja"],"age":[20,21,22]}
final(**d)
final(*data,**d)






