Python 3.14.4 (tags/v3.14.4:23116f9, Apr  7 2026, 14:10:54) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
#String Methods
#len()
a="python"
len(a)
6
b="Python Course"
len(b)
13
c=""
len(c)
0
d=" "
len(d)
1

#Count
a="Twinkle Twinkle little star"
a.count("T")
2
a.count("l")
4
a.count(" ")
3
a.count("Twinkle")
2


#Find a String
a="Python"
a.index("y)
        
SyntaxError: unterminated string literal (detected at line 1)
a.index("y")
        
1
a.find("y")
        
1
a.find("o")
        
4

#Escaping Sequences
        
#\n id new line
        
>>> #\t is tab space
...         
>>> a="Idno\nName\nEmailId\nMobile Number\nBranch\tCollege"
...         
>>> print(a)
...         
Idno
Name
EmailId
Mobile Number
Branch	College
>>> b="IdNo:141\nName:Teja\nMobile:9063758848\nEmailId:vkdteja03@gmail.com\nBranch: IT\nCollege:Vignan University"
...         
>>> b
...         
'IdNo:141\nName:Teja\nMobile:9063758848\nEmailId:vkdteja03@gmail.com\nBranch: IT\nCollege:Vignan University'
>>> print(b)
...         
IdNo:141
Name:Teja
Mobile:9063758848
EmailId:vkdteja03@gmail.com
Branch: IT
College:Vignan University
