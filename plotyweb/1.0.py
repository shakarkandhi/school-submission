import pandas as pd
import pyodbc
import plotly.express as px 
pd.options.plotting.backend = "plotly"
server = 'DESKTOP-JGFHFID\SQLEXPRESS' 
database = 'rpi' 
username = 'sa' 
password = '4321ivar' 
cnxn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)
SQL_Query = pd.read_sql_query(
'''select * from rpi.dbo.table1 order by [PLC_TIME]''', cnxn)

df = pd.DataFrame(SQL_Query)
print (df)
#fig = df.plot.line(x='PLC_TIME',y='CURRENT')
#fig.show()
fig1=px.line(x=df['PLC_TIME'], y = df['CURRENT'])
fig1.write_html('q.html')