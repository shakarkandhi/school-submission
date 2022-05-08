import csv
import io

#Input File Variable Creation
with open('SIMOVERT_VC.csv', 'r') as file:
    reader = csv.reader(file,delimiter=';')
    ip=list(reader)

#From-To Variable Table Creation
with open('AIS.csv', 'r') as file:
    reader = csv.reader(file,delimiter=',')
    ft=list(reader)

#From-To Value Input
lslen=len(ip)
x=26
y=1
ftlen=len(ft)
while(x<lslen):
    y=1
    while(y<ftlen):
        if(ft[y][0]==ip[x][0] and ft[y][1]==ip[x][2]):
            ft[y][3]=ip[x][4]
            if(ft[y][0]=='P095'):
                ft[y][3]=''.join(c for c in ft[y][3] if c.isdigit() or c=='-')
                ft[y][3]=''.join(c for c in ft[y][3] if c!='¹')
            else:
                ft[y][3]=''.join(c for c in ft[y][3] if c.isdigit() or c=='.' or c=='-')
                ft[y][3]=''.join(c for c in ft[y][3] if c!='¹')
        y+=1
    x+=1
y=1
ftlen=len(ft)
while(y<ftlen):
    if(ft[y][3]=='101' and ft[y][6]=='1'):
        ft[y][3]='"'+"722:0:63"+'"'
    if(ft[y][3]=='122' and ft[y][6]=='1'):
        ft[y][3]='"'+"722:1:63"+'"'
    if(ft[y][3]=='143' and ft[y][6]=='1'):
        ft[y][3]='"'+"722:2:63"+'"'
    if(ft[y][3]=='164' and ft[y][6]=='1'):
        ft[y][3]='"'+"722:3:63"+'"'
    if(ft[y][3]=='185' and ft[y][6]=='1'):
        ft[y][3]='"'+"722:4:63"+'"'
    if(ft[y][3]=='206' and ft[y][6]=='1'):
        ft[y][3]='"'+"722:5:63"+'"'
    y+=1
print(ft)

#Data Conversion
x=1
while(x<ftlen):
    y=1
    while(y<ftlen):
        if(ft[x][0]==ft[y][4]):
            ft[y][3]=(float(ft[y][3])*float(ft[x][3]))/100
            ft[y][3]=str(ft[y][3])
        y+=1
    x+=1
print(ft)

#Output File Variable Creation
with open('G120_CU240E2temp.txt','r') as file:
    data = file.readlines()
lslen=len(data)
x=5

#Output File Variable Writing
while(x<lslen):
    y=0
    while(y<ftlen):
        if(data[x][11:15]==ft[y][2]+',' and (data[x][16:18]==ft[y][5] or data[x][16:18]==ft[y][5]+')')):
            d1 = data[x]
            bd = d1[32:1000]
            data[x]= d1[0:21]+ft[y][3]+bd
        if(data[x][11:16]==ft[y][2]+',' and (data[x][17:19]==ft[y][5] or data[x][17:19]==ft[y][5]+')')):
            d1 = data[x]
            bd = d1[34:1000]
            data[x]= d1[0:22]+ft[y][3]+bd
        #if(data[x][11:17]==ft[y][2]+',' and (data[x][18:20]==ft[y][5] or data[x][18:20]==ft[y][5]+')')):
        #    d1 = data[x]
        #    bd = d1[34:1000]
        #    data[x]= d1[0:22]+ft[y][3]+bd
        y+=1
    x+=1

#Final File Writing
with open('G120_CU240E2.txt','w') as file:
    file.writelines(data)
