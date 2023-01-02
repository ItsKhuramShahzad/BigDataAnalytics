#!/usr/bin/python3
import sys
import csv
for line in sys.stdin:
	data = line.strip().split(",");
	key_year= data[0]
	if data[5].strip().isdigit():
		value_flights= float (data[8].strip())
	else: 
		value_flights=0
	print("{0}\t{1}".format(key_year,value_flights))
	
