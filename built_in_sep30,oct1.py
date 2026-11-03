#Task
#Built-in functions
#max(),min(),sum(),len(),print(),input(),type(),next(),range()
'''l=[1,2,3,4]
print(min(l))
print(max(l))
print(len(l))
print(sum(l))
a=input("Enter: ")
print(type(a))
if l[0] in range(1,11):
    print("Yes")
def sync(a):
    yield a
    yield a+"Vemuri"
b=sync(a)
print(next(b))
print(next(b))'''

#fromkeys()
'''a="codegnan"
print(a)
print(list(a))
print(tuple(a))
print(set(a))

#print(dict(a))'''

'''b=dict.fromkeys(a)
print(b)

c=dict.fromkeys(a,'teja')
print(c)

c["g"]="python"
print(c)'''

#eval()
'''while True:
    a=int(input("a value"))
    b=int(input("b value"))
    print(a+b)'''


'''while True:
    a=float(input("a value"))
    b=float(input("b value"))
    print(a+b)'''


'''while True:
    a=input("a value: ")
    b=input("b value: ")
    print(a+b)'''

  
'''while True:
    a=eval(input("Enter: "))
    b=eval(input("Enter: "))
    print(type(a))
    print(type(b))'''


#zip()->we can combine multiple collections into one collection,datatype complusary
'''a=[10,20,30,40,50]
names=['a','b','c','d','e']
print(a+names)

b=zip(a,names)
print(b)

b=zip(a,names)
print(*b)

b=list(zip(a,names))
print(b)

b=tuple(zip(a,names))
print(b)

b=set(zip(a,names))
print(b)

b=dict(zip(a,names))
print(b)'''

#enumerate->we can give counter to  the collection, datatype is complusary
'''names=["a",'b','c','d']
for i in range(len(names)):
    print(i,names[i])

b=list(enumerate(names))
print(b)

b=list(enumerate(names,10))
print(b)


b=tuple(enumerate(names,10))
print(b)


b=set(enumerate(names,10))
print(b)

b=dict(enumerate(names,10))
print(b)'''


#Annonymous function are name less functions and we used a keyword called is lambda
'''to create a annonymous functio'''
#Task
'''def func(x):
    return 2*x+5
print(func(5))'''


#syntax -> a=lambda arg:exp
'''a=lambda x:2*x+5
print(a(5))'''


'''b=lambda x:2*x+5
print(b(int(input())))'''

'''a=lambda a,b:a*b
print(a(2,3))'''

'''a=lambda x:x.upper()
print(a("teja"))'''

'''a=lambda a,b:a+b
print(a("Vemuri","Teja"))'''

'''a,b=[x for x in input("Enter: ").split(" ")]
c=lambda a,b:(a+" "+b).title()
print(c(a,b))'''


'''a=[2,3,4,5,6,7,8,9,22,33,12,24,46]
for i in a:
    if i%2==0:
        print(i)'''


#filter()->filter(function, iterable)
#a=[2,3,4,5,6,7,8,9,22,33,12,24,46]
'''if a%2==0:
    print(a)'''#error

'''for i in a:
    if i%2==0:
        print(i)'''

'''b=list(filter(lambda x:x%2==0,a))
print(b)'''

#[],(),{},set()
'''a=[]
print(type(a))

b=()
print(type(b))

c=set()
print(type(c))

d={}
print(type(d))'''

'''a=[[],(),set(),{},None,"","python",3,4.3,3+4j,True,False]
b=list(filter(None,a))
print(b)'''


#map()->each object from a collection and forms a new collection
'''a=[1,2,3,4,5,6,7]
b=[0,4,5,6,7,8,9]
c=list(map(max,a,b))
print(c)'''

'''a=list(map(int,input().split()))
print(a)'''

#run_time input()
'''a=int(input("A: "))
b=int(input("B: "))
print(a+b)'''

'''a,b=[int(x) for x in input("values").split(",")]
print(a+b)'''

'''a,b=int(input("enter the value").split(","))
print(a+b)#error'''

'''a,b=map(int,input("Enter the values").split(","))
print(a+b)'''


'''a=input("data1: ")
b=input("data2: ")
print(a+b)'''

'''a,b=[x for x in input().split()]
print(a+b)'''

'''a,b=input("data").split(",")
print(a,b)'''

'''a,b=map(str,input("data").split(","))
print(a+b)'''

'''a=list(map(int,input().split()))
print(a)

a=list(map(eval,input().split()))
print(a)

a=tuple(map(int,input().split()))
print(a)

a=set(map(int,input().split()))
print(a)

'''
#dict runtime
t=input().split()
d={}
for i in range(len(t)-1):
    d[t[0]]=t[1]
print(d)


'''a=dict(map(lambda x:x.split(":"),input().split(",")))
print(a)'''

'''a=input("Enter key value pairs: ")
b=dict(i.split(":") for i in a.split(","))
print(b)'''







