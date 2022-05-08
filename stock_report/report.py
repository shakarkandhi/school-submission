import pandas as pd


stock = []
stock.append(input("Enter Stock file name: "))
stock.append(input("Enter Stock sheet name: "))
stock.append(input("Enter Stock material column name: "))
stock.append(input("Enter Stock quantity column name: "))
print(stock)
buisness = []
buisness.append(input("Enter Buisness file name: "))
buisness.append(input("Enter Buisness sheet name: "))
buisness.append(input("Enter Buisness material column name: "))
buisness.append(input("Enter Buisness quantity column name: "))
buisness.append(input("Enter Buisness remarks column name: "))
print(buisness)
output = []
output.append(input("Enter Output File name: "))
output.append(input("Enter Output Sheet name: "))


stockdf = pd.read_csv(stock[0]+'.csv', encoding='latin1')
buisnessdf = pd.read_csv(buisness[0]+'.csv', encoding='latin1')


buisnessdf = buisnessdf[buisnessdf[buisness[4]] != 'billed']
buisnessdf = buisnessdf[buisnessdf[buisness[2]] != None]
buisnessdf.index = pd.RangeIndex(len(buisnessdf.index))


for i in stockdf.columns:
    if i != stock[2] and i != stock[3]:
        del stockdf[i]
for i in buisnessdf.columns:
    if i != buisness[2] and i != buisness[3]:
        del buisnessdf[i]


finaldf = pd.DataFrame(columns=['Material', 'Required', 'Available'])
finaldf['Material'] = buisnessdf[buisness[2]]
finaldf['Required'] = buisnessdf[buisness[3]]


for i in range(0, len(finaldf['Material'])):
    for j in range(0, len(stockdf[stock[2]])):
        if(str(finaldf['Material'][i]).replace("-", "") == str(stockdf[stock[2]][j]).replace(" ", "")):
            finaldf['Available'][i] = stockdf[stock[3]][j]

finaldf.to_excel(output[0]+'.xlsx', sheet_name=output[1], index=0)
