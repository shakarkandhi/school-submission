func=int(input("""Enter the number for the desired Function:
               (1) Area of Circle
               (2) Area of Rectangle
               (3) Area of Square
               ->"""))
if(func==1):
    r=float(input("Enter the radius : "))
    print("Area of the given circle is",(r*44/7),"units")
elif(func==2):
    l=float(input("Enter the length : "))
    b=float(input("Enter the breadth : "))
    print("Area of the given rectangle is",(l*b),"units")
elif(func==3):
    s=float(input("Enter the side : "))
    print("Area of the given square is",(s**2),"units")
else:
    print("The entered number is not a given function")