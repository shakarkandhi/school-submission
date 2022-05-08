import pandas as pd
import psycopg2
import datetime
import os
class Report1:
    def __init__(self,inp):
        dict1=inp.to_dict()
        dict1['fromdt']=dict1['fromdt'].replace('T', ' ')
        dict1['todt']=dict1['todt'].replace('T', ' ')
        self.data=dict1
    
    def generate(self):
        
        
        """Getting the data from SQL Server"""
        
        conn = psycopg2.connect(database="postgres", user='postgres', password='4321ivar', host='localhost', port= '5432')
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM public.testgrafana WHERE time BETWEEN '+"'"+str(self.data['fromdt'])+"'"+' AND '+"'"+str(self.data['todt'])+"'"+'order by time;')
        column_names = [desc[0] for desc in cursor.description]
        df=pd.DataFrame(cursor.fetchall(),columns=column_names)
        df['time']=df['time'].dt.tz_localize(None)
        cursor.close()
        conn.close()
        dtnow=datetime.datetime.now()
        fdt=str(dtnow.year)+str(dtnow.month)+str(dtnow.day)+str(dtnow.hour)+str(dtnow.minute)+str(dtnow.second)
        optpath=os.path.join('static','reports',fdt+'.xlsx')
        df.to_excel(optpath,index=False)
        return(fdt+'.xlsx')