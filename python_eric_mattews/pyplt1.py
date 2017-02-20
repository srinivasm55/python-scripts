import matplotlib.pyplot as plt


input = [1,2,3,4,5,6,7,8,9,10]
squares = [1,4,9,16,25,36,49,64,81,100]

#plt.plot(input,squares,linewidth=5)
plt.scatter(input,squares,s=10,c='red')
#plt.arrow()
plt.title("Plotting Squares",fontsize = 30)
plt.xlabel("Value",fontsize=15)
plt.ylabel("Squares",fontsize=15)

plt.tick_params(axis='both',which='major',labelsize=10)

plt.show()