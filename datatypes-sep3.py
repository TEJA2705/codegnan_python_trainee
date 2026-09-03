Python 3.14.4 (tags/v3.14.4:23116f9, Apr  7 2026, 14:10:54) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
#datatype
a=7
type(a)
<class 'int'>
>>> b=6.7
>>> type(b)
<class 'float'>
>>> c='teja'
>>> type(c)
<class 'str'>
>>> d="hello"
>>> type(d)
<class 'str'>
>>> e='''hi'''
>>> type(e)
<class 'str'>
>>> f=5+6j
>>> type(f)
<class 'complex'>
>>> g=5j
>>> type(g)
<class 'complex'>
>>> x=True
>>> type(x)
<class 'bool'>
>>> y=False
>>> type(y)
<class 'bool'>
>>> #Int coversion
>>> int(8)
8
int(5.0)
5
int("Teja")
Traceback (most recent call last):
  File "<pyshell#22>", line 1, in <module>
    int("Teja")
ValueError: invalid literal for int() with base 10: 'Teja'
int(4+7j)
Traceback (most recent call last):
  File "<pyshell#23>", line 1, in <module>
    int(4+7j)
TypeError: int() argument must be a string, a bytes-like object or a real number, not 'complex'
int(true)
Traceback (most recent call last):
  File "<pyshell#24>", line 1, in <module>
    int(true)
NameError: name 'true' is not defined. Did you mean: 'True'?
int(True)
1
int(False)
0
#float coversion
float(6)
6.0
float(6.6)
6.6
float("Teja")
Traceback (most recent call last):
  File "<pyshell#30>", line 1, in <module>
    float("Teja")
ValueError: could not convert string to float: 'Teja'
float(6+7j)
Traceback (most recent call last):
  File "<pyshell#31>", line 1, in <module>
    float(6+7j)
TypeError: float() argument must be a string or a real number, not 'complex'
float(True)
1.0
float(False)
0.0
#String conversion
str(1)
'1'
str(2.3)
'2.3'
str("Teja")
'Teja'
str(2+3j)
'(2+3j)'
str(True)
'True'
str(False)
'False'
#Complex conversion
complex(2)
(2+0j)
complex(4.5)
(4.5+0j)
complex("Teja")
Traceback (most recent call last):
  File "<pyshell#44>", line 1, in <module>
    complex("Teja")
ValueError: complex() arg is a malformed string
complex(2+j6)
Traceback (most recent call last):
  File "<pyshell#45>", line 1, in <module>
    complex(2+j6)
NameError: name 'j6' is not defined
complex(2+3j)
(2+3j)
complex(True)
(1+0j)
complex(False)
0j
#Boolean conversion
bool(2)
True
bool(2.3)
True
bool("Teja")
True
bool(3+5j)
True
bool(True)
True
bool(False)
False
