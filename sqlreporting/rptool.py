import pyodbc
import pandas as pd
import datetime
import tkinter as tk 

m = tk.Tk() 
def cmd(): 
    global td1, td2, rpm1, rpm2, rpm3, rpm4, rpm5, rpm6, rpm7, rpm8
    td1=e1.get()
    td2=e2.get()
    rpm1=(e3.get())
    rpm2=(e4.get())
    rpm3=(e5.get())
    rpm4=(e6.get())
    rpm5=(e7.get())
    rpm6=(e8.get())
    rpm7=(e9.get())
    rpm8=(e10.get())
    m.destroy()
m.title('SQL Server Reporting Tool')

e1 = tk.Entry(m) 
e2 = tk.Entry(m) 
e3 = tk.Entry(m, width=5) 
e4 = tk.Entry(m, width=5) 
e5 = tk.Entry(m, width=5) 
e6 = tk.Entry(m, width=5) 
e7 = tk.Entry(m, width=5) 
e8 = tk.Entry(m, width=5) 
e9 = tk.Entry(m, width=5) 
e10 = tk.Entry(m, width=5) 


tk.Label(m, text='').grid(row=0,column=0)
tk.Label(m, text='     From(DD-MM-YYYY HH:MM:SS)').grid(row=1,column=0)  
e1.grid(row=1, column=1)
tk.Label(m, text='To(DD-MM-YYYY HH:MM:SS)').grid(row=1,column=2) 
e2.grid(row=1, column=3) 
tk.Label(m, text='       ').grid(row=1,column=7)
tk.Label(m, text='RPM1').grid(row=2,column=0) 
e3.grid(row=3, column=0)
tk.Label(m, text='RPM2').grid(row=2,column=1)  
e4.grid(row=3, column=1)
tk.Label(m, text='RPM3').grid(row=2,column=2) 
e5.grid(row=3, column=2) 
tk.Label(m, text='RPM4').grid(row=2,column=3) 
e6.grid(row=3, column=3)
tk.Label(m, text='RPM5').grid(row=4,column=0)
e7.grid(row=5, column=0) 
tk.Label(m, text='RPM6').grid(row=4,column=1)
e8.grid(row=5, column=1)
tk.Label(m, text='RPM7').grid(row=4,column=2)
e9.grid(row=5, column=2) 
tk.Label(m, text='RPM8').grid(row=4,column=3)
e10.grid(row=5, column=3)

button = tk.Button(m, text='Print', width=25, command=cmd).grid(row=6,column=1,columnspan=2)
tk.Label(m, text='').grid(row=7,column=0)

m.mainloop() 


conn = pyodbc.connect('Driver={SQL Server};'
                      'Server=DESKTOP-8G2S04I\WINCC;'
                      'Database=DATA_WINCC;'
                      'Trusted_Connection=yes;')

cursor = conn.cursor()
cursor.execute('SELECT * FROM DATA_WINCC.dbo.Table_1')

ft=()
ft=list(ft)
for row in cursor:
    row=list(row)
    ft.append(row)
df = pd.DataFrame(ft,columns=['DateTime','RPM1','RPM2','RPM3','RPM4','RPM5','RPM6','RPM7','RPM8']) 

print(df)
print(td1)
print(td2)
print(rpm1)
print(rpm2)
print(rpm3)
print(rpm4)
print(rpm5)
print(rpm6)
print(rpm7)
print(rpm8)

x=0
lslen=len(df['DateTime'])

td1 = datetime.datetime.strptime(td1, '%d-%m-%Y %H:%M:%S')
td2 = datetime.datetime.strptime(td2, '%d-%m-%Y %H:%M:%S')
ls=()
ls=list(ls)
while(x<lslen):    
    if(df['DateTime'][x]>=td1 and df['DateTime'][x]<=td2):
        ls.append(ft[x])
    x+=1

ls = pd.DataFrame(ls,columns=['DateTime','RPM1','RPM2','RPM3','RPM4','RPM5','RPM6','RPM7','RPM8']) 

df=ls

print(df)

if(rpm1!=''):
    rpm1=str(rpm1)
    lslen=len(df)
    x=0
    rls1=()
    rls1=list(rls1)
    while(x<lslen):    
        if(str(df['RPM1'][x])==rpm1):
            rls1.append(df.iloc[x,:])
        x+=1
    rls1 = pd.DataFrame(rls1,columns=['DateTime','RPM1','RPM2','RPM3','RPM4','RPM5','RPM6','RPM7','RPM8']) 
    df=rls1
    df.index = range(len(df['RPM1']))
if(rpm2!=''):
    rpm2=str(rpm2)
    lslen=len(df)
    x=0
    rls2=()
    rls2=list(rls2)
    while(x<lslen):    
        if(str(df['RPM2'][x])==rpm2):
            rls2.append(df.iloc[x,:])
        x+=1
    rls2 = pd.DataFrame(rls2,columns=['DateTime','RPM1','RPM2','RPM3','RPM4','RPM5','RPM6','RPM7','RPM8']) 
    df=rls2
    df.index = range(len(df['RPM2']))
if(rpm3!=''):
    rpm3=str(rpm3)
    lslen=len(df)
    x=0
    rls3=()
    rls3=list(rls3)
    while(x<lslen):    
        if(str(df['RPM3'][x])==rpm3):
            rls3.append(df.iloc[x,:])
        x+=1
    rls3 = pd.DataFrame(rls3,columns=['DateTime','RPM1','RPM2','RPM3','RPM4','RPM5','RPM6','RPM7','RPM8']) 
    df=rls3
    df.index = range(len(df['RPM3']))
if(rpm4!=''):
    rpm4=str(rpm4)
    lslen=len(df)
    x=0
    rls4=()
    rls4=list(rls4)
    while(x<lslen):    
        if(str(df['RPM4'][x])==rpm4):
            rls4.append(df.iloc[x,:])
        x+=1
    rls4 = pd.DataFrame(rls4,columns=['DateTime','RPM1','RPM2','RPM3','RPM4','RPM5','RPM6','RPM7','RPM8']) 
    df=rls4
    df.index = range(len(df['RPM4']))
if(rpm5!=''):
    rpm5=str(rpm5)
    lslen=len(df)
    x=0
    rls5=()
    rls5=list(rls5)
    while(x<lslen):    
        if(str(df['RPM5'][x])==rpm5):
            rls5.append(df.iloc[x,:])
        x+=1
    rls5 = pd.DataFrame(rls5,columns=['DateTime','RPM1','RPM2','RPM3','RPM4','RPM5','RPM6','RPM7','RPM8']) 
    df=rls5
    df.index = range(len(df['RPM5']))
if(rpm6!=''):
    rpm6=str(rpm6)
    lslen=len(df)
    x=0
    rls6=()
    rls6=list(rls6)
    while(x<lslen):    
        if(str(df['RPM6'][x])==rpm6):
            rls6.append(df.iloc[x,:])
        x+=1
    rls6 = pd.DataFrame(rls6,columns=['DateTime','RPM1','RPM2','RPM3','RPM4','RPM5','RPM6','RPM7','RPM8']) 
    df=rls6
    df.index = range(len(df['RPM6']))
if(rpm7!=''):
    rpm7=str(rpm7)
    lslen=len(df)
    x=0
    rls7=()
    rls7=list(rls7)
    while(x<lslen):    
        if(str(df['RPM7'][x])==rpm7):
            rls7.append(df.iloc[x,:])
        x+=1
    rls7 = pd.DataFrame(rls7,columns=['DateTime','RPM1','RPM2','RPM3','RPM4','RPM5','RPM6','RPM7','RPM8']) 
    df=rls7
    df.index = range(len(df['RPM7']))
if(rpm8!=''):
    rpm8=str(rpm8)
    lslen=len(df)
    x=0
    rls8=()
    rls8=list(rls8)
    while(x<lslen):    
        if(str(df['RPM8'][x])==rpm8):
            rls8.append(df.iloc[x,:])
        x+=1
    rls8 = pd.DataFrame(rls8,columns=['DateTime','RPM1','RPM2','RPM3','RPM4','RPM5','RPM6','RPM7','RPM8']) 
    df=rls8
    df.index = range(len(df['RPM8']))
print(df)
