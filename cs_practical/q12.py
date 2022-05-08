first=0
second=1
lim=int(input("Please enter a number : "))
print(first,second,end=" ")
for i in range(0,lim-2):
    third=first+second
    print(third,end=" ")
    first,second=second,third