num=input("Please enter a Number : ")
prod=0
for i in num:
    prod+=int(i)**3
if(prod==int(num)):
    print("The given number is a Armstrong Number")
else:
    print("The given number is not a Armstrong Number")
