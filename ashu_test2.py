#Returns the number of a particular row in a csv file.
import csv
start = raw_input("Enter starting date: ")
end = raw_input("Enter ending date: ")
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

file = open('usdtoinr.csv', 'r')
myData1 = csv.reader(file)
index = start1
for row in myData1:
	if row[0] == start:
		print row[1]
		index += 1
	elif (index > start1 and index <= end1):
		print row[1]
		index += 1
	elif row[0] == end:
		print row[1]
		exit()
	else:
		pass

	
