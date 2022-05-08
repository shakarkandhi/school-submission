import pyodbc
import pandas as pd
import datetime
import tkinter as tk
from datetime import timedelta
#import pdfkit as pdf
import os
m = tk.Tk()
conn = pyodbc.connect('Driver={SQL Server};'
                      'Server=DESKTOP-JGFHFID\SQLEXPRESS;'
                      'Database=rpi;'
                      'Trusted_Connection=yes;')

cursor = conn.cursor()
cursor.execute('SELECT * FROM rpi.dbo.pharma')

ft=()
ft=list(ft)
for row in cursor:
    row=list(row)
    ft.append(row)
fd = pd.DataFrame(ft,columns=['Date Time','NOP','NOO','MFG DATE','EXP. DATE','BNO','BSIZE','LOTNO','LOTSIZE'])
btchnos=()
btchnos=list(btchnos)
btchnos.append('')
btlen=len(fd['BNO'])
x=1
while(x<btlen):
    if(str(fd['NOP'][x]) not in btchnos):
        btchnos.append(str(fd['NOP'][x]))
    x+=1

def cmd():
    m.destroy()
    rpm1=str(bvar1.get())
    rpm2=str(bvar2.get())
    rpm3=str(bvar3.get())
    rpm4=str(bvar4.get())
    rpm5=str(bvar5.get())
    rpm6=str(bvar6.get())
    rpm7=str(bvar7.get())
    rpm8=str(bvar8.get())
    td1=e1.get()
    td2=e2.get()
    df=fd
    x=0
    lslen=len(df['Date Time'])
    td1 = datetime.datetime.strptime(td1, '%d-%m-%Y %H:%M:%S')
    td2 = datetime.datetime.strptime(td2, '%d-%m-%Y %H:%M:%S')
    ls=()
    ls=list(ls)
    while(x<lslen):
        if(df['Date Time'][x]>=td1 and df['Date Time'][x]<=td2):
            ls.append(ft[x])
        x+=1

    ls = pd.DataFrame(ls,columns=['Date Time','NOP','NOO','MFG DATE','EXP. DATE','BNO','BSIZE','LOTNO','LOTSIZE'])

    df=ls
    if(rpm1!=''):
        rpm1=str(rpm1)
        lslen=len(df)
        x=0
        rls1=()
        rls1=list(rls1)
        while(x<lslen):
            if(str(df['NOP'][x])==rpm1):
                rls1.append(df.iloc[x,:])
            x+=1
        rls1 = pd.DataFrame(rls1,columns=['Date Time','NOP','NOO','MFG DATE','EXP. DATE','BNO','BSIZE','LOTNO','LOTSIZE'])
        df=rls1
        df.index = range(len(df['NOP']))
    if(rpm2!=''):
        rpm2=str(rpm2)  
        lslen=len(df)
        x=0
        rls2=()
        rls2=list(rls2)
        while(x<lslen):
            if(str(df['NOO'][x])==rpm2):
                rls2.append(df.iloc[x,:])
            x+=1
        rls2 = pd.DataFrame(rls2,columns=['Date Time','NOP','NOO','MFG DATE','EXP. DATE','BNO','BSIZE','LOTNO','LOTSIZE'])
        df=rls2
        df.index = range(len(df['NOO']))
    if(rpm3!=''):
        rpm3=str(rpm3)
        lslen=len(df)
        x=0
        rls3=()
        rls3=list(rls3)
        while(x<lslen):
            if(str(df['MFG DATE'][x])==rpm3):
                rls3.append(df.iloc[x,:])
            x+=1
        rls3 = pd.DataFrame(rls3,columns=['Date Time','NOP','NOO','MFG DATE','EXP. DATE','BNO','BSIZE','LOTNO','LOTSIZE'])
        df=rls3
        df.index = range(len(df['MFG DATE']))
    if(rpm4!=''):
        rpm4=str(rpm4)
        lslen=len(df)
        x=0
        rls4=()
        rls4=list(rls4)
        while(x<lslen):
            if(str(df['EXP. DATE'][x])==rpm4):
                rls4.append(df.iloc[x,:])
            x+=1
        rls4 = pd.DataFrame(rls4,columns=['Date Time','NOP','NOO','MFG DATE','EXP. DATE','BNO','BSIZE','LOTNO','LOTSIZE'])
        df=rls4
        df.index = range(len(df['EXP. DATE']))
    if(rpm5!=''):
        rpm5=str(rpm5)
        lslen=len(df)
        x=0
        rls5=()
        rls5=list(rls5)
        while(x<lslen):
            if(str(df['BNO'][x])==rpm5):
                rls5.append(df.iloc[x,:])
            x+=1
        rls5 = pd.DataFrame(rls5,columns=['Date Time','NOP','NOO','MFG DATE','EXP. DATE','BNO','BSIZE','LOTNO','LOTSIZE'])
        df=rls5
        df.index = range(len(df['BNO']))
    if(rpm6!=''):
        rpm6=str(rpm6)
        lslen=len(df)
        x=0
        rls6=()
        rls6=list(rls6)
        while(x<lslen):
            if(str(df['BSIZE'][x])==rpm6):
                rls6.append(df.iloc[x,:])
            x+=1
        rls6 = pd.DataFrame(rls6,columns=['Date Time','NOP','NOO','MFG DATE','EXP. DATE','BNO','BSIZE','LOTNO','LOTSIZE'])
        df=rls6
        df.index = range(len(df['BSIZE']))
    if(rpm7!=''):
        rpm7=str(rpm7)
        lslen=len(df)
        x=0
        rls7=()
        rls7=list(rls7)
        while(x<lslen):
            if(str(df['LOTNO'][x])==rpm7):
                rls7.append(df.iloc[x,:])
            x+=1
        rls7 = pd.DataFrame(rls7,columns=['Date Time','NOP','NOO','MFG DATE','EXP. DATE','BNO','BSIZE','LOTNO','LOTSIZE'])
        df=rls7
        df.index = range(len(df['LOTNO']))
    if(rpm8!=''):
        rpm8=str(rpm8)
        lslen=len(df)
        x=0
        rls8=()
        rls8=list(rls8)
        while(x<lslen):
            if(str(df['LOTSIZE'][x])==rpm8):
                rls8.append(df.iloc[x,:])
            x+=1
        rls8 = pd.DataFrame(rls8,columns=['Date Time','NOP','NOO','MFG DATE','EXP. DATE','BNO','BSIZE','LOTNO','LOTSIZE'])
        df=rls8
        df.index = range(len(df['LOTSIZE']))
    '''
        temp=df['Date Time'][0]+timedelta(seconds=avg)
        x=1
        lslen=len(df)
        tp1=()
        tp2=()
        tp1=list(tp1)
        tp2=list(tp2)
        tp2.append(df.iloc[0][:])
        while(x<lslen):
            if(df['Date Time'][x]<temp):
                tp1.append(df.iloc[x][:])
            else:
                tp1=pd.DataFrame(tp1,columns=['Date Time','NOP','NOO','MFG DATE','EXP. DATE','BNO','BSIZE','LOTNO','LOTSIZE'])
                tp2.append(tp1.mean())
                tp2=pd.DataFrame(tp2,columns=['Date Time','NOP','NOO','MFG DATE','EXP. DATE','BNO','BSIZE','LOTNO','LOTSIZE'])
                tp2['Date Time'].iloc[-1]=df['Date Time'][x]
                tp2=tp2.values.tolist()
                tp1=tp1.values.tolist()
                tp1.clear()
                temp+=timedelta(seconds=avg)
            x+=1
        
        temp-=timedelta(seconds=avg)
        
        x=0
        lslen=len(df)
        tp1.clear()
        tp3=()
        tp3=list(tp3)
        while(x<lslen):
            if(df['Date Time'][x]>=temp):
                tp1.append(df.iloc[x][:])
            x+=1
        tp1=pd.DataFrame(tp1,columns=['Date Time','NOP','NOO','MFG DATE','EXP. DATE','BNO','BSIZE','LOTNO','LOTSIZE'])
        tp3.append(tp1.mean())
        tp3=pd.DataFrame(tp3,columns=['Date Time','NOP','NOO','MFG DATE','EXP. DATE','BNO','BSIZE','LOTNO','LOTSIZE'])
        tp3['Date Time'].iloc[-1]=df['Date Time'].iloc[-1]        
        tp2.append(tp3.iloc[0][:])
        tp2=pd.DataFrame(tp2,columns=['Date Time','NOP','NOO','MFG DATE','EXP. DATE','BNO','BSIZE','LOTNO','LOTSIZE'])
        print(tp2)
        df=tp2
    '''
    df.drop(['NOP'], axis = 1)
    for col in df.columns:
        if 'NOP' in col:
            del df[col]
            
    dtnow=datetime.datetime.now()
    fdt=str(dtnow.year)+str(dtnow.month)+str(dtnow.day)+str(dtnow.hour)+str(dtnow.minute)+str(dtnow.second)
    
    s1=r"<table border='1' class='dataframe'>  <thead>  <tr style='text-align: center;'> <img src='C:\Users\IAGAUTOMATION\Desktop\Untitled.jpg' width=100px height=100px><th> Batch</th><td>"+str(batch)+"</td>\n</tr><tr style='text-align: right;'><th>Start</th><td> "+str(td1)+"</td><th>End</th><td>"+str(td2)+"</td></tr></table>"
    df.to_html(fdt+'.html')
    with open(fdt+'.html','r') as html_file:
        s=html_file.read()
        html_file.close()
    with open(fdt+'.html','w') as html_file:
        html_file.write(s1+s)
        html_file.close()
    path_wkhtmltopdf = r'C:\Program Files\wkhtmltopdf\bin\wkhtmltopdf.exe'
    config = pdf.configuration(wkhtmltopdf=path_wkhtmltopdf)
    pdf.from_file(fdt+'.html',fdt+'.pdf',configuration=config)

  
m.title('SQL Server Reporting Tool')

bvar1=tk.StringVar(m)
bvar1.set(btchnos[0])
w1 = tk.OptionMenu(m, bvar1, *btchnos)
w1.config(bg='#FFFFFF')
tk.Label(m, text='Name Of Product:',anchor="w",width=20).grid(row=2,column=0)
w1.grid(row=2,column=1)

bvar2=tk.StringVar(m)
bvar2.set(btchnos[0])
w2 = tk.OptionMenu(m, bvar2, *btchnos)
w2.config(bg='#FFFFFF')
tk.Label(m, text='Name Of Operator:',anchor="w",width=20).grid(row=2,column=2)
w2.grid(row=2,column=3)

bvar3=tk.StringVar(m)
bvar3.set(btchnos[0])
w3 = tk.OptionMenu(m, bvar3, *btchnos)
w3.config(bg='#FFFFFF')
tk.Label(m, text='Batch No.:',anchor="w",width=20).grid(row=3,column=0)
w3.grid(row=3,column=1)

bvar4=tk.StringVar(m)
bvar4.set(btchnos[0])
w4 = tk.OptionMenu(m, bvar4, *btchnos)
w4.config(bg='#FFFFFF')
tk.Label(m, text='Batch Size:',anchor="w",width=20).grid(row=3,column=2)
w4.grid(row=3,column=3)

bvar5=tk.StringVar(m)
bvar5.set(btchnos[0])
w5 = tk.OptionMenu(m, bvar5, *btchnos)
w5.config(bg='#FFFFFF')
tk.Label(m, text='Lot No.:',anchor="w",width=20).grid(row=4,column=0)
w5.grid(row=4,column=1)

bvar6=tk.StringVar(m)
bvar6.set(btchnos[0])
w6 = tk.OptionMenu(m, bvar6, *btchnos)
w6.config(bg='#FFFFFF')
tk.Label(m, text='Lot Size:',anchor="w",width=20).grid(row=4,column=2)
w6.grid(row=4,column=3)

bvar7=tk.StringVar(m)
bvar7.set(btchnos[0])
w7 = tk.OptionMenu(m, bvar7, *btchnos)
w7.config(bg='#FFFFFF')
tk.Label(m, text='MFG Date:',anchor="w",width=20).grid(row=5,column=0)
w7.grid(row=5,column=1)

bvar8=tk.StringVar(m)
bvar8.set(btchnos[0])
w8 = tk.OptionMenu(m, bvar8, *btchnos)
w8.config(bg='#FFFFFF')
tk.Label(m, text='EXP. Date:',anchor="w",width=20).grid(row=5,column=2)
w8.grid(row=5,column=3)

e1 = tk.Entry(m)
e2 = tk.Entry(m)

tk.Label(m, text='').grid(row=0,column=0)
tk.Label(m, text='           Start(DD-MM-YYYY HH:MM:SS)*').grid(row=1,column=0)
e1.grid(row=1, column=1)
tk.Label(m, text='End(DD-MM-YYYY HH:MM:SS)*').grid(row=1,column=2)
e2.grid(row=1, column=3)
tk.Label(m, text='       ').grid(row=1,column=7)



tk.Label(m, text='').grid(row=10,column=0)
button = tk.Button(m, text='Print', width=25, command=cmd).grid(row=11,column=1,columnspan=2)
tk.Label(m, text='').grid(row=12,column=0)

m.mainloop()
