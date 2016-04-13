import pandas as pd
import csv
import matplotlib.pyplot as plt

# Taking inputs.
def currency_select():

	print "1, USD to INR \n",
	print "2, USD to GBP \n",
	print "3, USD to CAN \n",
	print "4, USD to EUR\n",
	print "5, USD to AUD \n",
	file_dict = {"1":'usdtoinr.csv', "2":"usdgbp.csv","3":'USDCAN.csv', "4":"usdeuro.csv","5":"usd_to_aud.csv"}	
	inputfile = raw_input("please enter the currency from above: ")	
	dateparse = lambda dates: pd.datetime.strptime(dates, '%m/%d/%Y')	
	for keys in file_dict.keys():
		if inputfile == keys:
			file1 = pd.read_csv(file_dict[keys])
			myData = list ( csv.reader ( open (file_dict[keys])))
			plot_data = pd.read_csv(file_dict[keys],index_col='Date',date_parser=dateparse)
		else:
			pass	
	return (file1,myData,plot_data)


def date_select(myData):
	print("-----------Enter Dates-----------")
	in1 = raw_input(" Please enter start(latest) date in format m/dd/yyyy (eg:3/11/2016) : ")
	in2 = raw_input(" Please enter end(old) date in format m/dd/yyyy (eg:3/11/2010) : ")
	print("\nOUTPUT:")
	temp=0
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
	return (start,end,in1,in2)

#The below code works using pandas library dealing with data frames.
def output(start,end,file1,plot_data,in1,in2):
	if end > start:

		value = file1.iloc[start-1:end, :]
	else:
		value = file1.iloc[end+1:start+1, :]
	
	maxprice = value.iloc[:, 1].values.max()
	index = value.iloc[:, 1].values.argmax()
	de = value.iloc[index]
	print("\n\tThe maximum Price is \t\t %s    on \t %s" %(maxprice,de['Date']))

	x=value.iloc[0,1]
	y=value.iloc[-1,1]
	print("\n\tThe percentage change from \t %s  to \t %s  is   %.2f percent " %(value.iloc[0,0], value.iloc[-1,0],(x-y)/x * 100))

	maxprice = value.iloc[:, 2].values.max()
	index = value.iloc[:, 2].values.argmax()
	de = value.iloc[index]
	print("\n\tThe maximum opening Price is \t %s    on \t %s" %(maxprice,de['Date']))

	maxprice = value.iloc[:, 3].values.max()
	index = value.iloc[:, 3].values.argmax()
	de = value.iloc[index]
	print("\n\tThe maximum High Price is \t %s    on \t %s" %(maxprice,de['Date']))

	maxprice = value.iloc[:, 4].values.max()
	index = value.iloc[:, 4].values.argmax()
	de = value.iloc[index]
	print("\n\tThe maximum Low Price is \t %s     on \t %s" %(maxprice,de['Date']))
	
	#print plot_data
	ts = plot_data['Price']
	ts1 = ts[in1:in2]	
	plt.plot(ts1)
	plt.show()


file1,myData,plot_data = currency_select()
start1,end1,in1,in2 = date_select(myData)
output(start1,end1,file1,plot_data,in1,in2)


