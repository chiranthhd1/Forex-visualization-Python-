import csv
import numpy as np
import datetime as dt


year =0
priceUsd_Eur =[]
priceUsd_Eur =[]
priceUsd_gbp =[]
priceUsd_cny =[]
priceUsd_inr =[]
def read_file():
    file_dict = {"1":'usdeuro.csv',}
        #{"1":'usdtoinr.csv', "2":"usdgbp.csv","3":'USDCAN.csv', "4":"usdeuro.csv","5":"usd_to_aud.csv"}
    for keys in file_dict.keys():
        a = list ( csv.reader ( open (file_dict[keys])))
        c = 0
        d = 0
        c=int(c)
        for i in a:
            j = a[c][0]
            j = j.split("/")
            if j[2] == year:
                    d = a[c]
                    print d
                    break
            else:
                    pass
            c+=1
        d = int(d)
        print d



year = int(raw_input("Enter the year for which you need to see the consolidated report wrt USD in range (1990-2016):  "))
read_file()



# print year
# with open('usd_euro.csv', 'rb') as f:
#     reader = csv.reader(f)
#     header = next(reader)
#     for row in reader:
#         row = [i.split('\t') for i in row]
#         for word in row:
#             wordstr = ''.join(word)
#             date_object= dt.datetime.strptime(wordstr,'%b %d, %Y')
#             if year == date_object.year:
#                 rowStr = ''.join(row[1])
#                 #rowint = map(int, rowStr)
#                 priceUsd_Eur.append(rowStr)
#                 #priceEuroUsd.append(1/rowStr)

#
# year = int(raw_input("Enter the year for which you need to see the consolidated report wrt USD:  "))
# #print year
# price_usd =[]
# w = load_workbook(filename='usdeuro.xlsx', use_iterators = True , read_only=True)
# p = w.get_sheet_by_name('Sheet1')
# maxrow = p.get_highest_row()
# print maxrow
# for row_num in range(2,maxrow):
#     cell_val = p.cell(row = row_num, column = 1).value
#     date_object= dt.datetime.strptime(cell_val,'%b %d, %Y')
#     if date_object.year == year:
#          price_usd.append(int(p.cell(row = row_num, column = 2).value))
# print price_usd



