 # -*- coding: utf-8 -*-

import xlrd
import xlwt
from datetime import date,datetime

def read_excel():
    # 打开文件
    workbook = xlrd.open_workbook(r'F:\瑜伽课程可.xlsx')
    # 获取所有sheet
    # print(workbook.sheet_names()) # [u'sheet1', u'sheet2']
    # sheet1_name = workbook.sheet_names()[0]

    # 根据sheet索引或者名称获取sheet内容
    # sheet1 = workbook.sheet_by_index(0) # sheet索引从0开始
    sheet2 = workbook.sheet_by_name('Sheet1')

    # sheet的名称，行数，列数
    print(sheet2.name,sheet2.nrows,sheet2.ncols)

    # 获取整行和整列的值（数组）
    # rows = sheet2.row_values(3) # 获取第四行内容
    cols = sheet2.col_values(0) # 获取第三列内容
    # print(rows)
    # print(cols)
    for val in cols:
    	if val !="id":
    		print("%d," % int(val))

    # 获取单元格内容
    # print(sheet2.cell(1,0).value.encode('utf-8'))
    # print(sheet2.cell_value(1,0).encode('utf-8'))
    # print(sheet2.row(1)[0].value.encode('utf-8'))
    
    # # 获取单元格内容的数据类型
    # print(sheet2.cell(1,0).ctype)

if __name__ == '__main__':
    read_excel()