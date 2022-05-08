import pandas as pd
from datetime import *
import csv
import shutil
from dateutil.parser import parse
from tkinter import *
def clicked():
    dt1=str(txt1.get())
    dt2=str(txt2.get())
    td1=parse(dt1)
    td2=parse(dt2)
    dtnow=datetime.now()
    fdt=str(dtnow.year)+str(dtnow.month)+str(dtnow.day)+str(dtnow.hour)+str(dtnow.minute)+str(dtnow.second)
    shutil.copy('ssss.csv','temp\ dupliss.csv')
    with open(fdt+'.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["Date and Time","Temprature(C)"])
    df = pd.read_csv('temp\ dupliss.csv')
    final= df['Date'] +" "+ df['Time']
    a= df['Date'] +" "+ df['Time']
    dtlen=len(a)
    x=1
    new=a
    while(x<dtlen):
        new[x]=parse(a[x])
        x+=1

    print(type(new[1]))
    print(new)
    df['Date']=new
    df['Date'][0]=parse(df['Date'][0])
    x=0
    dtlen=len(df['Date'])
    while(x<dtlen):
        if (td1<df['Date'][x]):
            if (td2>df['Date'][x]):
                with open(fdt+".csv","a", newline='') as file2:
                    writerr=csv.writer(file2)
                    writerr.writerow([str(df['Date'][x]),str(df['Temprature'][x])])
        x=x+1
        window.quit()
window = Tk()
window.title("Welcome")
window.geometry('500x250')
lbl1 = Label(window, text="Please Enter First Date(YYYY-MM-DD HH:MM:SS):- ")
lbl1.grid(column=0, row=0)
txt1 = Entry(window,width=20)
txt1.grid(column=1,row=0)
lbl2= Label(window, text="Please Enter Second Date(YYYY-MM-DD HH:MM:SS):- ")
lbl2.grid(column=0, row=1)
txt2 = Entry(window,width=20)
txt2.grid(column=1,row=1)
btn=Button(window,text="Click Me! And Exit",command=clicked)
btn.grid(column=0,row=2)
window.mainloop()
