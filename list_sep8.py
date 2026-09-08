Python 3.14.4 (tags/v3.14.4:23116f9, Apr  7 2026, 14:10:54) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> #List[]
>>> a=[3,4.5,"python",6+8j,True,False]
>>> a
[3, 4.5, 'python', (6+8j), True, False]
>>> type(a)
<class 'list'>
>>> b=4.5
>>> type(b)
<class 'float'>
>>> c=[4.5]
>>> type(c)
<class 'list'>
>>> 
>>> #Methods in List
>>> a=["python","java","c"]
>>> a.append("c++")
>>> a
['python', 'java', 'c', 'c++']
>>> a.ppend("ml","ai")
Traceback (most recent call last):
  File "<pyshell#13>", line 1, in <module>
    a.ppend("ml","ai")
AttributeError: 'list' object has no attribute 'ppend'. Did you mean: 'append'?
>>> a.append(["ml","ai"])
a
['python', 'java', 'c', 'c++', ['ml', 'ai']]
a.extend(["ds","dl"])
a
['python', 'java', 'c', 'c++', ['ml', 'ai'], 'ds', 'dl']
a.insert(1,"c#")
a
['python', 'c#', 'java', 'c', 'c++', ['ml', 'ai'], 'ds', 'dl']
#Index
a,index("c#")
Traceback (most recent call last):
  File "<pyshell#21>", line 1, in <module>
    a,index("c#")
NameError: name 'index' is not defined
a.index("c#")
1
#copy()
a.copy()
['python', 'c#', 'java', 'c', 'c++', ['ml', 'ai'], 'ds', 'dl']
b=a.copy()
b
['python', 'c#', 'java', 'c', 'c++', ['ml', 'ai'], 'ds', 'dl']
#Deletion
a.pop()
'dl'
a.pop("c#")
Traceback (most recent call last):
  File "<pyshell#29>", line 1, in <module>
    a.pop("c#")
TypeError: 'str' object cannot be interpreted as an integer
a.pop(1)
'c#'
a
['python', 'java', 'c', 'c++', ['ml', 'ai'], 'ds']
a.remove(["ml","ai"])
a
['python', 'java', 'c', 'c++', 'ds']
a.remove("ds")
a
['python', 'java', 'c', 'c++']
a.delete("c")
Traceback (most recent call last):
  File "<pyshell#36>", line 1, in <module>
    a.delete("c")
AttributeError: 'list' object has no attribute 'delete'
#Sort()
a.sort()
a
['c', 'c++', 'java', 'python']
b=[5,6,7,2,1]
b.sort()
b
[1, 2, 5, 6, 7]
b=[2,3,"teja",3+6j,True]
b.sort()
Traceback (most recent call last):
  File "<pyshell#44>", line 1, in <module>
    b.sort()
TypeError: '<' not supported between instances of 'str' and 'int'
#reverse()
a.reverse()
a
['python', 'java', 'c++', 'c']
#len(0
len(a)
4
temp='java'
len(temp)
4
#count()
a.count("c")
1
#clear()
a.clear()
a
[]
