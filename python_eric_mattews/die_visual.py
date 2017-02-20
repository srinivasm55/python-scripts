from dice import Die


d = Die()

results = []

for r in range(100):
	result = d.roll()
	results.append(result)

print(results)

frequencies = []

for i in range(1,d.sides+1):
	freq = results.count(i)
	frequencies.append(freq)

print frequencies	

for i,j in enumerate(frequencies):
	print ("{},{}".format(i+1,j))

#print f	


import pygal

hist = pygal.Bar()

hist.x_labels = ['1','2','3','4','5','6']

hist.add('D6',frequencies)

hist.render_to_file('a.svg')





