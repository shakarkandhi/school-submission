import pyodbc
import pandas as pd
import datetime
import tkinter as tk
import csv
from datetime import timedelta
import pdfkit as pdf
m = tk.Tk()
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
fd = pd.DataFrame(ft,columns=['Date Time','RPM1','RPM2','RPM3','RPM4','RPM5','RPM6','RPM7','RPM8','BATCH'])
btchnos=()
btchnos=list(btchnos)
btchnos.append('')
btlen=len(fd['BATCH'])
x=1
while(x<btlen):
    if(str(fd['BATCH'][x]) not in btchnos):
        btchnos.append(str(fd['BATCH'][x]))
    x+=1
def cmd():
    batch=str(bvar.get())
    optype=opt.get()
    avg=avg1.get()
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
    rc1=cv1.get()
    rc2=cv2.get()
    rc3=cv3.get()
    rc4=cv4.get()
    rc5=cv5.get()
    rc6=cv6.get()
    rc7=cv7.get()
    rc8=cv8.get()
    '''
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


    df = pd.DataFrame(ft,columns=['Date Time','RPM1','RPM2','RPM3','RPM4','RPM5','RPM6','RPM7','RPM8','BATCH'])
    '''
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

    ls = pd.DataFrame(ls,columns=['Date Time','RPM1','RPM2','RPM3','RPM4','RPM5','RPM6','RPM7','RPM8','BATCH'])

    df=ls
    if(batch!=''):
        batch=str(batch)
        lslen=len(df)
        x=0
        rls1=()
        rls1=list(rls1)
        while(x<lslen):
            if(str(df['BATCH'][x])==batch):
                rls1.append(df.iloc[x,:])
            x+=1
        rls1 = pd.DataFrame(rls1,columns=['Date Time','RPM1','RPM2','RPM3','RPM4','RPM5','RPM6','RPM7','RPM8','BATCH'])
        df=rls1
        df.index = range(len(df['RPM1']))
    if(avg==0):


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
            rls1 = pd.DataFrame(rls1,columns=['Date Time','RPM1','RPM2','RPM3','RPM4','RPM5','RPM6','RPM7','RPM8','BATCH'])
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
            rls2 = pd.DataFrame(rls2,columns=['Date Time','RPM1','RPM2','RPM3','RPM4','RPM5','RPM6','RPM7','RPM8','BATCH'])
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
            rls3 = pd.DataFrame(rls3,columns=['Date Time','RPM1','RPM2','RPM3','RPM4','RPM5','RPM6','RPM7','RPM8','BATCH'])
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
            rls4 = pd.DataFrame(rls4,columns=['Date Time','RPM1','RPM2','RPM3','RPM4','RPM5','RPM6','RPM7','RPM8','BATCH'])
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
            rls5 = pd.DataFrame(rls5,columns=['Date Time','RPM1','RPM2','RPM3','RPM4','RPM5','RPM6','RPM7','RPM8','BATCH'])
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
            rls6 = pd.DataFrame(rls6,columns=['Date Time','RPM1','RPM2','RPM3','RPM4','RPM5','RPM6','RPM7','RPM8','BATCH'])
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
            rls7 = pd.DataFrame(rls7,columns=['Date Time','RPM1','RPM2','RPM3','RPM4','RPM5','RPM6','RPM7','RPM8','BATCH'])
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
            rls8 = pd.DataFrame(rls8,columns=['Date Time','RPM1','RPM2','RPM3','RPM4','RPM5','RPM6','RPM7','RPM8','BATCH'])
            df=rls8
            df.index = range(len(df['RPM8']))
    else:
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
                tp1=pd.DataFrame(tp1,columns=['Date Time','RPM1','RPM2','RPM3','RPM4','RPM5','RPM6','RPM7','RPM8','BATCH'])
                tp2.append(tp1.mean())
                tp2=pd.DataFrame(tp2,columns=['Date Time','RPM1','RPM2','RPM3','RPM4','RPM5','RPM6','RPM7','RPM8','BATCH'])
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
        tp1=pd.DataFrame(tp1,columns=['Date Time','RPM1','RPM2','RPM3','RPM4','RPM5','RPM6','RPM7','RPM8','BATCH'])
        tp3.append(tp1.mean())
        tp3=pd.DataFrame(tp3,columns=['Date Time','RPM1','RPM2','RPM3','RPM4','RPM5','RPM6','RPM7','RPM8','BATCH'])
        tp3['Date Time'].iloc[-1]=df['Date Time'].iloc[-1]        
        tp2.append(tp3.iloc[0][:])
        tp2=pd.DataFrame(tp2,columns=['Date Time','RPM1','RPM2','RPM3','RPM4','RPM5','RPM6','RPM7','RPM8','BATCH'])
        print(tp2)
        df=tp2
    if(rc1==0):
        for col in df.columns:
            if 'RPM1' in col:
                del df[col]
    if(rc2==0):
        df.drop(['RPM2'], axis = 1)
        for col in df.columns:
            if 'RPM2' in col:
                del df[col]
    if(rc3==0):
        df.drop(['RPM3'], axis = 1)
        for col in df.columns:
            if 'RPM3' in col:
                del df[col]
    if(rc4==0):
        df.drop(['RPM4'], axis = 1)
        for col in df.columns:
            if 'RPM4' in col:
                del df[col]
    if(rc5==0):
        df.drop(['RPM5'], axis = 1)
        for col in df.columns:
            if 'RPM5' in col:
                del df[col]
    if(rc6==0):
        df.drop(['RPM6'], axis = 1)
        for col in df.columns:
            if 'RPM6' in col:
                del df[col]
    if(rc7==0):
        df.drop(['RPM7'], axis = 1)
        for col in df.columns:
            if 'RPM7' in col:
                del df[col]
    if(rc8==0):
        df.drop(['RPM8'], axis = 1)
        for col in df.columns:
            if 'RPM8' in col:
                del df[col]
    
    df.drop(['BATCH'], axis = 1)
    for col in df.columns:
        if 'BATCH' in col:
            del df[col]
            
    dtnow=datetime.datetime.now()
    fdt=str(dtnow.year)+str(dtnow.month)+str(dtnow.day)+str(dtnow.hour)+str(dtnow.minute)+str(dtnow.second)
    with open(fdt+'.csv', 'w') as csv_file:
        writer=csv.writer(csv_file)
        writer.writerow(['Batch',batch])
        writer.writerow(["From",str(td1),"To",str(td2)])
    with open(fdt+'.csv', 'a',newline='') as csv_file:
        df.to_csv(csv_file,index=False)
    print(df)
    df.to_html(fdt+'.html')
    pdf.from_file(fdt+'.htl',fdt+'.pdf')
m.title('SQL Server Reporting Tool')
bvar=tk.StringVar(m)
bvar.set(btchnos[0])
w = tk.OptionMenu(m, bvar, *btchnos)
w.config(bg='#FFFFFF')
tk.Label(m, text='Batch Selection*',anchor="w",width=20).grid(row=2,column=0)
w.grid(row=2,column=1,columnspan=2)
e1 = tk.Entry(m)
e2 = tk.Entry(m)
cv1=tk.IntVar(value=1)
cv2=tk.IntVar(value=1)
cv3=tk.IntVar(value=1)
cv4=tk.IntVar(value=1)
cv5=tk.IntVar(value=1)
cv6=tk.IntVar(value=1)
cv7=tk.IntVar(value=1)
cv8=tk.IntVar(value=1)
avg1=tk.IntVar(value=0)
opt=tk.IntVar(value=3)
tk.Label(m, text='Average Interval:',anchor="w",width=20).grid(row=3,column=0)
tk.Radiobutton(m, text='1 min' ,variable=avg1, value=60).grid(row=3,column=1)
tk.Radiobutton(m, text='10 min', variable=avg1, value=600).grid(row=3,column=2)
tk.Radiobutton(m, text='30 min', variable=avg1, value=1800).grid(row=3,column=3)
tk.Radiobutton(m, text='60 min', variable=avg1, value=3600).grid(row=3,column=4)
tk.Radiobutton(m, text='None', variable=avg1, value=0).grid(row=3,column=5)
tk.Label(m, text='Export Type:',anchor="w",width=20).grid(row=8,column=0)
tk.Radiobutton(m, text='PDF' ,variable=opt, value=1).grid(row=8,column=1)
tk.Radiobutton(m, text='XLSX', variable=opt, value=2).grid(row=8,column=2)
tk.Radiobutton(m, text='CSV', variable=opt, value=3).grid(row=8,column=3)
tk.Label(m, text='Tag Selection:',anchor="w",width=20).grid(row=4,column=0)
c1 = tk.Checkbutton(m, text='RPM1', variable=cv1,onvalue=1,offvalue=0)
c2 = tk.Checkbutton(m, text='RPM2', variable=cv2,onvalue=1,offvalue=0)
c3 = tk.Checkbutton(m, text='RPM3', variable=cv3,onvalue=1,offvalue=0)
c4 = tk.Checkbutton(m, text='RPM4', variable=cv4,onvalue=1,offvalue=0)
tk.Label(m, text='Tag Selection:',anchor="w",width=20).grid(row=6,column=0)
c5 = tk.Checkbutton(m, text='RPM5', variable=cv5,onvalue=1,offvalue=0)
c6 = tk.Checkbutton(m, text='RPM6', variable=cv6,onvalue=1,offvalue=0)
c7 = tk.Checkbutton(m, text='RPM7', variable=cv7,onvalue=1,offvalue=0)
c8 = tk.Checkbutton(m, text='RPM8', variable=cv8,onvalue=1,offvalue=0)

c1.grid(row=4,column=1)
c2.grid(row=4,column=2)
c3.grid(row=4,column=3)
c4.grid(row=4,column=4)
c5.grid(row=6,column=1)
c6.grid(row=6,column=2)
c7.grid(row=6,column=3)
c8.grid(row=6,column=4)
e3 = tk.Entry(m, width=5)
e4 = tk.Entry(m, width=5)
e5 = tk.Entry(m, width=5)
e6 = tk.Entry(m, width=5)
e7 = tk.Entry(m, width=5)
e8 = tk.Entry(m, width=5)
e9 = tk.Entry(m, width=5)
e10 = tk.Entry(m, width=5)


tk.Label(m, text='').grid(row=0,column=0)
tk.Label(m, text='           Start(DD-MM-YYYY HH:MM:SS)*').grid(row=1,column=0)
e1.grid(row=1, column=1)
tk.Label(m, text='End(DD-MM-YYYY HH:MM:SS)*').grid(row=1,column=2)
e2.grid(row=1, column=3)
tk.Label(m, text='       ').grid(row=1,column=7)
tk.Label(m, text='Filter:',anchor="w",width=20).grid(row=5,column=0)
e3.grid(row=5, column=1)
e4.grid(row=5, column=2)
e5.grid(row=5, column=3)
e6.grid(row=5, column=4)
tk.Label(m, text='Filter:',anchor="w",width=20).grid(row=7,column=0)
e7.grid(row=7, column=1)
e8.grid(row=7, column=2)
e9.grid(row=7, column=3)
e10.grid(row=7, column=4)

tk.Label(m, text='').grid(row=10,column=0)
button = tk.Button(m, text='Print', width=25, command=cmd).grid(row=11,column=1,columnspan=2)
tk.Label(m, text='').grid(row=12,column=0)

m.mainloop()
