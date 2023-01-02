#!/usr/bin/python3
import sys
import csv
total_year =0
total_flights =0
oldkey= None
f = open("data.txt", "w")
for line in sys.stdin:
	data = line.strip().split("\t")
	thiskey= data[0] 
	value_flights =  data[1]
	if thiskey!= oldkey and oldkey!= None:
		with open('data.txt', 'a') as file:
        		file.write(str(oldkey))
        		file.write("\t")
        		file.write(str(total_flights))
        		file.write("\n")
		oldkey= thiskey
		total_flights=0
	oldkey= thiskey
	total_flights+= float(value_flights)
totalflights=0
with open('data.txt', 'r') as file:
	csv_reader = csv.reader(file, delimiter='\t')
	for data in csv_reader:
		totalflights+= float (data[1])
with open('data.txt', 'r') as file:
	csv_reader = csv.reader(file, delimiter='\t')
	for data in csv_reader:	
		key_year= data[0]
		flightcount= float (data[1])
		percentage= int ((flightcount/totalflights)*100)
		print("Year No: {0}\t Total flight of year : {1}\t Total flight Percentage per Year:  {2} %"
		.format(key_year, flightcount, percentage))
	
	
