import numpy as np 
import matplotlib.pyplot as plt

fileIn = open('./testset')
data_x = []
data_y = []
for line in fileIn.readlines():
	lineArr = line.strip()
	lineArr = lineArr.split()
	data_x.append([1.0,float(lineArr[0]),float(lineArr[1])])
	data_y.append(float(lineArr[2]))

fig = plt.figure()

ax = fig.add_axes([0.1,0.1,0.7,0.7])
ax.set_title("sample input")
for i in range(0,100):
        if (int(data_y[i])==1):
            ax.plot(data_x[i][1],data_x[i][2],'or')
        else:
            ax.plot(data_x[i][1],data_x[i][2],'ob')
plt.show()
