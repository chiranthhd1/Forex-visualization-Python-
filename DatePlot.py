import csv
import numpy as np
import datetime as dt
import matplotlib.pyplot as plt
import matplotlib.dates as mdates


year =0
priceUsd_Eur =[]
priceUsd_Eur =[]
priceUsd_gbp =[]
priceUsd_cny =[]
priceUsd_inr =[]
corrDates = []

def read_file(filename):
    a = list ( csv.reader ( open (filename)))
    d =[]
    #print a
    c = 1
    for i in a:
        if (c < len(a)) :
            try:
                j = a[c][0]
            except Exception :
                print "Error at "
                print a[c]

            x = j.split("/")
                #print x[2]
            #print i
            if x[2] == year:
                    #print "i am in if "
                d.append(a[c])
            c +=1
        #print i
    temp = getPrice(d)
    getDates(d)
    return temp

def getPrice(price):
    priceValue = []
    c = 0
    for i in price :
        priceValue.append(price[c][1])
        c += 1
    return priceValue

def getDates(dates):
    del corrDates [:]
    c = 0
    for i in dates :
        corrDates.append(dates[c][0])
        c += 1


year = raw_input("Enter the year for which you need to see the consolidated report wrt USD in range (1990-2016):  ")
priceUsd_Eur = read_file("usdeuro.csv")
print priceUsd_Eur
datesUsd_Eur = corrDates
print datesUsd_Eur

x = [dt.datetime.strptime(d,'%m/%d/%Y').date() for d in datesUsd_Eur]
y = range(len(x))
plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%m/%d/%Y'))
plt.gca().xaxis.set_major_locator(mdates.MonthLocator())
plt.plot(x,priceUsd_Eur, color= 'r')
plt.gcf().autofmt_xdate()
plt.show()
# priceUsd_inr = read_file("usdtoinr.csv")



