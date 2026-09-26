#every list comprehension rewritten it as a for loop but for loop cant written in list comphersion
#List Comprehension
a=["python","java","dsa"]

#print(a.upper())

'''for i in a:
    print(i.upper(),end="")'''

'''b=[]
for i in a:
    b.append(i.upper())
print(b)'''

#Syntax
#a=[exp for var in collection/range]
'''a=[i.upper() for i in a]
print(a)'''

'''b=["apple","banana"]
b=[i.capitalize() for i in b]
print(b)'''

'''b=[1,2,3,5,6,8,12,13]
b=[i*i for i in b]
print(b)'''

'''b=[x for x in range(16) if x%2==0]
print(b)'''

'''b=[x*x for x in range(31) if x%2==0]
print(b)'''

'''b=["grapes","berry","mango","kiwi","dragon","apple"]
c=[x for x in b if 'a' in x]
print(c)'''

'''b=["grapes","berry","mango","kiwi","dragon","apple"]
c=[x for x in b if 'a' not in x]
print(c)'''

#no elif in List comphersion
#if-else uasge in list Comphersion
'''a=[i*i if i%2==0 else i*5  for i in range(21)]
print(a)'''


a=[1,2,3,4,5]
b=[5,4,3,2,1]
c=[i+j for i in a for j in b if a.index(i)==b.index(j)]
print(c)

'''a=[1,2,3,4,5]
b=[5,4,3,2,1]
c=[a[i]+b[j] for i in range(len(a))]
print(c)'''

