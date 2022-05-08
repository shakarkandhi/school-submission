temperatures = [10, -20, -289, 100]
def c_to_f(c):
    f = c* 9/5 + 32
    return f

with open("temprature.txt","w")as myfile:
    for t in temperatures:
        myfile.write(str(c_to_f(t)))
		
