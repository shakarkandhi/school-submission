import psycopg2
import pandas as pd
import datetime
from zoneinfo import ZoneInfo
host = "ec2-65-1-130-86.ap-south-1.compute.amazonaws.com"
conn = psycopg2.connect(database="postgres", user='conn_check', password='4321ivar', host=host, port= '5432')
cursor = conn.cursor()
cursor.execute('select pid,pg_stat_activity.usename,state from pg_stat_activity;')
df=pd.DataFrame(cursor.fetchall(),columns=['PID','username','state'])
print(df)
users=pd.read_csv('list.csv')
print(users)
dtnow=datetime.datetime.now(tz=ZoneInfo('Asia/Kolkata'))
for i in range(0,len(users['User'])):
    if(users.loc[i,'User'] not in list(df['username'])):
        if(users.loc[i,'conn'] == 1):
            users.loc[i,'conn']=0
            command='INSERT INTO public.machine_status("time",%s) VALUES(\'%s\',0)' %(users.loc[i,'User'],dtnow)
            print(command)
            cursor.execute(command)
        elif(users.loc[i,'conn'] == 0):
            continue
    if(users.loc[i,'User'] in list(df['username'])): 
        if(users.loc[i,'conn'] == 0):
            users.loc[i,'conn']=1
            command='INSERT INTO public.machine_status("time",%s) VALUES(\'%s\',1)' %(users.loc[i,'User'],dtnow)
            print(command)
            cursor.execute(command)
        elif(users.loc[i,'conn'] == 0):
            continue
conn.commit()
cursor.close()
conn.close()
print(users)
users.to_csv('list.csv',index=False)