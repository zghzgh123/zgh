import xlrd

class lei():
    list1=[]
    a=xlrd.open_workbook('ddts.py')
    b=a.sheet_by_index(0)
    c=b.nrows
    for  i in range(1,c):
        list1.append(b.row_values(i))


