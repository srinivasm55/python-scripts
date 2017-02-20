class Car():
   def __init__(self,name):
      self.name = name
      self.reading = 0
   def getinfo(self):
   	   #print(self.name)
   	   return self.name.title() + ' '+str(self.reading)


c = Car('tesla')
#s = c.getinfo()
c.reading = 100
print(c.getinfo())

