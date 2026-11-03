#Exception Handling
'''
try-> Instructions form which are expecting the exceptions
except-> Exceptions are raised in try block it will be handled by this block
else -> optional(no-exceptions)
finally -> Always
'''

'''while True:
    try:
        a=int(input("A Value: "))
        b=int(input("B Value: "))
        c=a/b
        print("Value: ",c)
    except:
        print("exception is raised")
    else:
        print("No exceptions")
    finally:
        print("Programs Ends")'''


#file handling
'''a=open("teja.txt","w")
a.write("python full stack")
a.close()'''

'''a=open("teja.txt","w")
a.write("python")
a.close()'''

#append()
'''a=open("teja.txt","a")
a.write("\t full stack")
a.close()'''

'''a=input("Enter Text: ")
b=open("teja.txt","w")
b.write(a)
b.close()'''

#read()
#b=open("teja.txt","w")
#print(b.read())
#print(b.readline())
#print(b.readlines())
#print(b.read(18))
'''c=["krishna","teja","lohith","hemanth"]
for i in c:
    b.writelines(i+'\n')
b.writelines("\n".join(c))
b.close()'''


'''a=open("swaping.py")
print(a.read())'''

'''a=open('C:\\Users\\TEJA VEMURI\\Desktop\\codegnan\\swaping.py')
print(a.read())'''

'''a=open('C:/Users/TEJA VEMURI/Desktop/codegnan/swaping.py')
print(a.read())'''

    



