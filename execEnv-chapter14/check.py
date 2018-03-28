# !/usr/bin/env python
# coding=utf-8
import xlrd

"""对比"""

f = xlrd.open_workbook("医工科库存20170622.xls", 'r')
g = xlrd.open_workbook("医院最新库存-20170623.xlsx", 'r')

currentSheet = f.sheet_by_index(0)
compareSheet = g.sheet_by_index(1)
# print currentSheet.name, currentSheet.nrows, currentSheet.ncols
# print compareSheet.name, compareSheet.nrows, compareSheet.ncols

compareLines = compareSheet.nrows
print currentSheet.nrows, compareSheet.nrows
item = 4
fArray = []
fObj = {}
for item in (g for g in range(4, compareLines - 3)):
    currentItem = compareSheet.row_values(item)

    fObj['code'] = int(currentItem[0])
    fObj['price'] = float(currentItem[5])
    fObj['stores'] = int(currentItem[4])
    fArray.append(fObj)

fArray.sort(key=lambda x: x['code'])

print fArray

def excel2array():
    '将excel转化为数组并输出'

def getSortArray(oriArray):
    '输出排好序的数组对象'
    oriArray.sort(key=lambda x: x['code'])
    return oriArray

# TODO finish this func for check diff between excel files
