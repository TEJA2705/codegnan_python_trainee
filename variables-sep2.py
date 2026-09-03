Python 3.14.4 (tags/v3.14.4:23116f9, Apr  7 2026, 14:10:54) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
print(5+6)
11
a=10
b=12
print(a+b)
22
c=50
print(c)
50
e=100
print(E)
Traceback (most recent call last):
  File "<pyshell#7>", line 1, in <module>
    print(E)
NameError: name 'E' is not defined. Did you mean: 'e'?
print(e)
100
name="Teja"
print(name)
Teja
city="Guntur"
print(city)
Guntur
country="India"
print(country)
India
f=8,g=5
SyntaxError: invalid syntax. Maybe you meant '==' or ':=' instead of '='?
@f=10
SyntaxError: invalid syntax. Maybe you meant '==' or ':=' instead of '='?
_a=20
print(_a)
20
$=9
SyntaxError: invalid syntax
h,j=20,k
Traceback (most recent call last):
  File "<pyshell#20>", line 1, in <module>
    h,j=20,k
NameError: name 'k' is not defined
h,j=20,k=30
SyntaxError: invalid syntax. Maybe you meant '==' or ':=' instead of '='?
z=2,3,4,5,6,7
print(a)
10
x,y,w=2,3,4
print(x,y,w)
2 3 4
u,v,s=2,3,4,5,6,6
Traceback (most recent call last):
  File "<pyshell#26>", line 1, in <module>
    u,v,s=2,3,4,5,6,6
ValueError: too many values to unpack (expected 3, got 6)
u,v,s=(4,5,6)
print(u,v,s)
4 5 6
first="Teja"
lname="Vemuri"
print(first+lname)
TejaVemuri
print(first+"
      
SyntaxError: unterminated string literal (detected at line 1)
>>> print(first+" "+lname)
...       
Teja Vemuri
>>> del lname
...       
>>> print(lname)
...       
Traceback (most recent call last):
  File "<pyshell#35>", line 1, in <module>
    print(lname)
NameError: name 'lname' is not defined. Did you mean: 'name'?
>>> name1="Teja"
...       
>>> print(name1)
...       
Teja
>>> Name="Teja"
...       
>>> print(Name)
...       
Teja
>>> NAME="DURGA"
...       
>>> print(NAME)
...       
DURGA
