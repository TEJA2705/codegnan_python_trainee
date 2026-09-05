Python 3.14.4 (tags/v3.14.4:23116f9, Apr  7 2026, 14:10:54) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
#Slicing
a="Codegnan"
a[0:4}
SyntaxError: closing parenthesis '}' does not match opening parenthesis '['
a[0:4]
'Code'
a[4:8]
'gnan'
a[:4]
'Code'
a[4:]
'gnan'
b="Work Until You Succeed"
b[5:10]
'Until'
b[15:21]
'Succee'
b[15:]
'Succeed'
b[11:14]
'You'
b[0:4]
'Work'
c="Vijayawada is a Royal City"
len(c)
26
c[22:]
'City'
c[16:21]
'Royal'
c[:10]
'Vijayawada'
c[11:13]
'is'
d="Happy Teachers Day"
len(d)
18
d[-13:]
' Teachers Day'
d[:-13]
'Happy'
d[-3:0]
''
d[-1]
'y'
d[-3:]
'Day'
d[-12:-4]
'Teachers'
e="Vizag is a City of Destiny"
len(e)
26
e[:-21]
'Vizag'
e[-14:-18]
''
e[-14:-9]
'ity o'
e[-13:-9]
'ty o'
e[-15:-10]
'City '
e[-15:-11]
'City'
e[-7:]
'Destiny'
#Striding

a="Data Science"
a[::]
'Data Science'
a[::1]
'Data Science'
a[::-1]
'ecneicS ataD'
a[::2]
'Dt cec'
a[0:4:2]
'Dt'
len(a)
12
>>> a[-7::1]
'Science'
>>> b="Cloud Computing"
>>> a[2:13:3]
'tSee'
>>> b[2:13:3]
'o mt'
>>> b[4:14:5]
'dp'
>>> b[3:12:6]
'up'
>>> 
>>> c="Python Course"
>>> a[-2:-12:-4]
'cct'
>>> c[-2:-12:-4]
'sCh'
>>> c[-4:-13:-5]
'uo'
>>> c[-6:-12:-2]
'Cnh'
>>> c[::1]
'Python Course'
>>> c[::-1]
'esruoC nohtyP'
