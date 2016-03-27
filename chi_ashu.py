import csv
import numpy as np

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
if d2>d:
	aa = np.array(a[d:d2]) #can be used without changing to array
else:
	aa = np.array(a[d2:d]) #can be used without changing to array

print "values in between the dates are \n", aa,
ii = 0
ii = int(ii)
r=[]
for i in aa:
	r.append( aa[ii][2])
	ii+=1
print "\n" 
print "values of opening rate are \n", r # just for our info
print "\n" 
print "highest opening value is : " , max(r)
