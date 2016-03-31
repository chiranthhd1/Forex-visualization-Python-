import pandas as pd
import csv
# Taking inputs.

print "1, USD to INR \n",
print "2, USD to GBP \n",
print "3, USD to CAN \n",
print "4, USD to EUR\n",
print "5, USD to AUD \n",
inputfile = raw_input("please enter the currency from above: ")
file_dict = {"1":'usdtoinr.csv', "2":"usdgbp.csv","3":'USDCAN.csv', "4":"usdeuro.csv","5":"usd_to_aud.csv"}
for keys in file_dict.keys():
	if inputfile == keys:
		#file = pd.read_csv(, index_col = 0)
		#a = list ( csv.reader ( open (file_dict[keys])))
		o = open(file_dict[keys], 'r')
		file = pd.read_csv(file_dict[keys])
	else:
		pass

print("-----------Enter Dates-----------")
end = raw_input(" Please enter start date in format m/dd/yyyy (eg:3/11/2016) : ")
start = raw_input(" Please enter end date in format m/dd/yyyy (eg:3/11/2016) : ")
print("\nOUTPUT:")

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


#The below code works using pandas library dealing with data frames.

if end1 > start1:

	value = file.iloc[start1-1:end1, :]
else:
	value = file.iloc[end1+1:start1+1, :]

maxprice = value.iloc[:, 1].values.max()
index = value.iloc[:, 1].values.argmax()
print("\nThe maximum Price is %s on %s" %(maxprice,value.iloc[index]))

x=value.iloc[0,1]
y=value.iloc[-1,1]
print("\nThe percentage change from %s to %s is %.2f percent " %(value.iloc[0,0], value.iloc[-1,0],(x-y)/x * 100))

maxprice = value.iloc[:, 2].values.max()
index = value.iloc[:, 2].values.argmax()
print("\nThe maximum Price is %s on %s" %(maxprice,value.iloc[index]))

maxprice = value.iloc[:, 3].values.max()
index = value.iloc[:, 3].values.argmax()
print("\nThe maximum Price is %s on %s" %(maxprice,value.iloc[index]))

maxprice = value.iloc[:, 4].values.max()
index = value.iloc[:, 4].values.argmax()
print("\nThe maximum Price is %s on %s" %(maxprice,value.iloc[index]))


'''
#The below code works using pandas library dealing with data frames.


value = file.iloc[start1-1:end1, :]

maxPrice = 0
maxprice = file.iloc[start1-1:end1, 1].values.max()
index = file.iloc[start1-1:end1, 1].values.argmax()
print("\nThe maximum Price is %s on %s" %(maxprice,value.iloc[index]))
x=file.iloc[start1-1, 1]
y=file.iloc[end1-1, 1]
print("\nThe percentage change from %s to %s is %.2f percent " %(file.iloc[end1-1,0], file.iloc[start1-1,0],(x-y)/x * 100))

maxprice = file.iloc[start1-1:end1, 2].values.max()
index = file.iloc[start1-1:end1, 2].values.argmax()
print("\nThe maximum Open Price is %s on %s" %(maxprice,value.iloc[index]))

maxprice = file.iloc[start1-1:end1, 3].values.max()
index = file.iloc[start1-1:end1, 3].values.argmax()
print("\nThe maximum High Price is %s on %s" %(maxprice,value.iloc[index]))

maxprice = file.iloc[start1-1:end1, 4].values.max()
index = file.iloc[start1-1:end1, 4].values.argmax()
print("\nThe maximum Low Price is %s on %s" %(maxprice,value.iloc[index]))

'''
