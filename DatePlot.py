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
print len(datesUsd_Eur)
# priceUsd_cny = read_file("usdtocny.csv")
# print priceUsd_cny
# datesUsd_cny = corrDates
# print len(datesUsd_cny)
priceUSD_CAN = read_file("USDCAN.csv")
datesUSD_can = corrDates
print priceUSD_CAN
print len(datesUSD_can)
# priceUSD_INR = read_file("usdtoinr.csv")
# datesUSD_INR = corrDates
# print priceUSD_INR

eur_x = [dt.datetime.strptime(d,'%m/%d/%Y').date() for d in datesUsd_Eur]
#cny_x = [dt.datetime.strptime(d,'%m/%d/%Y').date() for d in datesUsd_cny]
can_x = [dt.datetime.strptime(d,'%m/%d/%Y').date() for d in datesUSD_can]
#inr_x = [dt.datetime.strptime(d,'%m/%d/%Y').date() for d in datesUSD_INR]

plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%m/%d/%Y'))
plt.gca().xaxis.set_major_locator(mdates.MonthLocator())

# #ax1 = plt.subplot(211)
# plt.plot(eur_x, priceUsd_Eur, color = 'r')
# #plt.setp(ax1.get_xticklabels(), fontsize=6)
# plt.gcf().autofmt_xdate()
# plt.show()
# #ax2 = plt.subplot(212, sharex=ax1)
# plt.plot(can_x, priceUSD_CAN, color = 'b')
# # # make these tick labels invisible
# # plt.setp(ax2.get_xticklabels())
# plt.gcf().autofmt_xdate()
# plt.show()


# ax3 = plt.subplot(313, sharex=ax1)
# plt.plot(cny_x, priceUsd_cny, color = 'y')
# # # make these tick labels invisible
# plt.setp(ax3.get_xticklabels())
# plt.gcf().autofmt_xdate()

# ax4 = plt.subplot(314, sharex=ax1)
# plt.plot(inr_x, priceUSD_INR, color = 'g')
# # # make these tick labels invisible
# plt.setp(ax4.get_xticklabels())
# plt.gcf().autofmt_xdate()


#plt.show()
# ax2 = plt.subplot(212, sharex=ax1)
# plt.plot(can_x, priceUSD_CAN)
# # make these tick labels invisible
# plt.setp(ax2.get_xticklabels(),)

#plt.plot(eur_x,priceUsd_Eur, color= 'r')
#plt.plot(can_x,priceUSD_CAN, color= 'b')
# plt.gcf().autofmt_xdate()
# plt.show()
# priceUsd_inr = read_file("usdtoinr.csv")



