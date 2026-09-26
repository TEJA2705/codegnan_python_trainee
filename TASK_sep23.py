#max,min,sum
'''a=[1,2,3,45,678,90]
print(max(a))
print(min(a))
print(sum(a))'''

#Marks Report Analysis
'''n=int(input("Enter No Of Students: "))
a=[]
for i in range(1,n+1):
    a.append(int(input(f"Enter {i} Student Marks:")))
print("Total Students:",n)
print("Highest Mark: ",max(a))
print("Lowest Mark: ",min(a))
print("Sum Of Marks: ",sum(a))
print("Average Marks: ",sum(a)/n)'''

#BMI
'''height=float(input("Enter Height: "))
weight=float(input("Enter Weight: "))
h=height**2
res=weight/h
if res<=18.5:
    print("Under Weight")
elif res>18.5 and res<=24.5:
    print("Healthy Weight")
elif res>24.5 and res<=29.5:
    print("Over Weight")
else:
    print("Obesity")'''

#Pattern Problems
#1.Right Angle Traiangle
a=int(input())
for i in range(a):
    for j in range(a):
        print("*",end="")
    print()

#2 Reverse Triangle
#4 pyramid (mine)

00 01 02 03 04
10 11 12 13 14
20 21 22 23 24
30 31 32 33 34
40 41 42 43 44 

