import csv

with open('sitka_weather_2014.csv') as f:
	reader = csv.reader(f)
	print(type(reader))
	h_row = next(reader)
	for row in reader:
		date = row[0]
		high = row[1]
		low = row[3]
		print(date,high,low)

#print h_row

#print(type(h_row))

