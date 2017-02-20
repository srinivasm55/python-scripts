### threat feeds####



import urllib2

response = urllib2.urlopen('http://malc0de.com/bl/IP_Blacklist.txt')

webdata = response.read()

print webdata

f = "malcode.txt"

with open(f,"w") as data:
    data.write(webdata)
