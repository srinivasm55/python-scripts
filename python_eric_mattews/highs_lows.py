import csv
from matplotlib import pyplot as plt
from datetime import datetime

#filename = 'sitka_weather_07-2014.csv'
filename = 'sitka_weather_2014.csv'
with open(filename) as f:
	reader = csv.reader(f)
	header_row = next(reader)
	print(header_row)
	
	for index,colname in enumerate(header_row):
		#print(index,colname)				### op's as a tuple (a,b)
		print("{},{}".format(index,colname))    ### op's as a,b
	

	
	highs = []
	dates = []
	lows = []

	for row in reader:
		#highs.append(row[1]) ###list of type string
		try:
			cur_date = datetime.strptime(row[0],'%Y-%m-%d')
			high = int(row[1])
			low = int(row[3])
		except ValueError:
			print(cur_date,'missing date')
		else:
			dates.append(cur_date)		
			highs.append(high)    ### list of type integer
			lows.append(low)

#print(highs)	
#print(dates)
fig = plt.figure(dpi=128,figsize=(10,6))
plt.plot(dates,highs,c='red')
#plt.scatter(dates,highs,c='red')
plt.plot(dates,lows,c='blue')

plt.fill_between(dates,highs,lows,facecolor='blue',alpha=0.1)

fig.autofmt_xdate()

plt.show()












