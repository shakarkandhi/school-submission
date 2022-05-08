max_marks=float(input("Please Enter Maximum Marks Possible in any Subject : "))
e=float(input("Please Enter your English Marks : "))
p=float(input("Please Enter your Physics Marks : "))
c=float(input("Please Enter your Chemistry Marks : "))
m=float(input("Please Enter your Mathematics Marks : "))
cs=float(input("Please Enter your Computer Science Marks : "))
total_marks=e+p+c+m+cs
percentage=total_marks/max_marks*20
print("Total Marks :",total_marks)
print("Percentage :",percentage)
if(percentage>=75):
    grade="A"
elif(percentage<75 and percentage>=60):
    grade="B"
elif(percentage<60 and percentage>=45):
    grade="C"
elif(percentage<45 and percentage>=33):
    grade="D"
elif(percentage<33):
    grade="Reappear"
print("Grade :",grade)