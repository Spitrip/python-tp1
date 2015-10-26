import xlrd
#-------------------------------
__author__ = 'Igors Sigalovs'

def getExcelFileToSqlite3(fileDir):
    wb = xlrd.open_workbook(fileDir)
    for name in wb.sheet_names():
        sheet = wb.sheet_by_name(name)
        print(sheet.cell_value(0, 0))
        print(sheet.cell_value(0, 1))
        print(sheet.cell_value(0, 2))
        print(sheet.cell_value(0, 3))
        print(sheet.cell_value(0, 4))

getExcelFileToSqlite3('teses.xls')