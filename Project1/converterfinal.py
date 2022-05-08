import csv
import io
with open('BATCH CHARGER 2.csv', 'r') as file:
    reader = csv.reader(file,delimiter=',')
    ip=list(reader)
with open('AIS.csv', 'r') as file:
    reader = csv.reader(file,delimiter=',')
    ft=list(reader)
lslen=len(ip)
x=2
y=1
ftlen=len(ft)
while(x<lslen):
    y=1
    while(y<ftlen):
        if(ft[y][0]==ip[x][0]):
            ft[y][2]=ip[x][4]
            if(ft[y][0]=='P095'):
                ft[y][2]=''.join(c for c in ft[y][2] if c.isdigit())
            else:
                ft[y][2]=''.join(c for c in ft[y][2] if c.isdigit() or c=='.')
        y+=1
    x+=1
print(ft)
with open('Script_1.txt','r') as file:
    data = file.readlines()
lslen=len(data)
x=5
while(x<lslen):
    y=0
    while(y<ftlen):
        if(data[x][11:14]==ft[y][1]):
            d1=data[x]
            bd = '     '+d1[30:1000]
            data[x]= d1[0:21]+ft[y][2]+bd
        if(data[x][11:15]==ft[y][1]):
            d1=data[x]
            bd = '     '+d1[31:1000]
            data[x]= d1[0:22]+ft[y][2]+bd
        y+=1
    x+=1

with open('Script_1.txt','w') as file:
    file.writelines(data)
