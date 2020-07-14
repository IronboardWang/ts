import openpyxl

wb = openpyxl.load_workbook("transaction.xlsx")
print(wb.sheetnames)