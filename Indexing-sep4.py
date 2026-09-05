Python 3.14.4 (tags/v3.14.4:23116f9, Apr  7 2026, 14:10:54) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> #Indexing
>>> a="Vemuri"
>>> a[0]
'V'
>>> a[5]
'i'
>>> a[3]
'u'
>>> a[0]+a[1]+a[2]
'Vem'
>>> b="My name is Teja"
>>> a[8]+a[9]+a[10]+a[11]
Traceback (most recent call last):
  File "<pyshell#7>", line 1, in <module>
    a[8]+a[9]+a[10]+a[11]
IndexError: string index out of range
>>> b[8]+b[9]+b[10]+b[11]
'is T'
>>> a="I am Learning Python Fullstack"
>>> a[14:19]
'Pytho'
>>> a[14]+a[15]+a[16]+a[17]+a[18]+a[19]
'Python'
>>> a[5]+a[6]+a[7]+a[8]+a[9]
'Learn'
a[-9]+a[-8]+a[-7]+a[-6]+a[-5]+a[-4]+a[-3]+a[-2]+a[-1]
'Fullstack'
b="Codegnan it Solutions"
len(b)
21
b[-13]+b[-14]+b[-15]+b[-16]+b[-17]+b[-18]+b[-19]+b[-20]+b[-21]
' nangedoC'
