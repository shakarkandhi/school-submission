import pandas as pd
import datetime
import shutil
import tkinter as tk
from dateutil.parser import parse
import pdfkit as pdf
import os


shutil.copy('GELATIN1.csv','dupliss.csv')
fd = pd.read_csv('dupliss.csv')
fd['DATE']=fd['DATE']+" "+fd['TIME']
len1=len(fd['DATE'])
x=0
while(x<len1):
    fd['DATE'][x]=datetime.datetime.strptime(fd['DATE'][x], '%d.%m.%Y %H:%M:%S')
    x+=1

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
    df=df[df['DATE']>td1]
    df=df[df['DATE']<td2]
    if(nopop!=''):
        df=df[df['Prod_name']==nopop]
    if(nooop!=''):
        df=df[df['Op_name']==nooop]
    if(mdop!=''):
        df=df[df['Mfg_date']==mdop]
    if(edop!=''):
        df=df[df['Exp_date']==edop]
    if(bnoop!=''):
        df=df[df['Batch_no']==bnoop]
    if(bsop!=''):
        df=df[df['Batch_size']==bsop]
    if(lotnop!=''):
        df=df[df['Lot_no']==lotnop]
    if(lotsop!=''):
        df=df[df['Lot_size']==lotsop]

    for col in df.columns:
        if 'Prod_name' in col:
            del df[col]
        if 'Op_name' in col:
            del df[col]
        if 'Mfg_date' in col:
            del df[col]
        if 'Exp_date' in col:
            del df[col]
        if 'Batch_size' in col:
            del df[col]
        if 'Batch_no' in col:
            del df[col]
        if 'Lot_size' in col:
            del df[col]
        if 'Lot_no' in col:
            del df[col]
        if 'Null_time' in col:
            del df[col]
        if 'Process_status' in col:
            del df[col]
        if 'Purge_state' in col:
            del df[col]
        if 'Recipe_name' in col:
            del df[col]      
        if 'aa' in col:
            del df[col]
        if 'ab' in col:
            del df[col]
        if 'ac' in col:
            del df[col]
        if 'ad' in col:
            del df[col]
        if 'ae' in col:
            del df[col]
        if 'TIME' in col:
            del df[col]
    dtnow=datetime.datetime.now()
    fdt=str(dtnow.year)+str(dtnow.month)+str(dtnow.day)+str(dtnow.hour)+str(dtnow.minute)+str(dtnow.second)
    
    df.to_html(fdt+'.html',index=False,header=False,columns=['DATE','Imp_rpm_set','Imp_rpm_obs','Imp_torq_obs','Chop_rpm_obs','Chop_rpm_set','Chop_torq_obs','Imp_amp_obs','Chop_amp_obs','Set_time_min','Set_time_sec','Start_time','Stop_time'])
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
    pdf.from_file(fdt+'.html',fdt+'.pdf',configuration=config,options={'header':'false'})
    os.remove(fdt+'.html')
    

  


m = tk.Tk()


os.remove('dupliss.csv')
bs=()
bs=list(bs)
bs.append('')
btlen=len(fd['Batch_size'])
x=1
while(x<btlen):
    if(str(fd['Batch_size'][x]) not in bs):
        bs.append(str(fd['Batch_size'][x]))
    x+=1

btchnos=()
btchnos=list(btchnos)
btchnos.append('')
btlen=len(fd['Batch_no'])
x=1
while(x<btlen):
    if(str(fd['Batch_no'][x]) not in btchnos):
        btchnos  .append(str(fd['Batch_no'][x]))
    x+=1

noo=()
noo=list(noo)
noo.append('')
btlen=len(fd['Op_name'])
x=1
while(x<btlen):
    if(str(fd['Op_name'][x]) not in noo):
        noo.append(str(fd['Op_name'][x]))
    x+=1

nop=()
nop=list(nop)
nop.append('')
btlen=len(fd['Prod_name'])
x=1
while(x<btlen):
    if(str(fd['Prod_name'][x]) not in nop):
        nop.append(str(fd['Prod_name'][x]))
    x+=1

lotn=()
lotn=list(lotn)
lotn.append('')
btlen=len(fd['Lot_no'])
x=1
while(x<btlen):
    if(str(fd['Lot_no'][x]) not in lotn):
        lotn.append(str(fd['Lot_no'][x]))
    x+=1

md=()
md=list(md)
md.append('')
btlen=len(fd['Mfg_date'])
x=1
while(x<btlen):
    if(str(fd['Mfg_date'][x]) not in md):
        md.append(str(fd['Mfg_date'][x]))
    x+=1

ed=()
ed=list(ed)
ed.append('')
btlen=len(fd['Exp_date'])
x=1
while(x<btlen):
    if(str(fd['Exp_date'][x]) not in ed):
        ed.append(str(fd['Exp_date'][x]))
    x+=1


lots=()
lots=list(lots)
lots.append('')
btlen=len(fd['Lot_size'])
x=1
while(x<btlen):
    if(str(fd['Lot_size'][x]) not in lots):
        lots.append(str(fd['Lot_size'][x]))
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