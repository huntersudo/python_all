'''


'''
import openpyxl

# return Workbook object ,just like File Object
wb = openpyxl.load_workbook("file/es_02.xlsx")

print(type(wb))

print(wb.get_sheet_names())  # return list

sheet = wb.get_sheet_by_name('es_01_1')

print(type(sheet))  # Worksheet
print(sheet)
print(sheet.title)  # name

a_sheet = wb.get_active_sheet()

print(a_sheet.title)
