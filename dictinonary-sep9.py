Python 3.14.4 (tags/v3.14.4:23116f9, Apr  7 2026, 14:10:54) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> #dict{}
>>> a={"name":"Teja","city":"Vijayawada"}
>>> print(a)
{'name': 'Teja', 'city': 'Vijayawada'}
>>> type(a)
<class 'dict'>
>>> b={"name","teja"}
>>> type(b)
<class 'set'>
>>> 
>>> a={"day":9,"Month":"sep","year":2026}
>>> a["month"}
SyntaxError: closing parenthesis '}' does not match opening parenthesis '['
>>> a["month"]
Traceback (most recent call last):
  File "<pyshell#9>", line 1, in <module>
    a["month"]
KeyError: 'month'
>>> a["Month"]
'sep'
>>> #Keys()
>>> a.keys()
dict_keys(['day', 'Month', 'year'])
>>> #Values()
a.values()
dict_values([9, 'sep', 2026])
#items()
a.items()
dict_items([('day', 9), ('Month', 'sep'), ('year', 2026)])
a.get("year")
2026
#update -> for adding of elements
a={"name":"Teja","village":"Namburu"}
a.update({"email":"vkdteja02@gmail.com"})
a
{'name': 'Teja', 'village': 'Namburu', 'email': 'vkdteja02@gmail.com'}
a.update({"Phone":"9063258848","age":21})
a
{'name': 'Teja', 'village': 'Namburu', 'email': 'vkdteja02@gmail.com', 'Phone': '9063258848', 'age': 21}
#Setdefault
a={"hour":2,"min":28}
a.setdefault("sec",54)
54
a
{'hour': 2, 'min': 28, 'sec': 54}
a.pop()
Traceback (most recent call last):
  File "<pyshell#28>", line 1, in <module>
    a.pop()
TypeError: pop expected at least 1 argument, got 0
a.pop("sec")
54
a
{'hour': 2, 'min': 28}
a.popitem()
('min', 28)
a
{'hour': 2}
#copy()
a.copy()
{'hour': 2}
len(a)
1
len(a)
1
a.count("hour")
Traceback (most recent call last):
  File "<pyshell#37>", line 1, in <module>
    a.count("hour")
AttributeError: 'dict' object has no attribute 'count'
a.index("hour")
Traceback (most recent call last):
  File "<pyshell#38>", line 1, in <module>
    a.index("hour")
AttributeError: 'dict' object has no attribute 'index'
a.clear()
a
{}
#wont allow duplicates
a={"name":"teja","year":2026,"name":"vemuri"}
a
{'name': 'vemuri', 'year': 2026}
a={"name":"teja","year":2026,"name1":"vemuri"}
a
{'name': 'teja', 'year': 2026, 'name1': 'vemuri'}
a={"idnos":[10,20,30],"name":["teja","chandu","durga"]}
a
{'idnos': [10, 20, 30], 'name': ['teja', 'chandu', 'durga']}
a.keys()
dict_keys(['idnos', 'name'])
a.values()
dict_values([[10, 20, 30], ['teja', 'chandu', 'durga']])
a[idnos][1]
Traceback (most recent call last):
  File "<pyshell#51>", line 1, in <module>
    a[idnos][1]
NameError: name 'idnos' is not defined
a["idnos"][1]
20
