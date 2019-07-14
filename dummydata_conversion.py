import xlrd
import pandas as pd

excelfile=pd.ExcelFile("dummydata.xlsx")
i=1
while i <11:
    dframe=excelfile.parse("Sheet"+str(i))
    filename="Sheet"+str(i)+".csv"
    dframe.to_csv(filename,sep=",")  #had  to change bc of unicode error in string function  UnicodeEncodeError: 'ascii' codec can't encode character u'\xe9' in position 3: ordinal not in range(128)
    dframe=None #TODO check if this line is really needed
    print("done with "+str(i))
    i+=1