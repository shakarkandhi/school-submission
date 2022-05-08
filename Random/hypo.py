import math
def hypo(x,y):
    x=x**2
    y=y**2
    c=x+y
    return(math.sqrt(c))


re="A"
while re =='A':
    a=int(input("A :- "))
    b=int(input("B :- "))
    print("C :- ",hypo(a,b))
