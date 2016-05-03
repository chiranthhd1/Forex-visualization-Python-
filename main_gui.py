import pandas as pd
import csv
import pylab
import webbrowser
import matplotlib.pyplot as plt
import os
from  termcolor import colored
import flask
from flask import render_template
import easygui as eg

Currencies_dict = {'usdtoinr.csv':"USD to Indian Rupee", "usdgbp.csv":"USD to Great Britan Pound",'USDCAN.csv':"USD to Canadian Dollar", "usdeuro.csv" : "USD to Euro","usd_to_aud.csv":"USD to Australian Dollar", "usdtocny.csv":"USD to Chinese Yen"}

# Taking inputs.
def currency_select():
	file_dict = {"USD to INR":'usdtoinr.csv', "USD to GBP":"usdgbp.csv","USD to EUR":'USDCAN.csv', "USD to CAN":"usdeuro.csv","USD to AUD":"usd_to_aud.csv","USD to CNY":"usdtocny.csv"}
	
	title = "Curreny Selection"
	msg = "Please select any currency from above:"
	choice = ["USD to INR","USD to GBP","USD to CAN","USD to EUR","USD to AUD","USD to CNY"]
	inputfile = eg.choicebox(msg,title,choice)
	inputfile = str(inputfile)		

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
	while True:
        	try:	
			title = "Select Range"
			msg2 = ("\nSelected option is " +(chosen_curr))
			msg1  = "Data Ranges from" + end_date+ " to " +  start_date	
			fieldNames = ["Please enter start(latest) date in format m/dd/yyyy (eg:3/11/2016)", "Please enter end(old) date in format m/dd/yyyy (eg:3/11/2010)"]
			fieldValues = []
			fieldValues = eg.multenterbox(msg1+msg2,title,fieldNames)
			temp=0
			start=0
			end=0
			if fieldValues == None:
				flag = 1
				fieldValues = [0,0]
				return (0,0,0,0,flag)
			else:
				flag = 0

			
			for i in myData:
				if myData[temp][0] == fieldValues[0]:
					start= temp
				elif myData[temp][0] == fieldValues[1]:
					end = temp
				else:
					pass
				temp+=1
			if start == 0 and end == 0: 
				raise ValueError
				
			elif start == 0: 
				raise ValueError
			elif end == 0:
				raise ValueError	
			else:
                                break

        	except  ValueError:
                	a = ("Error!! No Data Found, Please Try again with proper Date")
			eg.msgbox(a)
							
				
	start = int(start)
	end = int(end)
	return (start,end,fieldValues[0],fieldValues[1],flag)

			
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

	x = value.iloc[0,1]
	y = value.iloc[-1,1]
	z = ((x-y)/x * 100)
	a = ("The percentage change from %s  to  %s  is %.2f percent " %(value.iloc[0,0], value.iloc[-1,0],z))
	
	minprice = value.iloc[:, 1].values.min()
	index = value.iloc[:, 1].values.argmin()
	de = value.iloc[index]
	b = ("\nThe minimum Price was                   %s  on %s" %(minprice,de['Date']))

	maxprice = value.iloc[:, 2].values.max()
	index = value.iloc[:, 2].values.argmax()
	de = value.iloc[index]
	c = ("\nThe maximum opening Price was     %s  on %s" %(maxprice,de['Date']))
	
	maxprice = value.iloc[:, 3].values.max()
	index = value.iloc[:, 3].values.argmax()
	de = value.iloc[index]
	d = ("\nThe maximum High Price was          %s  on %s" %(maxprice,de['Date']))
	
	maxprice = value.iloc[:, 4].values.max()
	index = value.iloc[:, 4].values.argmax()
	de = value.iloc[index]
	e = ("\nThe maximum Low Price was           %s  on %s" %(maxprice,de['Date']))
	

	eg.msgbox(a+b+c+d+e)

	ts = plot_data['Price']
	ts1 = ts[in1:in2]	
	plt.plot(ts1)
	plt.xlabel('Time Elapsed')
	plt.ylabel(chosen_curr)
	plt.title('Time Series graph ')
	mng = plt.get_current_fig_manager()
	mng.resize(*mng.window.maxsize())
	eg.msgbox("Graph has been plotted, please access it in a browser using URL: 'http://127.0.0.1:5000/'")
	plt.savefig("static/op1.png")	

# Taking inputs.
def annual_select(op):
	file_dict = {"1":'usdtoinr.csv', "2":"usdgbp.csv","3":'USDCAN.csv', "4":"usdeuro.csv","5":"usd_to_aud.csv","6":"usdtocny.csv"}

        while True:
        	try:	
			title = "Year Selection"
			msg1 = ("\nEnter Year")			
			msg2 = (("Selected option is %r") %(op))
                        fieldNames = ["Enter year between (2002-2016):"]
			fieldValues = []
			fieldValues = eg.multenterbox(msg2,title,fieldNames)
			if fieldValues == None:
				int_year = fieldValues
	                else:
				int_year = int(fieldValues[0])
                        if int_year == None:
				break
			elif int_year > 2001 and int_year < 2017:
                                break
                        else:
                                raise ValueError

        	except  ValueError:
                	a = ("Error!! No Data Found, Please Try again with proper Year")
			eg.msgbox(a)
	if fieldValues == None:
		input_year = fieldValues
	else:
		input_year = fieldValues[0]
	if input_year == None:
		flag =1
		return (0,0,0,0,0,0,0,flag)

	else:
		flag =0
		dateparse = lambda dates: pd.datetime.strptime(dates, '%m/%d/%Y')	

		plot_data_usdinr = pd.read_csv(file_dict["1"],index_col='Date',date_parser=dateparse)
		plot_data_usdgbp = pd.read_csv(file_dict["2"],index_col='Date',date_parser=dateparse)
		plot_data_usdcan = pd.read_csv(file_dict["3"],index_col='Date',date_parser=dateparse)
		plot_data_usdeur = pd.read_csv(file_dict["4"],index_col='Date',date_parser=dateparse)
		plot_data_usdaud = pd.read_csv(file_dict["5"],index_col='Date',date_parser=dateparse)
		plot_data_usdcny = pd.read_csv(file_dict["6"],index_col='Date',date_parser=dateparse)
		return (plot_data_usdinr,plot_data_usdgbp,plot_data_usdcan,plot_data_usdeur,plot_data_usdaud,plot_data_usdcny,input_year,flag)

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
	mng = plt.get_current_fig_manager()
	mng.resize(*mng.window.maxsize())
	plt.xlabel('Time Elapsed')
	plt.savefig("static/op3.png")
	eg.msgbox("Graph has been plotted, please access it in a browser using URL: 'http://127.0.0.1:5000/'")
	

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
	mng = plt.get_current_fig_manager()
	mng.resize(*mng.window.maxsize())
	plt.xlabel('Currencies')
	plt.ylabel("Percentage change")
	title = 'Time Series graph for '+input_year 
	plt.title(title)
	#plt.title('Time Series graph')
	plt.savefig("static/op2.png")
	eg.msgbox("Graph has been plotted, please access it in a browser using URL: 'http://127.0.0.1:5000/'")
	
def web_plot():
    APP = flask.Flask(__name__)
    @APP.route('/')
    def index():
        """ Displays the index page accessible at '/'
        """
        return flask.render_template('index.html')
    APP.debug=True
    APP.run()
    url='http://127.0.0.1:5000/'
    webbrowser.open_new(url)


while True:

	op1 = "Consolidated analysis on annual basis" 
	op3 = "Change Percentage for selected year"
	
	msg = "What do you want to see"
	title = "Choose option"
	choice = ["Consolidated analysis  of all the currencies on annual basis", "Analysis of a particular currency in a specified time range", "Change in value of currency(percentage) for selected year","Exit"]
	user_in = eg.choicebox(msg,title,choice)
	user_in = str (user_in)
	
	if user_in == "Analysis of a particular currency in a specified time range": 
		file1,myData,plot_data,chosen_curr,end_date,start_date = currency_select()
		start1,end1,in1,in2,flag = date_select(myData,chosen_curr,end_date,start_date)
		print flag
		if flag == 1:
			pass
		else:
			output(start1,end1,file1,plot_data,in1,in2,chosen_curr)
	elif user_in == "Change in value of currency(percentage) for selected year":
		plot_data_usdinr,plot_data_usdgbp,plot_data_usdcan,plot_data_usdeur,plot_data_usdaud,plot_data_usdcny,input_year,flag = annual_select(op3)
		if flag == 1:
			pass
		else:
			plot_func_chng(plot_data_usdinr,plot_data_usdgbp,plot_data_usdcan,plot_data_usdeur,plot_data_usdaud,plot_data_usdcny,input_year)
	elif user_in == "Consolidated analysis  of all the currencies on annual basis":
		plot_data_usdinr,plot_data_usdgbp,plot_data_usdcan,plot_data_usdeur,plot_data_usdaud,plot_data_usdcny,input_year,flag = annual_select(op1)
		if flag == 1:
			pass
		else:
			plot_func(plot_data_usdinr,plot_data_usdgbp,plot_data_usdcan,plot_data_usdeur,plot_data_usdaud,plot_data_usdcny,input_year)
	
	elif user_in == "Exit":
		exit(0)
	else:
		exit(0)

