#this is a visualization of the "collatz problem".
#the "collatz problem" describes a series of calculations performed on 
#different numbers. even numbers will be divided by two and odd numbers 
#multiplied by three and added to one.
#it visualizes the length of adjacent calculations from a given number (x) to
#the final pattern of 4, 2, 1, 4, 2, 1 ..

from math import *
import matplotlib.pyplot as plt 
import numpy as np
import time

def main():
	start = time.time()
	countlis = []
	x = 100001

	for n in range(1,x):
		count = 0
		#print(n)
		while n > 1:
			if n % 2 == 0:
				n = n/2
				count+=1
			else:
				n = (n*3)+1
				count+=1
			
			#print(n)
		
		countlis.append(count)

	stop = time.time()

	countlis = np.array(countlis)
	cl = [y for y in range(len(countlis+1))]
	plt.scatter(cl, countlis, marker="o", color="r", s=2) #x, y, marker, color, size
	plt.show()
	print(float((stop-start)/60))

if __name__ == "__main__":
	main()
