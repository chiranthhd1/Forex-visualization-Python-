import pandas as pd
import csv
import matplotlib.pyplot as plt

# Taking inputs.
def currency_select():

	print "\t1, USD to INR \n",
	print "\t2, USD to GBP \n",
	print "\t3, USD to CAN \n",
	print "\t4, USD to EUR\n",
	print "\t5, USD to AUD \n",
	file_dict = {"1":'usdtoinr.csv', "2":"usdgbp.csv","3":'USDCAN.csv', "4":"usdeuro.csv","5":"usd_to_aud.csv"}	
	inputfile = raw_input("\tPlease enter the currency from above: ")
	input_year = raw_input("\tEnter year to be analysed ")	
	dateparse = lambda dates: pd.datetime.strptime(dates, '%m/%d/%Y')	
	for keys in file_dict.keys():
		if inputfile == keys:
			#file1 = pd.read_csv(file_dict[keys])
			#myData = list ( csv.reader ( open (file_dict[keys])))
			plot_data = pd.read_csv(file_dict[keys],index_col='Date',date_parser=dateparse)
		else:
			pass	
	return (plot_data,input_year)


def plot_func(plot_data,input_year):
	ts = plot_data['Price']
	ts1 = ts[input_year]	
	plt.plot(ts1)
	plt.xlabel('Time Elapsed')
	plt.ylabel('USD to INR rate')
	plt.title('Time Series graph ')
	plt.show()

plot_data,input_year = currency_select()
plot_func(plot_data,input_year)


