#Email Automation
#otp Authentication
import random
import math
import smtplib#simple mail transfer protocol


digits="0123456789"
OTP=""

for i in range(4):
    OTP+=digits[math.floor(random.random()*10)]
otp=OTP+" is your otp"
msg=otp

s=smtplib.SMTP("smtp.gmail.com",587)#port number
s.starttls()
s.login("vkdteja02@gmail.com","jcbz yges oogn cnic")
user="vkdteja02@gmail.com"
email=input("Enter the mail which you want to send otp")
s.sendmail(user,email,msg)
while True:
    a=input("Enter the otp: ")
    if a==OTP:
        print("otp is correct")
    else:
        print("Incorrect otp")
