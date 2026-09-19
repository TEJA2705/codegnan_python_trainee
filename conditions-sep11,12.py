#if condition using comparision operators
#<,>,>=,<=,!=,==
'''a=10
b=20
if a<b:
    print("True")'''

'''a=40
b=60
if a>b:
    print("True")'''

'''a=50
b=8
if a>b:
    print("True")'''

'''a=10
b=20
if a<=b:
    print("True")'''

'''a=30
b=20
if a>=b:
    print("True")'''

'''a=10
b=20
if a!=b:
    print("True")'''

'''a=20
b=20
if a==b:
    print("True")'''

'''a="python"
b="java"
if a!=b:
    print("Same")'''

'''a=int(input("Enetr 1st value: "))
b=int(input("Enter 2nd Value: "))
if a>b:
    print("A is greater than B")'''

'''a=int(input("Enter A value: "))
if a>30:
    print("True")'''


#if condition by using Logical operator
#and,or,not
'''a=4
b=8
if a<b and b>a:
    print("True")'''


'''a=6
b=9
if a<=b and b>=a:
    print("True")'''

'''a=4
b=8
if a!=b and b==a:
    print("True")'''

'''a=10
b=20
if a>b or b>a:
    print("True")'''

'''a=41
b=28
if a<=b or b<=a:
    print("True")'''

'''a=4
b=8
if a!=b or b==a:
    print("True")'''

'''a=4
b=8
if not a>b:
    print("True")'''

'''a=4
b=8
if not b>a:
    print("True")'''

'''a=4
b=8
if not a<b and b>a:
    print("True")'''

'''a=4
b=8
if not a<b or b>a:
    print("True")'''

'''a=int(input("Enter 1st Value: "))
b=int(input("Enter 2nd Value: "))
if (not a>b and b>a)and (a<=b or b<=a):
    print("Condition Is true")'''


#if condition by using identity operator
'''a=10
if type(a) is int:
    print("It is Integer")'''


'''a=2.5
if type(a) is not int:
    print("It Is not Int")'''

'''a=int(input("Enter the Value: "))
if type(a) is int:
    print("Yes It is a Integer")'''


#if condition using membership operator
#in,not in
'''a=[2,3,4,5,6]
if 5 in a:
    print("True")'''


'''a=[2,3,4,5,6]
if 5 not in a:
    print("True")'''

'''a=[2,3,4,5,6,10]
if 10 in a:
    print("True")'''

'''a=int(input("Enter a Value: "))
if 30 in a:
    print("True")'''#Error


'''a=[1,2,2,3,4,5,6]
b=int(input("Enter a Value: "))
if b in a:
    print("Yes")'''


#if else conditions using comparision operator
'''a=5
b=9
if a>b:
    print("A id greater")
else:
    print("B id greater")'''


'''a=5
b=9
if a<b:
    print("A id greater")
else:
    print("B id greater")'''

'''a=5
b=9
if a==b:
    print("both are equal")
else:
    print("Both are not equal")'''

'''a=5
b=9
if a!=b:
    print("Both are Not Equal")
else:
    print("Both are equal")'''


#if else condition using Logical Operator
'''a=5
b=6
if a>5 and b>5:
    print("Both are greater than 5")
else:
    print("Bothare less than 5")'''

'''a=5
b=6
if a>5 or b>5:
    print("one of greater than 5")
else:
    print("Both are less than 5")'''

'''a=5
b=6
if not a<b:
    print("Both are greater than 5")
else:
    print("Else block executed")'''


#if else condition by using membership operator
'''a=[5,6,7,8,9,10]
b=6
if b in a:
    print("B in A")
else:
    print("B not in A")'''

'''a=[5,6,7,8,9,10]
b=6
if b not in a:
    print("B not in A")
else:
    print("B in A")'''

#if else condition using Identity Operator
'''b=6
if type(b) is int:
    print("B in Int")
else:
    print("B not in Int")'''


'''b=6.6
if type(b) is int:
    print("B in Int")
else:
    print("B not in Int")'''



#if-elif-else conditions by using comparison operators
'''a=2
b=4
if a<b:
    print("less")
elif b>a:
    print("greater")
else:
    print("true")'''


'''a=6
b=8
if a>b:
    print("less")
elif b>a:
    print("greater")
else:
    print("true")'''

'''a=12
b=14
if a==b:
    print("less")
elif b<a:
    print("greater")
else:
    print("true")'''

'''a=5
b=8
if a<b:
    print("less")
elif b>a:
    print("greater")
elif a!=b:
    print("not equal")    
else:
    print("true")'''

#if-elif-else conditions by using logical operators 
'''a=5
b=3
if a<b and b>a:
    print("less")
elif a>=b or b!=a:
    print("greater")
elif not b<a:
    print("true")
else:
    print("false")'''

#if-elif-else conditions by using identify operators
'''a=15
if type(a)is int:
    print("true")
elif type(a)is not float:
    print("greater")
else:
    print("false")'''

#if-elif-else conditions by using membership operators
'''a=[2,4,6,8,9,2,10]
if 16 in a:
    print("true")
elif 4 not in a:
    print("greater")
else:
    print("false")'''

#multiple -if
'''a=5
b=10
if a<b:
    print("less")
if b>a:
    print("greater")
if a!=b:
    print("true")'''

'''a=5
b=10
if a<b:
    print("less")
elif b>a:
    print("greater")
if a!=b:
    print("true")'''

#mutiple-if condition by using logical operators
'''a=4
b=2
if a>b and b<a:
    print("true")
if b>a or a!=b:
    print("greater")
if not b>a:
    print("false")'''

#multiple-if condition by using identify operators
'''a=40
if type(a) is int:
    print("true")
if type(a)is not int:
    print("greater")
if type(a) is complex:
    print("false")'''

#multiple-if conditions by using membership operators
'''b=[20,21,22,23,24,26]
if 19 in b:
    print("false")
if 24 not in b:
    print("true")
if 26 in b:
    print("in")'''

#nested-if
'''a=6
b=12
if a<b:
    print("less")
    if b>a:
        print("greater")'''

'''a=6
b=12
if a>b:
    print("less")
if b>a:
    print("greater")'''

'''a=6
b=12
if a==b:
    print("less")
    if b>a:
        print("greater")'''

'''a=10
b=20
if a>b:
    print("less")
    if b==a:
        print("equal")'''

'''a=10
b=20
if a<b:
    print("less")
    if b==a:
        print("equal")
    else:
        print("true")'''

'''a=30
b=50
if a>b:
    print("less")
    if b>a:
        print("equal")
else:
    print("true")'''

'''a=60
b=80
if a<b:
    print("less")
    if b>a:
        print("equal")
    else:
        print("false")
else:
    print("true")'''

'''a=60
b=80
if a>b:
    print("less")
    if b==a:
        print("equal")
    else:
        print("false")
else:
    print("true")'''

a=60
b=80
if a<b:
    print("less")
    if b==a:
        print("equal")
    if a!=b:
        print("not equal")
    else:
        print("false")
else:
    print("true")

    




    




    




    
