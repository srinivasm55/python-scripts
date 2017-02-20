import json

filename = 'population_data.json'

with open(filename) as f:
	pop_data = json.load(f)

#print type(pop_data)
#print pop_data
print len(pop_data)	

for pop_dict in pop_data:
	if pop_dict['Year'] == '2010':
		country_name = pop_dict['Country Name']
		population = int(float(pop_dict['Value']))
		print(country_name+": "+str(population))
