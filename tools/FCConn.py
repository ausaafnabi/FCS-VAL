# Importing file required for Serial Connection with the Computer
import serial

import matplotlib.pyplot as plt
import numpy as np

plt.ion()
fig=plt.figure()

i=0 
x=list()
y=list()
i=0
conn = serial.Serial('/dev/ttyACM0',9600)
conn.close()
conn.open()
count=1
while True:
	data = conn.readline()
	print(data.decode())
	dataArray = data.decode().split('\t')
	count += 1
	if(count >8):
		x.append(i)
		y.append(data.decode())
		plt.scatter(i,float(dataArray[1]))
		i +=1
		plt.show()
		plt.pause(0.0001)
		if (count>100):
			break


