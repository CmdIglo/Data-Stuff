# A program for visualizing the unemployment rate in Detroit from 1990 to 2020
# X axis labelled with "Unemployment rate" and Y axis labelled with "Date"
# You can find the data in this repo as "export.csv"
# Markers at lowest and highest unemployment rate showing the rate and the date in format "YYYY-MM"
# This program was originally written for a presentation for school about Detroit's economy and cityscape

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

def main():
	lisLab = []
	lisArb = []
	df = pd.read_csv("export.csv")

	for i in range(len(df["label"])):
		lisLab.append(df["label"][i])
		lisArb.append(df["Arbeitslosenrate"][i])                                                                                                      #Arbeitslosenrate = unemployment rate
	
	lisArb.reverse()
	lisLab.reverse()
	
	maxval = max(lisArb)
	minval = min(lisArb)
	ymax = 0                                                                                                                                          #can be left out
	ymin = 0                                                                                                                                          #can be left out	
	for j in range(len(lisArb)):
		if lisArb[j] == maxval:
			ymax = j
			maxLab = lisLab[j]
		if lisArb[j] == minval:
			ymin = j
			minLab = lisLab[j]
	
	arrow_properties = dict(
    facecolor="black", width=0.5,
    headwidth=4, shrink=0.1)
	
	lisArb = np.array(lisArb)
	lisLab = np.array(lisLab)
	
	plt.title("Unemployment rate in Detroit over the years")

	plt.xlabel("Date")                                                                                                                               #datum = date
	plt.ylabel("Unemployment rate")
	
	plt.annotate("Highest unemployment rate ({}%): \n {}".format(maxval,maxLab), (ymax, maxval), (ymax-175, maxval-5), arrowprops=arrow_properties)
	plt.annotate("Lowest unemployment rate ({}%): \n {}".format(minval,minLab), (ymin, minval), (ymin-100, minval+15), arrowprops=arrow_properties)
	
	plt.plot(lisLab, lisArb, color="blue")
	
	frame = plt.gca()
	frame.axes.get_xaxis().set_ticks([])
	frame.axes.get_yaxis().set_ticks([])
	
	plt.show()

if __name__ == "__main__":
		main()
