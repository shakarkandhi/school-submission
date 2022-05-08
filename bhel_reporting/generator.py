import pandas as pd
import numpy as np
import psycopg2
import matplotlib.pyplot as plt
import os
import datetime
import pdfkit as pdf
from datetime import timedelta
import calendar
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
        cursor.execute('SELECT datetime,main_supply_energy FROM public.cotmac_iiot WHERE datetime BETWEEN '+"'"+str(self.data['fromdt'])+"'"+' AND '+"'"+str(self.data['todt'])+"'"+'order by datetime;')
        df=pd.DataFrame(cursor.fetchall(),columns=['datetime','energy'])
        cursor.close()
        conn.close()
        print(df)
        
        """Grouping the data via frequency"""
        
        def getDateRangeFromWeek(p_year,p_week):
        
            firstdayofweek = datetime.datetime.strptime(f'{p_year}-{p_week}-1', "%Y-%W-%w").date()
            lastdayofweek = firstdayofweek + datetime.timedelta(days=6.9)
            return str(firstdayofweek)+' To '+ str(lastdayofweek)
        
        
        if(self.data['frequency'].lower()=='monthly'):
            df['month'] = df['datetime'].dt.month
            df['year'] = df['datetime'].dt.year
            df['month'] = df['month'].apply(lambda x: calendar.month_name[x])
            df['Time Period'] = df['month'] + " " + df['year'].astype(str)
            df=df.groupby(by=['Time Period'])['energy'].agg(['first','last'])
            df['Energy Consumption(KWh)']=df['last']-df['first']
            df=df.drop(['first','last'],axis=1)
        if(self.data['frequency'].lower()=='weekly'):
            df['week']= df['datetime'].dt.isocalendar().week
            df['year']= df['datetime'].dt.isocalendar().year
            df['Time Period']=df.apply(lambda x : getDateRangeFromWeek(x['year'],x['week']),axis=1)
            df=df.groupby(by=['Time Period'])['energy'].agg(['first','last'])
            df['Energy Consumption(KWh)']=df['last']-df['first']
            df=df.drop(['first','last'],axis=1)
        if(self.data['frequency'].lower()=='total'):
            period= df.iloc[-1]['datetime'].strftime("%d-%m-%Y") + " to " + df.iloc[0]['datetime'].strftime("%d-%m-%Y")
            con=df.iloc[-1]['energy']-df.iloc[0]['energy']
            energy={'Time Period':period,'Energy Consumption(KWh)':con}
            df=pd.DataFrame(energy,index=[0])


        """Graph Plotting and File saving"""
        
        
        df.plot.bar(x='Time Period',width=0.08,y='Energy Consumption(KWh)',legend=None)
        plt.xticks(rotation=0,horizontalalignment='center',fontweight='light',fontsize='medium')
        plt.savefig('temp.jpeg',bbox_inches="tight")
        df.to_html('temp.html',index=False)
        filestr=open('temp.html','r')
        str1='''<center><img src="logo.png" alt="logo" width='50' id='logo'>
        <h1>Bharat Heavy Electrical Limited</h1>
        <h3>IIOT Project</h3></center>
        <h4>Energy Consumption Report</h4>
        <h4>From:''' +str(self.data['fromdt'])+'''   To:''' +str(self.data['todt'])+'''</h4>
        <img src="temp.jpeg" alt="graph" id='graph'>
        '''
        str2=filestr.read()
        filestr.close()
        filestr=open('temp.html','w')
        filestr.write(str1+str2)
        filestr.close()
        dtnow=datetime.datetime.now()
        fdt=str(dtnow.year)+str(dtnow.month)+str(dtnow.day)+str(dtnow.hour)+str(dtnow.minute)+str(dtnow.second)
        path_wkhtmltopdf = r'D:\Coding\Python\wkhtmltopdf\bin\wkhtmltopdf.exe'
        config = pdf.configuration(wkhtmltopdf=path_wkhtmltopdf)
        optpath=os.path.join('static','reports',fdt+'.pdf')
        pdf.from_file('temp.html',optpath,configuration=config)
        os.remove('temp.jpeg')
        os.remove('temp.html')
        return(fdt+'.pdf')
        
        

class Report2:
    def __init__(self,inp):
        dict1=inp.to_dict()
        dict1['fromdt']=dict1['fromdt'].replace('T', ' ')
        dict1['todt']=dict1['todt'].replace('T', ' ')
        self.data=dict1
    
    def generate(self):
        
        
        """Getting the data from SQL Server"""
        
        conn = psycopg2.connect(database="postgres", user='postgres', password='4321ivar', host='localhost', port= '5432')
        cursor = conn.cursor()
        cursor.execute('SELECT datetime,'+self.data['sensor']+' FROM public.cotmac_iiot WHERE DateTime BETWEEN '+"'"+str(self.data['fromdt'])+"'"+' AND '+"'"+str(self.data['todt'])+"'"+'order by datetime;')
        df=pd.DataFrame(cursor.fetchall(),columns=['datetime','sensor'])
        cursor.close()
        conn.close()
        
        
        
        
        """Filtering data according to set values"""
        
        
        
        
        finaldf=pd.DataFrame(columns=['Result','From','To','Duration'])
        bit1=1
        bit2=1
        x=0
        while(x<len(df)):
            
            if(self.data['setval1']!=''):
                if(df['sensor'][x]<float(self.data['setval1'])):
                    if(bit1==1):
                        startdt=df['datetime'][x]
                        bit1=0
                elif(df['sensor'][x]>float(self.data['setval1'])):
                    if(bit1==0):
                        enddt=df['datetime'][x]
                        timediff=enddt-startdt
                        finaldf=finaldf.append({'Result':('Less Than '+self.data['setval1']),'From':startdt,'To':enddt,'Duration':timediff},ignore_index=True)
                        bit1=1
            
            
            if(self.data['setval2']!=''):
                if(df['sensor'][x]>float(self.data['setval2'])):
                    if(bit2==1):
                        startdt1=df['datetime'][x]
                        bit2=0
                elif(df['sensor'][x]<float(self.data['setval2'])):
                    if(bit2==0):
                        enddt1=df['datetime'][x]
                        timediff1=enddt1-startdt1
                        finaldf=finaldf.append({'Result':('Greater Than '+self.data['setval2']),'From':startdt1,'To':enddt1,'Duration':timediff1},ignore_index=True)
                        bit2=1
            x+=1
        
        
        
        else:
            if(bit1==0):
                enddt=df['datetime'][x-1]
                timediff=enddt-startdt
                finaldf=finaldf.append({'Result':('Less Than '+self.data['setval1']),'From':startdt,'To':enddt,'Duration':timediff},ignore_index=True)
            
            if(bit2==0):
                enddt1=df['datetime'][x-1]
                timediff1=enddt1-startdt1
                finaldf=finaldf.append({'Result':('Greater Than '+self.data['setval2']),'From':startdt1,'To':enddt1,'Duration':timediff1},ignore_index=True)

            

        
        

        """File saving"""
        
        
        finaldf.to_html('temp.html',index=False)
        filestr=open('temp.html','r')
        str1='''<center><img src="logo.png" alt="logo" width='50' id='logo'>
        <h1>Bharat Heavy Electrical Limited</h1>
        <h3>IIOT Project</h3></center>
        <h4>Min-Max Value</h4>
        <h5>'''+str(self.data['sensor'])+'''</h5>
        <h5>From:''' +str(self.data['fromdt'])+'''   To:''' +str(self.data['todt'])+'''</h5>
        <h5>Less Than: '''+str(self.data['setval1'])+'''</h5>
        <h5>Greater Than: '''+str(self.data['setval2'])+'''</h5>
        '''
        str2=filestr.read()
        filestr.close()
        filestr=open('temp.html','w')
        filestr.write(str1+str2)
        filestr.close()
        dtnow=datetime.datetime.now()
        fdt=str(dtnow.year)+str(dtnow.month)+str(dtnow.day)+str(dtnow.hour)+str(dtnow.minute)+str(dtnow.second)
        path_wkhtmltopdf = r'D:\Coding\Python\wkhtmltopdf\bin\wkhtmltopdf.exe'
        config = pdf.configuration(wkhtmltopdf=path_wkhtmltopdf)
        optpath=os.path.join('static','reports',fdt+'.pdf')
        print(optpath)
        pdf.from_file('temp.html',optpath,configuration=config)
        os.remove('temp.html')
        return(fdt+'.pdf')


class Report3:
    def __init__(self,inp):
        dict1=inp.to_dict()
        dict1['fromdt']=dict1['fromdt'].replace('T', ' ')
        dict1['todt']=dict1['todt'].replace('T', ' ')
        self.data=dict1
    
    def generate(self):
        
        """Getting the data from SQL Server"""
        conn = psycopg2.connect(database="postgres", user='postgres', password='4321ivar', host='localhost', port= '5432')
        cursor = conn.cursor()
        cursor.execute('SELECT datetime,'+self.data['sensor']+' FROM public.cotmac_iiot WHERE datetime BETWEEN '+"'"+str(self.data['fromdt'])+"'"+' AND '+"'"+str(self.data['todt'])+"'"+'order by datetime;')
        df=pd.DataFrame(cursor.fetchall(),columns=['datetime','sensor'])
        cursor.close()
        conn.close()
        
        
        """Filtering data according to set values"""
        
        df['sensor1']=df['sensor'].shift(450)
        df['level']=df['sensor']-df['sensor1']
        df['timediff']=df['datetime'].diff()
        #df=df[df['level']>30]
        df.to_csv('test.csv')
       # df=df[df['timediff']> timedelta(hours=2)]
        print(df)
        
        
            
        """File saving"""
        
        
        finaldf.to_html('temp.html',index=False)
        filestr=open('temp.html','r')
        str1='''<center><img src="logo.png" alt="logo" width='50' id='logo'>
        <h1>Bharat Heavy Electrical Limited</h1>
        <h3>IIOT Project</h3></center>
        <h4>Oil Filling Report</h4>
        <h4>From:''' +str(self.data['fromdt'])+'''   To:''' +str(self.data['todt'])+'''</h4>
        '''
        str2=filestr.read()
        filestr.close()
        filestr=open('temp.html','w')
        filestr.write(str1+str2)
        filestr.close()
        dtnow=datetime.datetime.now()
        fdt=str(dtnow.year)+str(dtnow.month)+str(dtnow.day)+str(dtnow.hour)+str(dtnow.minute)+str(dtnow.second)
        path_wkhtmltopdf = r'D:\Coding\Python\wkhtmltopdf\bin\wkhtmltopdf.exe'
        config = pdf.configuration(wkhtmltopdf=path_wkhtmltopdf)
        optpath=os.path.join('static','reports',fdt+'.pdf')
        pdf.from_file('temp.html',optpath,configuration=config)
        os.remove('temp.html')
        return(fdt+'.pdf')
    
    
    
    
    
    

class Report4:
    def __init__(self,inp):
        dict1=inp.to_dict()
        dict1['fromdt']=dict1['fromdt'].replace('T', ' ')
        dict1['todt']=dict1['todt'].replace('T', ' ')
        self.data=dict1
    
    def generate(self):
        
        
        """Getting the data from SQL Server"""
        
        conn = psycopg2.connect(database="postgres", user='postgres', password='4321ivar', host='localhost', port= '5432')
        cursor = conn.cursor()
        cursor.execute('SELECT datetime,cross_rail_vfd_current,vibraton_of_left_side_lead_screw,vibraton_of_right_side_lead_screw,temperature_of_left_side_lead_screw,temperature_of_right_side_lead_screw,inclination_x,inclination_y,vibraton_of_cross_rail_motor FROM public.cotmac_iiot WHERE datetime BETWEEN '+"'"+str(self.data['fromdt'])+"'"+' AND '+"'"+str(self.data['todt'])+"'"+'order by datetime;')
        df=pd.DataFrame(cursor.fetchall(),columns=['datetime','current','vibleft','vibright','templeft','tempright','incx','incy','vibmotor'])
        cursor.close()
        conn.close()

        
        """Grouping the data via frequency"""
        
        
        def getDateRangeFromWeek(p_year,p_week):
        
            firstdayofweek = datetime.datetime.strptime(f'{p_year}-{p_week}-1', "%Y-%W-%w").date()
            lastdayofweek = firstdayofweek + datetime.timedelta(days=6.9)
            return str(firstdayofweek)+' To '+ str(lastdayofweek)
        
        
        if(self.data['frequency'].lower()=='monthly'):
            df['month'] = df['datetime'].dt.month
            df['month'] = df['month'].apply(lambda x: calendar.month_name[x])
            df=df.groupby(by=['month']).mean()
            df['month']=df.index
            finaldf=df[['month','current','vibleft','vibright','templeft','tempright','incx','incy','vibmotor']]
        
        if(self.data['frequency'].lower()=='weekly'):
            df['week']= df['datetime'].dt.isocalendar().week
            df['year']= df['datetime'].dt.isocalendar().year
            df['week period']=df.apply(lambda x : getDateRangeFromWeek(x['year'],x['week']),axis=1)
            df=df.groupby(by=['week period']).mean()
            df['week period']=df.index
            finaldf=df[['week period','current','vibleft','vibright','templeft','tempright','incx','incy','vibmotor']]
        

        finaldf.columns=['Time Period','Avg Current','Avg Vibration Left Screw','Avg Vibration Right Screw','Avg Temperature Left Screw','Avg Temperature Right Screw','Avg Inclination X','Avg Inclination Y','Avg Vibration Cross Rail Motor']
        
        
        
        """Graph Plotting and File saving"""
        
        
        plt.plot('Time Period','Avg Current',data=finaldf)
        plt.plot('Time Period','Avg Vibration Left Screw',data=finaldf)
        plt.plot('Time Period','Avg Vibration Right Screw',data=finaldf)
        plt.plot('Time Period','Avg Temperature Left Screw',data=finaldf)
        plt.plot('Time Period','Avg Temperature Right Screw',data=finaldf)
        plt.plot('Time Period','Avg Inclination X',data=finaldf)
        plt.plot('Time Period','Avg Inclination Y',data=finaldf)
        plt.plot('Time Period','Avg Vibration Cross Rail Motor',data=finaldf)
        plt.xticks(rotation=0,horizontalalignment='center',fontweight='light',fontsize='medium')
        plt.savefig('temp.jpeg',bbox_inches="tight")
        finaldf.to_html('temp.html',index=False)
        filestr=open('temp.html','r')
        str1='''<center><img src="logo.png" alt="logo" width='50' id='logo'>
        <h1>Bharat Heavy Electrical Limited</h1>
        <h3>IIOT Project</h3></center>
        <h4>Energy Consumption Report</h4>
        <h4>From:''' +str(self.data['fromdt'])+'''   To:''' +str(self.data['todt'])+'''</h4>
        <img src="temp.jpeg" alt="graph" id='graph'>
        '''
        str2=filestr.read()
        filestr.close()
        filestr=open('temp.html','w')
        filestr.write(str1+str2)
        filestr.close()
        dtnow=datetime.datetime.now()
        fdt=str(dtnow.year)+str(dtnow.month)+str(dtnow.day)+str(dtnow.hour)+str(dtnow.minute)+str(dtnow.second)
        path_wkhtmltopdf = r'D:\Coding\Python\wkhtmltopdf\bin\wkhtmltopdf.exe'
        config = pdf.configuration(wkhtmltopdf=path_wkhtmltopdf)
        optpath=os.path.join('static','reports',fdt+'.pdf')
        pdf.from_file('temp.html',optpath,configuration=config)
        os.remove('temp.jpeg')
        os.remove('temp.html')
        return(fdt+'.pdf')