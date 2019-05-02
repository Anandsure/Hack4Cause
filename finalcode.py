import xlrd
loc = ("table123.xlsx")
wb= xlrd.open_workbook(loc)
sheet = wb.sheet_by_index(0)
sheet.cell_value(0,0)
print("\t\t\t",sheet.cell_value(0,0))
for i in range(2,sheet.nrows):
    l1=sheet.row_values(i)
    print("Name: ",l1[0])
    '''"Time Slot: ",l1[1],"Location: ",l1[2],"Duty: ",l1[3])'''
    print("\n")
    

