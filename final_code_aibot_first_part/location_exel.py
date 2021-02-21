import pandas as pd
import openpyxl
from pandas import ExcelWriter
import pytest

#df = pd.DataFrame(location)

def location_excel_read_data():
        df = pd.read_excel('location.xlsx')
        location = df.values.tolist()
        return location
def test():
        location = location_excel_read_data()
test()
'''
location = list(set(ghamari_dic))
df = pd.DataFrame(location)
writer = pd.ExcelWriter('location.xlsx')
df.to_excel(writer)
writer.save()'''