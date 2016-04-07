import csv
import numpy as np
import datetime as dt


year =0
priceUsd_Eur =[]
priceUsd_Eur =[]
priceUsd_gbp =[]
priceUsd_cny =[]
priceUsd_inr =[]
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
    return temp

def getPrice(price):
    priceValue = []
    c = 0
    for i in price :
        priceValue.append(price[c][1])
        c += 1
    return priceValue

year = raw_input("Enter the year for which you need to see the consolidated report wrt USD in range (1990-2016):  ")
priceUsd_Eur = read_file("usdeuro.csv")
#print "Price_EUR:"
#print priceUsd_Eur
priceUsd_gbp = read_file("usdgbp.csv")
#print "Price_GBP:"
#print priceUsd_gbp
priceUsd_cny = read_file("usdtocny.csv")
#print "Price_CNY:"
#print priceUsd_cny
priceUsd_inr = read_file("usdtoinr.csv")
#print "Price_INR:"
#print priceUsd_inr



