num=input("Please Enter a Number : ")
i=0
while(i<len(num)):
    if(num[i] != num[-1-i]):
        print("Entered number is not a Palindrome")
        break
    i+=1
else:
    print("Entered number is a Palindrome")
