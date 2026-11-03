#diff blw module,package and library
#module
'''
->A module is single python file it consists python code
->A module contains varaiables , functions , classes
Examples of modules is such as mymodule.py,math.py,random.py'''
#package
'''
A Package contains of python modules is called as package
ex-> requests,numpy,pandas
'''
#libraries
'''
* It consists both modules and packages
Ex: numpy,pandas,matplotlib,Django
'''
#Note: Every python file is a module and import is keyword every python file saved
'''internally with varaibale name as __main__'''

'''import module1
print(module1.greetings("Teja"))'''

#import module1

#import module1

'''import module1
a=module1.details["idnos"]
print(a)'''

#import module1

'''import math
print(math.pi)
print(math.pi*3)
print(math.sqrt(4))
print(math.pow(2,2))
print(math.log(10))
print(math.cos(45))
print(math.sin(45))
print(math.ceil(3.9))
print(math.ceil(9.12))
print(math.floor(6.9))'''

#from keyword
'''from math import pi,log,sqrt,tan
print(pi)
print(tan(45))
#print(math.pow(2,3))
print(math.floor(2,3))# error because we import only four functions'''


#sys module
#import sys
'''print(sys.path)

for i in sys.path:
    print(i)

print(sys.version)'''


#os Module

#import os
#print(os.path)
#print(os.getcwd())
#print(os.listdir())
#print(os.mkdir("temp"))
#print(os.listdir())
#print(os.chdir("C:\\Users\\TEJA VEMURI\\Downloads"))
#print(os.listdir())

'''random module is used to generate random numbers in python , randint()
function is defined as random module
'''
#import random
'''a=random.sample(range(10,50),5)
print(a)'''

#randint()
'''a=random.randint(5,12)
print(a)'''

#choice()
'''a=[1,2,30,4,5]
b=random.choice(a)
print(b)'''


#Task
'''while True:
    r=int(input("Roll The Dice: "))
    ra=random.randint(1,6)
    print("Random Value: ",ra)
    option=int(input("1.Yes\n2.No\nChoose One Option: "))
    if option==1:
        continue
    else:
        break'''

#calendar module
#import calendar
'''year=2005
month=7
print(calendar.month(year,month))'''

'''year=2005
print(calendar.calendar(year))'''

'''a=int(input("Enter year: "))
b=int(input("Enter month: "))
print(calendar.month(a,b))'''


#date & time
'''from datetime import date
a=date.today()
print(a)'''

'''import datetime
a=datetime.datetime.now()
print(a)'''

'''import time
a=time.time()
print(a)#epoch time

b=time.localtime(a)
print(b)

print(f"Today date is {b.tm_mday}-{b.tm_mon}-{b.tm_year}")
print(f"Today Time is {b.tm_hour}-{b.tm_min}-{b.tm_sec}")
print(f"today date is {b.tm_wday}-{b.tm_yday}-{b.tm_isdst}")'''


'''#Task - oct6
import random
import time
for i in range(10):
    a=random.randint(999,9999)
    print(a)
    time.sleep(2)'''

#Regex-Regular expression
'''
Regular Expression powerful tools(module) embedded in python which is mainly used to
find a pattern within a given string or statements or files and mainly used for text
manipulation.
'''
'''a="codegnan is in vja"
print(a)'''

'''a="codegnan\nis\nin\tvja"
print(a)'''

'''a=r"codegnan\nis\nin\tvja"
print(a)'''#it prints as it is of value because we use raw string(it prints as it is)


#compile(),search(),findall(),split(),sub()
#sequence characters
'''
\w -> it matches alphanumeric[A-Z,a-z,0-9,_]
\W -> it matches non alphanumeric
\d -> it matches any digits
\D -> it matches non digits
\s -> it represents white spaces
\S -> it represents non-white spaces
'''


import re
a="code map money cash cap maths cup cat mug mat"
'''b=re.compile(r"m\w\w\w\w")#one \w will give two charcters
print(b)


#search()
c=b.search(a)
print(c)'''

'''c=re.search(r"m\w+",a)
print(c)'''

#findall()
'''b=re.findall(r"m\w+",a)
print(b)'''

'''b=re.findall("m\w+",a)# here we can't mention raw string but it produce the output
print(b)'''#because it find special characters

'''b=re.findall(r"c\w+",a)
print(b)'''

#split()
c=re.split(r"m",a)
print(c)

d=re.split(r"\s",a)
print(d)

d=re.split(r"m\S",a)
print(d)



#sub()
'''e=re.sub(r"maths","science",a)
print(e)'''


'''a='codegna 123 teja 34'
d=re.findall(r"\d",a)
c=re.findall(r"\d+",a)
print(c,d)'''




