ipmort pyodbc

conn = pyodbc.connect('Driver={SQL Server};'
                      'Server=DESKTOP-8G2S04I\WINCC;'
                      'Database=DATA_WINCC;'
                      'Trusted_Connection=yes;')

cursor = conn.cursor()
cursor.execute('SELECT * FROM DATA_WINCC.dbo.Table_1')
