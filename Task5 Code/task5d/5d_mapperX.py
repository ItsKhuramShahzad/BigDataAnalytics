#!/usr/bin/python3
import sys
import csv
for line in sys.stdin:
	data = line.strip().split(",");
	key_airport= data[4]
	if data[5].strip().isdigit():
		value_flights=  int (data[5].strip())
	else: 
		value_flights=0
	value_percentage=0
	print("{0}\t{1}".format(key_airport,value_flights))
	
