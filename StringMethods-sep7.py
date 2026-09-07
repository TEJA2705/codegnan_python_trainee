Python 3.14.4 (tags/v3.14.4:23116f9, Apr  7 2026, 14:10:54) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
#Replace
a="Wait until you succeed"
a.replace("Wait","Work")
'Work until you succeed'
a.replace("work","Wait")
'Wait until you succeed'

#Upper
a="upper"
a.upper()
'UPPER'
#lower
b="CODE"
b.lower()
'code'
#Capitalize
c="my"
c.capitalize()
'My'
#title
d="my name is teja"
d.title()
'My Name Is Teja'

a="Hello World"
a.startswith("h")
False
a.stratswith("H")
Traceback (most recent call last):
  File "<pyshell#20>", line 1, in <module>
    a.stratswith("H")
AttributeError: 'str' object has no attribute 'stratswith'. Did you mean: 'startswith'?
a.startswith("H")
True
a.endswith("d")
True
a.isalpha()
False
b="Java"
b.isalpha()
True
c="123"
c.isdigit()
True
d="123hello"
d.isalnum()
True

#strip()
#lstrip(),rstrip()
a="    Teja    "
a.strip()
'Teja'
a.lstrip()
'Teja    '
a.rstrip()
'    Teja'

#concatenation
a="Code"
b="gnan"
print(a+b)
Codegnan
print(a+" "+b)
Code gnan

#anthor use of title
a="python"
b="course"
print((a+" "+b).title())
Python Course

#split
a="python java c c++"
a.split()
['python', 'java', 'c', 'c++']

#join
b="vja","hyd","vzg"
"".join(b)
'vjahydvzg'
" ".join(b)
'vja hyd vzg'
"k".join(b)
'vjakhydkvzg'
a="hello"
"k".join(a)
'hkeklklko'

#Formating
a=5
b=7
print(a+b)
12
print("Sum of two numbers",a+b)
Sum of two numbers 12

#Format method
a="motu"
b="patlu"
print("hello {}{}".format(a,b))
hello motupatlu
print("Hello {} {}".format(a,b))
Hello motu patlu
print("Hello {} hello {}".format(a,b))
Hello motu hello patlu

>>> #Formating string
>>> a="Durga"
>>> b="Teja"
>>> print(f"hello {Durga} {Teja}")
Traceback (most recent call last):
  File "<pyshell#77>", line 1, in <module>
    print(f"hello {Durga} {Teja}")
NameError: name 'Durga' is not defined
>>> print(f"Hello {a} {b}")
Hello Durga Teja
>>> 
>>> 
>>> fname="Teja"
>>> lname="Vemuri"
>>> print("My Name is {} {}".format(fname,lname))
My Name is Teja Vemuri
>>> print(f"My Name is {lname} {fname}")
My Name is Vemuri Teja
>>> 
>>> a,b=2,3
>>> print("Sum: {}{}{}".format(a,b,a+b))
Sum: 235
>>> print("Sum: {} {}is {}".format(a,b,a+b))
Sum: 2 3is 5
>>> print("Sum of {} {} is {}".format(a,b,a+b))
Sum of 2 3 is 5
