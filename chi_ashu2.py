import csv
import numpy as np
import pandas as pd

print "1, USD to INR \n",
print "2, USD to GBP \n",
print "3, USD to CAN \n",
print "4, USD to EUR\n",
print "5, USD to AUD \n",
inputfile = raw_input("please enter the currency from above")
file_dict = {"1":'usdtoinr.csv', "2":"usdgbp.csv","3":'USDCAN.csv', "4":"usdeuro.csv","5":"usd_to_aud.csv"}
for keys in file_dict.keys():
	if inputfile == keys:
		#file = pd.read_csv(, index_col = 0)
		a = list ( csv.reader ( open (file_dict[keys])))
	else:
		pass





file = pd.read_csv('usdtoinr.csv', index_col = 0)
a = list ( csv.reader ( open ("usdtoinr.csv")))

b=[]
in1 = raw_input("please enter start date in format m/dd/yyyy (eg:3/11/2016) \t")
in2 = raw_input("please enter end date in format m/dd/yyyy (eg:3/11/2016) \t")

c=0
c=int(c)
for i in a:
        if a[c][0] == in1:
                d= c
        elif a[c][0] == in2:
                d2 = c
        else:
                pass
        c+=1

d2 = int(d2)
d = int(d)
#ashu's method using pandas can also be used, here its been changed to because later in code we are appending desired value to an empty list
'''
if d2>d:
        aa = np.array(file.iloc[d:d2, :])
else:
        aa = np.array(file.iloc[d2:d, :])

'''
# mine can also be used
if d2>d:
        aa = np.array(a[d:d2]) #can be used without changing to array
else:
        aa = np.array(a[d2:d]) #can be used without changing to array

# this is common
#print "values in between the dates are \n", aa,
ii = 0
ii = int(ii)
r=[]
for i in aa:
        r.append( float(aa[ii][2]))
        ii+=1
print "\n"
#print "values of opening rate are \n", r # just for our info
#print "\n"
print "highest opening value is : " , max(r)
