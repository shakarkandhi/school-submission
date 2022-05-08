num=int(input("Please enter a number : "))
lim=int(input("Please enter a limit : "))

sum1=0
for n in range(0,lim):
    sum1+=num**n
print("Sum of the series is",sum1)