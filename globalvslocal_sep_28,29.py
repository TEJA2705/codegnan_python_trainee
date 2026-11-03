#Difference Blw Local and Global Variable
'''A varaibale is defined inside and outside the function is called Global and
Local Variables
-> A Variable is defined Outside the function and is accessible to the entire global
space is called Global Variable
-> A Variable is defined inside the function and is accessible to the entire global
space is called local Variable
'''
#First Case of Global Variable
'''a=4
def check():
    print("Inside value is",a)
check()
print("Outside Value is",a)'''

#Second Case of Global Variable
'''a=5
def check1():
    a=10
    a=a**2
    print("Inside value is",a)
check1()
print("Outside a is",a)'''

#Third Case of Global Variable
'''a=5
def check2():
    a=8
    print("A Value is: ",a)
    a=10
    print("A Value is: ",a+5)
    b=12
    b+=a
    print("B Value is: ",b)
check2()
print("Outside A Value is",a)
print("Outside B Value is",b)'''
#Error Because b is an local Variable it Can't be accessed outside


#Usage Of global keyword
''' When User wants to Create a variable inside the function directly and carry 
forward the updated value even outside the function then we need to use global
Keyword variable   '''

'''a=4
def final():
    global a
    print("inside value is",a)
    a=7
    print("Updated Value is",a)
    b=13
    b=b+a
    print("B Value is",b)
final()
print("A value is",a)
print("B value is",b)'''

#ASQII (American Standard Code for Information Interchange)
#chr,ord
'''print(chr(65))
print(chr(90))
print(chr(92))
print(ord("a"))
print(ord("z"))'''
#print(ord(65))# Error Because It Accepts only characters
#print(chr("a")) Error Because It accepts ony numbers

#Task
'''for i in range(ord("A"),ord("Z")+1):
    print(chr(i),end=" ")
print()
for i in range(ord("a"),ord("z")+1):
    print(chr(i),end=" ")'''

'''n=input("Enter Name: ")
for i in n:
    print(f"{i}:{ord(i)}")'''

#Railway Ticket
'''def func(gender):
    if gender=='male':    
        age=int(input("Enter You Age: "))
        if age>60:
            discount=(30/100)*ticket_price
            return ticket_price-discount
        else:
            return ticket_price
    else:
        age=int(input("Enter You Age: "))
        if age>60:
            discount=(50/100)*ticket_price
            return ticket_price-discount
        else:
            discount=(30/100)*ticket_price
            return ticket_price-discount
ticket_price=1000
gender=input("Enter Your Gender: ")
price=func(gender)
print(f"price: {price}")'''


'''#Generators -> No tuple comphersion in above cases if we remove those braces and
keep parenthsis than the outcome is generator'''

'''a=[i for i in range(16)]
print(a)
print(*a)'''

'''a=(i for i in range(16))
print(a)
print(*a)'''

'''print(type(a))'''

'''a=(i for i in range(16))
#print(list(a))
#print(tuple(a))
print(set(a))'''

'''#Generator is also a function which can be used as an iterator (loop) when producing a
group of  values where we can use yield
yyield vs return
 ->return will terminate the function where as yeild can pass the
 function and go on with every successive iteration.
'''

a,b=[int(x) for x in input("Enter: ").split(",")]
def check(a,b):
    while a<b:
        yield a
        a=a+1
        yield a
for i in check(a,b):
    print(i)

'''a,b=[int(x) for x in input("Enter: ").split(",")]
def check(a,b):
    while a<b:
        a+=1
        return a
print(check(a,b))'''


#yield v/s return
'''def mygen():
    #return "python"
    #return "java"
    #return "c"
    return "python","java","c"
print(*mygen())'''

'''def mygen():
    yield "vja"
    yield "hyd"
    yield "vzg"
print(*mygen())

#next()
b=mygen()
print(next(b))
print(next(b))
print(next(b))'''








    
