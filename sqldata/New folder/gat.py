# -*- coding: utf-8 -*-
"""
Created on Sun Apr 19 23:55:45 2020

@author: DELL
"""




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
cursor.execute('SELECT * FROM DATA_WINCC.dbo.Table_4')

ft=()
ft=list(ft)
for row in cursor:
    row=list(row)
    ft.append(row)
fd = pd.DataFrame(ft,columns=['Date Time','ObjectID','Description','Electronic Signature'])

def w2cmd():
    td1=str(e1.get())
    td2=str(e2.get())
    df=fd
    td1 = datetime.datetime.strptime(td1, '%d-%m-%Y %H:%M:%S')
    td2 = datetime.datetime.strptime(td2, '%d-%m-%Y %H:%M:%S')
    df=df[df['Date Time']>td1]
    df=df[df['Date Time']<td2]
    dtnow=datetime.datetime.now()
    fdt=str(dtnow.year)+str(dtnow.month)+str(dtnow.day)+str(dtnow.hour)+str(dtnow.minute)+str(dtnow.second)
    
    s1=r"<img src = 'download.png' width=100px/><font size=5><b>Akums Drugs & Parmaceuticals Ltd.</b></font><h2 style='text-align: center;'> Gelatin Aduit Trail Report</h2>"
    df.to_html(fdt+'.html',index=False)
    with open(fdt+'.html','r') as html_file:
        s=html_file.read()
        html_file.close()
    s=s.replace('<tr style="text-align: right;">','<tr style="text-align: center;">')
    s=s.replace('<tr>','<tr align="center">')
    with open(fdt+'.html','w') as html_file:
        html_file.write(s1+s)
        html_file.close()
    path_wkhtmltopdf = r'C:\Program Files\wkhtmltopdf\bin\wkhtmltopdf.exe'
    config = pdf.configuration(wkhtmltopdf=path_wkhtmltopdf)
    pdf.from_file(fdt+'.html',fdt+'.pdf',configuration=config)
    os.remove(fdt+'.html')
    
m=tk.Tk()
e1 = tk.Entry(m)
e2 = tk.Entry(m)
tk.Label(m, text='').grid(row=0,column=0)
tk.Label(m, text='Geletin Audit Trail',anchor='w').grid(row=1,column=1,columnspan=2)
tk.Label(m, text='').grid(row=2,column=0)
tk.Label(m, text='           Start(DD-MM-YYYY HH:MM:SS)*').grid(row=3,column=0)
e1.grid(row=3, column=1)
tk.Label(m, text='End(DD-MM-YYYY HH:MM:SS)*').grid(row=3,column=2)
e2.grid(row=3, column=3)
tk.Label(m, text='       ').grid(row=1,column=7)



tk.Label(m, text='').grid(row=10,column=0)
button = tk.Button(m, text='Print', width=25,command=w2cmd).grid(row=11,column=1,columnspan=2)
tk.Label(m, text='').grid(row=12,column=0)
m.mainloop()