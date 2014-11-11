import numpy as np
import matplotlib.pyplot as plt

fileIn = open('./testset')
for line in fileIn.readlines():
	lineArr = line.strip().split()
	data_x.append([1.0,float(lineArr[0]),float(lineArr[1])])
	data_y.append(int(lineArr[2]))

fig = plt.figure()
ax = fig.add_axes([0.1,0.1,0.8,0.8])
ax.set_title('asdf');
for i in range(0,100):	

