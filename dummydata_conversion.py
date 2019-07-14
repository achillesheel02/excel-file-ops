import xlrd
import pandas as pd

excelfile=pd.ExcelFile("dummydata.xlsx")

for i in range(1,11):
    dframe=excelfile.parse("Sheet"+str(i))
    dframe.to_csv("Sheet"+str(i)+".csv",sep=",")
    dframe=None #TODO check if this line is really needed