import pandas as pd
import csv
'''
myData = []
index = 0 
start1 = 0
end1 = 0
'''
# Taking inputs.
def currency_select():
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
			#o = open(file_dict[keys], 'r')
			file1 = pd.read_csv(file_dict[keys])
			myData = list ( csv.reader ( open (file_dict[keys])))
		else:
			pass	
	return (file1,myData)
def date_select(myData):
	print("-----------Enter Dates-----------")
	in1 = raw_input(" Please enter start date in format m/dd/yyyy (eg:3/11/2016) : ")
	in2 = raw_input(" Please enter end date in format m/dd/yyyy (eg:3/11/2016) : ")
	print("\nOUTPUT:")
	temp=0
	temp=int(temp)
	for i in myData:
        	if myData[temp][0] == in1:
                	start= temp
        	elif myData[temp][0] == in2:
     	        	end = temp
        	else:
                	pass
        	temp+=1

	start = int(start)
	end = int(end)
	return (start,end)

#The below code works using pandas library dealing with data frames.
def output(start,end,file1):
	if end > start:

		value = file1.iloc[start-1:end, :]
	else:
		value = file1.iloc[end+1:start+1, :]

	print value	
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

file1,myData = currency_select()
start1,end1 = date_select(myData)
output(start1,end1,file1)


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
