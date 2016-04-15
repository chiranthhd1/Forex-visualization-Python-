import pandas as pd
import csv
import matplotlib.pyplot as plt

# Taking inputs.
def currency_select():
	'''
	print "\t1, USD to INR \n",
	print "\t2, USD to GBP \n",
	print "\t3, USD to CAN \n",
	print "\t4, USD to EUR\n",
	print "\t5, USD to AUD \n",
	'''	
	file_dict = {"1":'usdtoinr.csv', "2":"usdgbp.csv","3":'USDCAN.csv', "4":"usdeuro.csv","5":"usd_to_aud.csv","6":"usdtocny.csv"}	
#	inputfile = raw_input("\tPlease enter the currency from above: ")

	input_year = raw_input("\tEnter year to be analysed ")	
	dateparse = lambda dates: pd.datetime.strptime(dates, '%m/%d/%Y')	
	#for keys in file_dict.keys():
	#	if inputfile == keys:
			#file1 = pd.read_csv(file_dict[keys])
			#myData = list ( csv.reader ( open (file_dict[keys])))


	plot_data_usdinr = pd.read_csv(file_dict["1"],index_col='Date',date_parser=dateparse)
	plot_data_usdgbp = pd.read_csv(file_dict["2"],index_col='Date',date_parser=dateparse)
	plot_data_usdcan = pd.read_csv(file_dict["3"],index_col='Date',date_parser=dateparse)
	plot_data_usdeur = pd.read_csv(file_dict["4"],index_col='Date',date_parser=dateparse)
	plot_data_usdaud = pd.read_csv(file_dict["5"],index_col='Date',date_parser=dateparse)
	plot_data_usdcny = pd.read_csv(file_dict["6"],index_col='Date',date_parser=dateparse)


#		else:
#			pass	
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

#	plt.title('Time Series graph ')
	plt.show()

plot_data_usdinr,plot_data_usdgbp,plot_data_usdcan,plot_data_usdeur,plot_data_usdaud,plot_data_usdcny,input_year = currency_select()
plot_func(plot_data_usdinr,plot_data_usdgbp,plot_data_usdcan,plot_data_usdeur,plot_data_usdaud,plot_data_usdcny,input_year)


