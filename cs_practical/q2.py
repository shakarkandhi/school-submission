x=int(input("Please Enter first Number : "))
y=int(input("Please Enter second Number : "))
z=int(input("Please Enter third Number : "))
if(x>y):
    if(x>z):
        print("Largest number from the given numbers is",x)
    else:
        print("Largest number from the given numbers is",z)
else:
    if(y>z):
        print("Largest number from the given numbers is",y)
    else:
        print("Largest number from the given numbers is",z)
