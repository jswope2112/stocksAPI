import requests
import json
import numpy as np
from datetime import date
import matplotlib.pyplot as plt
import sys

#Allow the stock called to be based upon an input and retrieve the data if that stock is valid
#Error if nothing is entered and exit the program
try:
	SMA200 = 'http://www.alphavantage.co/query?function=SMA&symbol=' + sys.argv[1] +'&interval=daily&time_period=200&series_type=open&apikey=9S5OS48JQM20W5U9'
	cost = 'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=' + sys.argv[1] + '&outputsize=full&interval=60min&apikey=9S5OS48JQM20W5U9'
	first_data = requests.get(SMA200)
	second_data = requests.get(cost)
except BaseException:
	print("Enter a valid stock")
	exit()

print(sys.argv[1])
print (first_data)
data = first_data.json()
days = []
SMA = []

#Get all of the SMA values from the data pulled and throw an exception and exit the program if an invalid stock was entered
try:
	for k, v in data["Technical Analysis: SMA"].items():
		year = int(k[:4])
		month = int(k[5:7])
		day = int(k[8:10])
		SMA.append(v["SMA"])
		days.append(date(year,month,day))
	print(SMA[0])
	print(type(days[0]))
except BaseException:
	print("Enter a valid stock")
	exit()
print (second_data)
#get data for the price averages at opening
data1 = second_data.json()
prices = []
days1 = []
for d, p in data1['Time Series (Daily)'].items():
	prices.append(p['1. open'])
	year = int(d[:4])
	month = int(d[5:7])
	day = int(d[8:10])
	days1.append(date(year,month,day))

#Plot the prices vs the SMA(200)
f = plt.figure()
plt.plot(days1, prices, 'r', label = 'Prices')
plt.plot(days, SMA, 'k', label = 'SMA(200)')
plt.ylabel("Price")
plt.xlabel("Date")
plt.title("SMA(200) vs Price of " + sys.argv[1])
plt.legend(loc = 2)
f.savefig("stocks_graph")
