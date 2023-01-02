#!/usr/bin/python3
import sys
import csv
for line in sys.stdin:
	data = line.strip().split(",");
	key_airline= data[2]
	if data[5].strip().isdigit():
		value_flights= float (data[5].strip())
	else: 
		value_flights=0
	print("{0}\t{1}".format(key_airline,value_flights))
	
