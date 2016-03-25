
import csv
# Inputs are taken in reverse order bacause data in .csv file is from present date to past date.
end = raw_input("Enter starting date: ")
start = raw_input("Enter ending date: ")
o = open('usdtoinr.csv', 'r')
myData = csv.reader(o)
index = 0 
start1 = 0
end1 = 0

for row in myData:
	if row[0] == start:
		start1 = index
		index += 1
	elif row[0] == end:
		end1 = index
		pass
	else:
		index += 1
o.close()
# Code under quotes is traditional Python code dealing with lists.
"""
file = open('usdtoinr.csv', 'r')
myData1 = csv.reader(file)
index = start1
for row in myData1:
	if row[0] == start:
		print row[:]
		index += 1
	elif (index > start1 and index <= end1):
		print row[:]
		index += 1
	elif row[0] == end:
		print row[:]
		exit()
	else:
		pass

"""
#The below code works using pandas library dealing with data frames.
import pandas as pd

file = pd.read_csv('usdtoinr.csv', index_col = 0)

print (file.iloc[start1-1:end1, :])

