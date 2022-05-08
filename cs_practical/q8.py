num=input("Please enter a Number : ")
prod=1
sod=0
for i in num:
    prod*=int(i)
    sod+=int(i)
if(prod==sod):
    print("The given number is a Magical Number")
else:
    print("The given number is not a Magical Number")