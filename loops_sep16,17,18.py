#Task
'''a=['apple','banana','grapes']
for i in range(len(a)):
    a[i]=a[i].upper()
print(a)'''


#while loop
'''a=10
while a>1:
    print(a)'''


'''a=10
while a<1:
    print(a)'''

'''a=20
while a>=1:
    print(a)
    a=a-1'''

'''a=20
while a>1:
    a=a-1
    print(a)'''

'''a=15
while a>2:
    print(a)
    a=a-1'''

'''a=20
while a>1:
    a=a-1
print(a)'''

'''a=30
while a>1:
    print(a)
    a+=1'''

'''a=30
while a>1:
    print(a)
    a-=1'''

'''a=5
while a<15:
    print(a)
    a+=1'''

'''while True:
    age=int(input("Enter the age: "))
    if age>=18:
        print("Eligible for vote")
    else:
        print("Not Eligible for Vote")'''


#range()
#start-stop-step
'''for i in range(10):
    print(i)'''

'''for i in range(15,30):
    print(i)'''

'''for i in range(0,20,2):
    print(i,end=" ")'''

'''for i in range(5,50,5):
    print(i,end=" ")'''

'''for i in range(3,30,3):
    print(i,end=" ")'''


#Task
'''while True:
    marks=int(input("Enter the Marks: "))
    if marks in range(91,101):
        print("Grade-A")
    elif marks in range(81,91):
        print("Grade-B")
    elif marks in range(71,81):
        print("Grade-C")
    elif marks in range(50,71):
        print("Grade-D")
    else:
        print("Fail")'''

#Task
'''a=int(input("Enter No of Students: "))
p,ab=0,0
for i in range(a):
    att=input(f"Enter {i+1}st Attendence: ").lower()
    if att=='p':
        p+=1
    else:
        ab+=1
print("Total No of Students: ",a)
print("Total Presentes: ",p)
print("Total Abstences: ",ab)'''


#Break -> The break statement is used to terminate the entire loop
#Continue -> continue statement is skip the current iteration and rest of the code will contiune
#pass -> A pass is null statement it does nothing but syntactially we need

#Break
'''a=10
while a>1:
    print(a)
    a=a-1
    if a==7:
        break'''

'''a=10
while a>1:
    a=a-1
    if a==4:
        break
    print(a)'''


'''for i in range(10):
    if i==8:
        break
    print(i)'''

'''a="python"
if a=="h":
    break  #Error because we cant write break outside loop
print(a)'''


'''a="python"
for i in a:
    if i=='h':
        break
    print(i)'''


#Continue
'''a=20
while a>5:
    a=a-1
    if a==12:
        continue
    print(a)'''

'''for i in range(15):
    if i==10:
        continue
    print(i)'''

'''a="python"
for i in a:
    if i=="y":
        continue
    print(i)'''

#Pass
'''a=5
while a>1:
    print(a)
    a=a-1
    if a==2:
        pass  # If we cant put pass it gives error'''

'''for i in range(25):
    if i==10:
        pass
    print(i)'''

#ATM Application
balance=100000
card='c'
pwd=1234

card1=input("Enter Type of Card: ")
if card==card1:
    print("Welcome Teja")
    pwsd=int(input("Enter the Password: "))
    if pwd==pwsd:
        while True:
            option=int(input("Options: \n1.Balance Enquiry\n2.WithDraw\nEnter Option: "))
            if option==1:
                print(f"Your Balance: {balance}")
            elif option==2:
                withdraw=int(input("Enter Amount: "))
                if withdraw<=balance:
                    balance=balance-withdraw
                else:
                    print("Insufficeint Funds")
            else:
                print("Invalid Option")
    else:
        print("Wrong Password")
else:
    print("Inavlid Card Type")
    
    


