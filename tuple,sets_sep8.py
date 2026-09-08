Python 3.14.4 (tags/v3.14.4:23116f9, Apr  7 2026, 14:10:54) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
#tuple
a=(2,5.6,"teja",3+4j,True,False)
print(a)
(2, 5.6, 'teja', (3+4j), True, False)
type(a)
<class 'tuple'>
len(a)
6
a.count(4+9j)
0
a.count(3+4j)
1
a.index(False)
5

#sets
a={"hi"}
a
{'hi'}
type(a)
<class 'set'>
#set is semi mutable and unordered
#wont allow duplicates
a={4,4.5,"python",5+4j,True,False}
print(a)
{False, True, (5+4j), 4.5, 4, 'python'}
type(a)
<class 'set'>
b={6,7,8,9,2,3,6,7}
b
{2, 3, 6, 7, 8, 9}

#methods in sets
#add()
a={1,4,2,3}
a
{1, 2, 3, 4}
a.add(5)
a
{1, 2, 3, 4, 5}
#subset
b={7,8,9}
b.issubset(a)
False
b={1,2}
b.issubset(a)
True
a.issubset(b)
False
#superset
a.issuperset(b)
True
b.issuperset(a)
False
#union
a={1,2,3,4,5,6}
b={2,3,4,7,8,9}
a.union(b)
{1, 2, 3, 4, 5, 6, 7, 8, 9}
#intersection  -> common values
a.intersection(b)
{2, 3, 4}
#update -> it updates the entire set
a.update(b)
a
{1, 2, 3, 4, 5, 6, 7, 8, 9}
#difference
a.difference(b)
{1, 5, 6}
#symmetric difference
a.symmetric_difference(b)
{1, 5, 6}
a
{1, 2, 3, 4, 5, 6, 7, 8, 9}
b
{2, 3, 4, 7, 8, 9}
#difference_update
a.difference_update(b)
a
{1, 5, 6}
>>> b.difference_update(a)
>>> b
{2, 3, 4, 7, 8, 9}
>>> #intersection_update
>>> a={3,4,5,6,7,8}
>>> b={1,3,6,7,8,9,10}
>>> a.intersection_update(b)
>>> a
{8, 3, 6, 7}
>>> b.intersection_update(a)
>>> b
{8, 3, 6, 7}
>>> #symmetric differnce update
>>> a={6,7,8,9,10,11,12}
>>> b={10,11,12,13,14,15}
>>> a.symmetric_difference_update(b)
>>> a
{6, 7, 8, 9, 13, 14, 15}
>>> b.symmetric_difference_update(a)
>>> b
{6, 7, 8, 9, 10, 11, 12}
>>> #pop()
>>> a={10,20,30,40,50}
>>> a.pop()
50
>>> a
{20, 40, 10, 30}
a.pop()
20
a
{40, 10, 30}
#remove()
a.remove(10)
a
{40, 30}
#discard
a.discard(30)
a
{40}
a.copy()
{40}
b=a.copy()
b
{40}
#clear()
a.clear()
a
set()
b=set()
b.add(50)
b
{50}
#len()
len(b)
1
a.index(50)
Traceback (most recent call last):
  File "<pyshell#93>", line 1, in <module>
    a.index(50)
AttributeError: 'set' object has no attribute 'index'
a.count(50)
Traceback (most recent call last):
  File "<pyshell#94>", line 1, in <module>
    a.count(50)
AttributeError: 'set' object has no attribute 'count'
#disjoint
a={3,4,5,6,7,8}
b={2,3,4,5,6}
a.disjoin(b)
Traceback (most recent call last):
  File "<pyshell#98>", line 1, in <module>
    a.disjoin(b)
AttributeError: 'set' object has no attribute 'disjoin'. Did you mean: 'isdisjoint'?
a.disjoint(b)
Traceback (most recent call last):
  File "<pyshell#99>", line 1, in <module>
    a.disjoint(b)
AttributeError: 'set' object has no attribute 'disjoint'. Did you mean: 'isdisjoint'?
a.isdisjoint(b)
False
