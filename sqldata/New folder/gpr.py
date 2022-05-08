import pyodbc
import pandas as pd
import datetime
import tkinter as tk
import pdfkit as pdf
import os



conn = pyodbc.connect('Driver={SQL Server};'
                      'Server=DESKTOP-8G2S04I\WINCC;'
                      'Database=DATA_WINCC;'
                      'Trusted_Connection=yes;')

cursor = conn.cursor()
cursor.execute('SELECT * FROM DATA_WINCC.dbo.Table_2')

ft=()
ft=list(ft)
for row in cursor:
    row=list(row)
    ft.append(row)


def w1cmd():
    nopop=str(nopin.get())
    nooop=str(nooin.get())
    mdop=str(mdin.get())
    edop=str(edin.get())
    bnoop=str(bnoin.get())
    bsop=str(bsin.get())
    lotnop=str(lotnin.get())
    lotsop=str(lotsin.get())
    td1=e1.get()
    td2=e2.get()
    df=fd
    td1 = datetime.datetime.strptime(td1, '%d-%m-%Y %H:%M:%S')
    td2 = datetime.datetime.strptime(td2, '%d-%m-%Y %H:%M:%S')
    df=df[df['Date Time']>td1]
    df=df[df['Date Time']<td2]
    if(nopop!=''):
        df=df[df['NOP']==nopop]
    if(nooop!=''):
        df=df[df['NOO']==nooop]
    if(mdop!=''):
        df=df[df['MFG DATE']==mdop]
    if(edop!=''):
        df=df[df['EXP. DATE']==edop]
    if(bnoop!=''):
        df=df[df['BNO']==bnoop]
    if(bsop!=''):
        df=df[df['BSIZE']==bsop]
    if(lotnop!=''):
        df=df[df['LOTNO']==lotnop]
    if(lotsop!=''):
        df=df[df['LOTSIZE']==lotsop]

    for col in df.columns:
        if 'NOP' in col:
            del df[col]
    for col in df.columns:
        if 'NOO' in col:
            del df[col]
    for col in df.columns:
        if 'MFG DATE' in col:
            del df[col]
    for col in df.columns:
        if 'EXP. DATE' in col:
            del df[col]
    for col in df.columns:
        if 'BSIZE' in col:
            del df[col]
    for col in df.columns:
        if 'BNO' in col:
            del df[col]
    for col in df.columns:
        if 'LOTSIZE' in col:
            del df[col]
    for col in df.columns:
        if 'LOTNO' in col:
            del df[col]
    dtnow=datetime.datetime.now()
    fdt=str(dtnow.year)+str(dtnow.month)+str(dtnow.day)+str(dtnow.hour)+str(dtnow.minute)+str(dtnow.second)
    
    df.to_html(fdt+'.html',index=False,header=False)
    with open(fdt+'.html','r') as html_file:
        s=html_file.read()
        html_file.close()
    s=s.replace('<tr>','<tr align="right">')
    a=""
    x=36
    slen=len(s)
    while(x<slen):
        a+=s[x]
        x+=1  
    s=a
    s0=r"<html><head><style>table#t01, td {  border-collapse: collapse;  border: 1px solid black;}</style></head><img src = 'download.png' width=100px/><font size=5><b>Akums Drugs & Parmaceuticals Ltd.</b></font><h2 style='text-align: center;'> Gelatin Process Report</h2>"
    s1=r"<table border='1' class='dataframe'> <thead>   <tr style='text-align: left;'>   <th width=210px>NAME OF OPERATOR</th><td width=210px>"+nooop+"</td>   <th width=210px>NAME OF PRODUCT</th><td width=210px>"+nopop+"</td>  </tr>  <tr style='text-align: left;'> <th width=210px>BATCH NO.</th><td    width=75px>"+bnoop+"</td><th width=210px>BATCH SIZE </th><td  width=75px>"+bsop+"</td>  </tr>  <tr style='text-align: left;'>  <th width=210px>MFG Date</th><td  width=75px>"+mdop+"</td>  <th width=210px>EXP. Date</th><td  width=75px>"+edop+"</td>  </tr>  <tr style='text-align: left;'>  <th width=210px>LOT NO.</th><td  width=75px>"+lotnop+"</td>  <th width=210px>LOT SIZE</th><td  width=75px>"+str(lotsin.get())+"</td></tr>  </table>"
    f1=r"<br><table  id='t01' class='dataframe'>  <thead>    <tr style='text-align: center;'>      <th></th>      <th colspan=2>STILER RPM</th>      <th width=50px>VOLTAGE (STILLER)</th>      <th colspan=2>VACUUM</th>      <th width=50px>CURRENT (STILER)</th>      <th colspan=4>PROCESS TIME</th> <th colspan=2>TEMPARATURE</th>    </tr>  </thead>  <thead>    <tr style='text-align: center;'>      <th>DATE/TIME</th>      <th>SET</th>      <th>ACTUAL</th>      <th>ACTUAL</th>      <th>SET</th>      <th>ACTUAL</th>      <th>ACTUAL</th>      <th colspan=2>SET</th>      <th colspan=2>ACTUAL</th><th>SET</th>      <th>ACTUAL</th>    </tr>  </thead>  <thead>    <tr style='text-align: center;'>      <th></th>      <th>(rpm)</th>      <th>(rpm)</th>      <th>(Volt)</th>      <th>(mmHg)</th>      <th>(mmHg)</th>      <th>(A)</th>      <th>(Min)</th>      <th>(Sec)</th>      <th>(Min)</th>      <th>(Sec)</th>  <th>('C)</th>     <th>('C)</th> </tr>  </thead>"
    s2=r"<br> <table border='1' class='dataframe'>  <thead>     <tr style='text-align: left;'>  <th width=210px> SIGN/DATE</th>  <td> </td>  <th width=210px> SIGN/DATE</th>  <td> </td>  </tr>    <tr style='text-align: left;'>  <th width=210px> Checked by       (production)</th>  <td  width=210px> </td>  <th width=210px> Verified by (IPQA)</th>  <td  width=210px> </td>  </tr>"
    with open(fdt+'.html','w') as html_file:
        html_file.write(s0+s1+f1+a+s2)
        html_file.close()
    path_wkhtmltopdf = r'C:\Program Files\wkhtmltopdf\bin\wkhtmltopdf.exe'
    config = pdf.configuration(wkhtmltopdf=path_wkhtmltopdf)
    pdf.from_file(fdt+'.html',fdt+'.pdf',configuration=config)
    os.remove(fdt+'.html')


  


m = tk.Tk()

fd = pd.DataFrame(ft,columns=['Date Time','RPM1','RPM2','RPM3','RPM4','RPM5','RPM6','RPM7','RPM8','RMP9','RPM10','RMP11','RPM12','NOP','NOO','MFG DATE','EXP. DATE','BNO','BSIZE','LOTNO','LOTSIZE'])

bs=()
bs=list(bs)
bs.append('')
btlen=len(fd['BSIZE'])
x=1
while(x<btlen):
    if(str(fd['BSIZE'][x]) not in bs):
        bs.append(str(fd['BSIZE'][x]))
    x+=1

btchnos=()
btchnos=list(btchnos)
btchnos.append('')
btlen=len(fd['BNO'])
x=1
while(x<btlen):
    if(str(fd['BNO'][x]) not in btchnos):
        btchnos  .append(str(fd['BNO'][x]))
    x+=1

noo=()
noo=list(noo)
noo.append('')
btlen=len(fd['NOO'])
x=1
while(x<btlen):
    if(str(fd['NOO'][x]) not in noo):
        noo.append(str(fd['NOO'][x]))
    x+=1

nop=()
nop=list(nop)
nop.append('')
btlen=len(fd['NOP'])
x=1
while(x<btlen):
    if(str(fd['NOP'][x]) not in nop):
        nop.append(str(fd['NOP'][x]))
    x+=1

lotn=()
lotn=list(lotn)
lotn.append('')
btlen=len(fd['LOTNO'])
x=1
while(x<btlen):
    if(str(fd['LOTNO'][x]) not in lotn):
        lotn.append(str(fd['LOTNO'][x]))
    x+=1

md=()
md=list(md)
md.append('')
btlen=len(fd['MFG DATE'])
x=1
while(x<btlen):
    if(str(fd['MFG DATE'][x]) not in md):
        md.append(str(fd['MFG DATE'][x]))
    x+=1

ed=()
ed=list(ed)
ed.append('')
btlen=len(fd['EXP. DATE'])
x=1
while(x<btlen):
    if(str(fd['EXP. DATE'][x]) not in ed):
        ed.append(str(fd['EXP. DATE'][x]))
    x+=1


lots=()
lots=list(lots)
lots.append('')
btlen=len(fd['LOTSIZE'])
x=1
while(x<btlen):
    if(str(fd['LOTSIZE'][x]) not in lots):
        lots.append(str(fd['LOTSIZE'][x]))
    x+=1

  
m.title('SQL Server Reporting Tool')

nopin=tk.StringVar(m)
nopin.set(btchnos[0])
w1 = tk.OptionMenu(m, nopin, *nop)
w1.config(bg='#FFFFFF')
tk.Label(m, text='Name Of Product:',anchor="w",width=20).grid(row=2,column=2)
w1.grid(row=2,column=3)

nooin=tk.StringVar(m)
nooin.set(btchnos[0])
w2 = tk.OptionMenu(m, nooin, *noo)
w2.config(bg='#FFFFFF')
tk.Label(m, text='Name Of Operator:',anchor="w",width=20).grid(row=2,column=0)
w2.grid(row=2,column=1)

bnoin=tk.StringVar(m)
bnoin.set(btchnos[0])
w3 = tk.OptionMenu(m, bnoin, *btchnos)
w3.config(bg='#FFFFFF')
tk.Label(m, text='Batch No.:',anchor="w",width=20).grid(row=3,column=0)
w3.grid(row=3,column=1)

bsin=tk.StringVar(m)
bsin.set(btchnos[0])
w4 = tk.OptionMenu(m, bsin, *bs)
w4.config(bg='#FFFFFF')
tk.Label(m, text='Batch Size:',anchor="w",width=20).grid(row=3,column=2)
w4.grid(row=3,column=3)

lotnin=tk.StringVar(m)
lotnin.set(btchnos[0])
w5 = tk.OptionMenu(m, lotnin, *lotn)
w5.config(bg='#FFFFFF')
tk.Label(m, text='Lot No.:',anchor="w",width=20).grid(row=5,column=0)
w5.grid(row=5,column=1)

lotsin=tk.StringVar(m)
lotsin.set(btchnos[0])
w6 = tk.OptionMenu(m, lotsin, *lots)
w6.config(bg='#FFFFFF')
tk.Label(m, text='Lot Size:',anchor="w",width=20).grid(row=5,column=2)
w6.grid(row=5,column=3)

mdin=tk.StringVar(m)
mdin.set(btchnos[0])
w7 = tk.OptionMenu(m, mdin, *md)
w7.config(bg='#FFFFFF')
tk.Label(m, text='MFG Date:',anchor="w",width=20).grid(row=4,column=0)
w7.grid(row=4,column=1)

edin=tk.StringVar(m)
edin.set(btchnos[0])
w8 = tk.OptionMenu(m, edin, *ed)
w8.config(bg='#FFFFFF')
tk.Label(m, text='EXP. Date:',anchor="w",width=20).grid(row=4,column=2)
w8.grid(row=4,column=3)

e1 = tk.Entry(m)
e2 = tk.Entry(m)

tk.Label(m, text='').grid(row=0,column=0)
tk.Label(m, text='           Start(DD-MM-YYYY HH:MM:SS)*').grid(row=1,column=0)
e1.grid(row=1, column=1)
tk.Label(m, text='End(DD-MM-YYYY HH:MM:SS)*').grid(row=1,column=2)
e2.grid(row=1, column=3)
tk.Label(m, text='       ').grid(row=1,column=7)



tk.Label(m, text='').grid(row=10,column=0)
button = tk.Button(m, text='Print', width=25, command=w1cmd).grid(row=11,column=1,columnspan=2)
tk.Label(m, text='').grid(row=12,column=0)
m.mainloop()