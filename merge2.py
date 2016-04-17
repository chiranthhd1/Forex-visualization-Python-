import pandas as pd
import csv
import matplotlib.pyplot as plt
import os
Currencies_dict = {'usdtoinr.csv':"USD to Indian Ruppee", "usdgbp.csv":"USD to Great Britan Pound",'USDCAN.csv':"USD to Canadian Dollar", "usdeuro.csv" : "USD to Euro","usd_to_aud.csv":"USD to Australian Dollar", "usdtocny.csv":"USD to Chinese Yen"}
# Taking inputs.
def currency_select():
	os.system('clear')
	print ("\n\n")
	print("\t---------------------------------Choose Currency----------------------------------")
	print "\t1, USD to INR \n",
	print "\t2, USD to GBP \n",
	print "\t3, USD to CAN \n",
	print "\t4, USD to EUR\n",
	print "\t5, USD to AUD \n",
	print "\t6, USD to CNY \n",
	file_dict = {1:'usdtoinr.csv', 2:"usdgbp.csv",3:'USDCAN.csv', 4:"usdeuro.csv",5:"usd_to_aud.csv", 6:"usdtocny.csv"}
	while True:
        	try:
			inputfile = int(raw_input("\tPlease select any currency from above: "))
                	break
        	except  ValueError:
                	print "\n\tError!! Please Enter an interger from 1 to 6 , Try again"
		
	

	dateparse = lambda dates: pd.datetime.strptime(dates, '%m/%d/%Y')	
	for keys in file_dict.keys():
		if inputfile == keys:
			file1 = pd.read_csv(file_dict[keys])
			myData = list ( csv.reader ( open (file_dict[keys])))
			plot_data = pd.read_csv(file_dict[keys],index_col='Date',date_parser=dateparse)
		else:
			pass	
	s = file_dict[inputfile]
	chosen_curr = Currencies_dict[s]
	end_date = file1["Date"].iloc[-1]
	start_date = file1["Date"].iloc[0]
	return (file1,myData,plot_data,chosen_curr,end_date,start_date)


def date_select(myData,chosen_curr,end_date,start_date):
	os.system('clear')	
	print ("\n\n")
	print " \tSelected option is "+chosen_curr
	print ("\tData Ranges from '%s' to '%s'") %(end_date,start_date)	
	print ("\n")	
	print("\t---------------------------------Enter Dates----------------------------------")
	in1 = raw_input(" \tPlease enter start(latest) date in format m/dd/yyyy (eg:3/11/2016) : ")
	in2 = raw_input(" \tPlease enter end(old) date in format m/dd/yyyy (eg:3/11/2010)      : ")
	print ("\t-----------------------------------------------------------------------------")
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
def output(start,end,file1,plot_data,in1,in2,chosen_curr):
	if end > start:

		value = file1.iloc[start-1:end, :]
	else:
		value = file1.iloc[end+1:start+1, :]
	
	maxprice = value.iloc[:, 1].values.max()
	index = value.iloc[:, 1].values.argmax()
	de = value.iloc[index]
	os.system('clear')	
	print ("\n\n")
	print "\tSelected option is "+chosen_curr
	print ("\n")	
	print ("\t----------------------------------Output--------------------------------------")
	print("\n\tThe maximum Price is \t\t %s    on \t %s" %(maxprice,de['Date']))

	x=value.iloc[0,1]
	y=value.iloc[-1,1]
	print("\n\tThe percentage change from \t%s  to \t %s  is   %.2f percent " %(value.iloc[0,0], value.iloc[-1,0],(x-y)/x * 100))

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
	plt.xlabel('Time Elapsed')
	plt.ylabel(f)
	plt.title('Time Series graph ')
	plt.show()


# Taking inputs.
def annual_select():
	os.system('clear')
	print ("\n\n")
		
	file_dict = {"1":'usdtoinr.csv', "2":"usdgbp.csv","3":'USDCAN.csv', "4":"usdeuro.csv","5":"usd_to_aud.csv","6":"usdtocny.csv"}

	input_year = raw_input("\tEnter year to be analysed ")	
	dateparse = lambda dates: pd.datetime.strptime(dates, '%m/%d/%Y')	

	plot_data_usdinr = pd.read_csv(file_dict["1"],index_col='Date',date_parser=dateparse)
	plot_data_usdgbp = pd.read_csv(file_dict["2"],index_col='Date',date_parser=dateparse)
	plot_data_usdcan = pd.read_csv(file_dict["3"],index_col='Date',date_parser=dateparse)
	plot_data_usdeur = pd.read_csv(file_dict["4"],index_col='Date',date_parser=dateparse)
	plot_data_usdaud = pd.read_csv(file_dict["5"],index_col='Date',date_parser=dateparse)
	plot_data_usdcny = pd.read_csv(file_dict["6"],index_col='Date',date_parser=dateparse)
	
	return (plot_data_usdinr,plot_data_usdgbp,plot_data_usdcan,plot_data_usdeur,plot_data_usdaud,plot_data_usdcny,input_year)

def plot_func(plot_data_usdinr,plot_data_usdgbp,plot_data_usdcan,plot_data_usdeur,plot_data_usdaud,plot_data_usdcny,input_year):
	ts_inr = plot_data_usdinr['Price']
	ts_gbp = plot_data_usdgbp['Price']
	ts_can = plot_data_usdcan['Price']
	ts_eur = plot_data_usdeur['Price']
	ts_aud = plot_data_usdaud['Price']
	ts_cny = plot_data_usdcny['Price']
	
	ts1_inr = ts_inr[input_year]	
	ts1_gbp = ts_gbp[input_year]	
	ts1_can = ts_can[input_year]	
	ts1_eur = ts_eur[input_year]	
	ts1_aud = ts_aud[input_year]	
	ts1_cny = ts_cny[input_year]	
	
	f, axes = plt.subplots(6, 1)
	axes[0].plot(ts1_inr, color = "r")
	axes[0].set_ylabel('USD to INR')

	axes[1].plot(ts1_gbp, color = 'b')
	axes[1].set_ylabel('USD to GBP')

	axes[2].plot(ts1_can,  color = 'maroon')
	axes[2].set_ylabel('USD to CAN')

	axes[3].plot(ts1_eur,  color = 'g')
	axes[3].set_ylabel('USD to EUR')

	axes[4].plot(ts1_aud,  color = 'k')
	axes[4].set_ylabel('USD to AUD')

	axes[5].plot(ts1_cny, color = 'm')
	axes[5].set_ylabel('USD to CNY')

	plt.show()

def plot_func_chng(plot_data_usdinr,plot_data_usdgbp,plot_data_usdcan,plot_data_usdeur,plot_data_usdaud,plot_data_usdcny,input_year):
	ts_inr = plot_data_usdinr['Change %']
	ts_gbp = plot_data_usdgbp['Change %']
	ts_can = plot_data_usdcan['Change %']
	ts_eur = plot_data_usdeur['Change %']
	ts_aud = plot_data_usdaud['Change %']
	ts_cny = plot_data_usdcny['Change %']
	
	ts1_inr = ts_inr[input_year].tolist()
	ts1_gbp = ts_gbp[input_year].tolist()	
	ts1_can = ts_can[input_year].tolist()	
	ts1_eur = ts_eur[input_year].tolist()	
	ts1_aud = ts_aud[input_year].tolist()	
	ts1_cny = ts_cny[input_year].tolist()	
        ts1_inr_chng = []
        ts1_gbp_chng = []
        ts1_can_chng = []
        ts1_eur_chng = []
        ts1_aud_chng = []
        ts1_cny_chng = []
        for row in ts1_inr:
                ts1_inr_chng.append(float((row.split("%", 1))[0]))
        #print ts1_inr_chng
        for row in ts1_gbp:
                ts1_gbp_chng.append(float((row.split("%", 1))[0]))
        for row in ts1_can:
                ts1_can_chng.append(float((row.split("%", 1))[0]))
        for row in ts1_eur:
                ts1_eur_chng.append(float((row.split("%", 1))[0]))
        for row in ts1_aud:
                ts1_aud_chng.append(float((row.split("%", 1))[0]))
        for row in ts1_cny:
                ts1_cny_chng.append(float((row.split("%", 1))[0]))
        chng=[]
        chng.append(sum(ts1_inr_chng))
        chng.append(sum(ts1_gbp_chng))
        chng.append(sum(ts1_can_chng))
        chng.append(sum(ts1_eur_chng))
        chng.append(sum(ts1_aud_chng))
        chng.append(sum(ts1_cny_chng))

        x = [1,2,3,4,5,6]
        xtik = ['INR', 'GBP', 'CAN', 'EUR', 'AUD', 'CNY']
        plt.bar(x,chng,0.5,color='b')
        plt.axhline(0, color='k')
        plt.xticks(x,xtik)
        plt.show()

os.system('clear')
print ("\n")
print ("\n")
print("\t---------------------------------Choose Process----------------------------------")
print ("\t What do you want to see")
print ("\t 1. Consolidated analysis on annual basis ")
print ("\t 2. Analysis of a particular currency in a specified time range ")
print ("\t 3. Change Percentage for selected year")
while True:
        try:
                user_in = int(raw_input(" \t Please enter 1 ,2 or 3: "))
                break
        except  ValueError:
                print "\n\t Error!! Please Enter an interger from 1 to 3 , Try again"

if user_in == 2:
	file1,myData,plot_data,chosen_curr,end_date,start_date = currency_select()
	start1,end1,in1,in2 = date_select(myData,chosen_curr,end_date,start_date)
	output(start1,end1,file1,plot_data,in1,in2,chosen_curr)
elif user_in == 1:
        plot_data_usdinr,plot_data_usdgbp,plot_data_usdcan,plot_data_usdeur,plot_data_usdaud,plot_data_usdcny,input_year = annual_select()
        plot_func(plot_data_usdinr,plot_data_usdgbp,plot_data_usdcan,plot_data_usdeur,plot_data_usdaud,plot_data_usdcny,input_year)
else:
        plot_data_usdinr,plot_data_usdgbp,plot_data_usdcan,plot_data_usdeur,plot_data_usdaud,plot_data_usdcny,input_year = annual_select()
        plot_func_chng(plot_data_usdinr,plot_data_usdgbp,plot_data_usdcan,plot_data_usdeur,plot_data_usdaud,plot_data_usdcny,input_year)



       


