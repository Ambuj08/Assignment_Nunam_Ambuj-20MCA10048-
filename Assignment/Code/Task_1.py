import pandas as pd
import cProfile
#define Function
def data_collecter(sheets,df,detailsDF,detailsVolDF,detailsTempDF):
    for x in sheets:
        if x.startswith('Detail_67_'):
            detailsDF = detailsDF.append(df[x], ignore_index=True)
        elif x.startswith('DetailVol_67_'):
            detailsVolDF = detailsVolDF.append(df[x], ignore_index=True)
        elif x.startswith('DetailTemp_67_'):
            detailsTempDF = detailsTempDF.append(df[x], ignore_index=True)
    return detailsDF, detailsVolDF, detailsTempDF    

xls = pd.ExcelFile(r'../../Data/data.xlsx')
xls1 = pd.ExcelFile(r'../../Data/data_1.xlsx')

df1 = pd.read_excel(xls, None) #read Data
df2 = pd.read_excel(xls1, None) #read Data_1

#making sheets of data
sheets1 = df1.keys()
sheets2 = df2.keys()
detailsDF = pd.DataFrame()
detailsVolDF = pd.DataFrame()
detailsTempDF = pd.DataFrame()

#Call cProfile for Unit Test
cProfile.run("data_collecter(sheets1, df1, detailsDF, detailsVolDF, detailsTempDF)")

detailsDF, detailsVolDF, detailsTempDF = data_collecter(sheets1, df1, detailsDF, detailsVolDF, detailsTempDF)
detailsDF, detailsVolDF, detailsTempDF = data_collecter(sheets2, df2, detailsDF, detailsVolDF, detailsTempDF)
#convert into CSV file
detailsDF.to_csv(r'../../Results/Task_1/detail.csv', index=False)
detailsVolDF.to_csv(r'../../Results/Task_1/detailVol.csv', index=False)
detailsTempDF.to_csv(r'../../Results/Task_1/detailTemp.csv', index=False)
