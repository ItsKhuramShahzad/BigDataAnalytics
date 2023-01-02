#!/usr/bin/python3
import sys
value_flights=0
value_cancel=0

for line in sys.stdin:
	data = line.strip().split(",");
	key_airport= data[4]
	if data[5].strip().isdigit() and data[15].strip().isdigit():
		value_flights=  int (data[5].strip())
		value_cancel=  int (data[15].strip())	
	else: 
		value_flights=0
		value_cancel=0
	print("{0}\t{1}\t{2}".format(key_airport,value_flights, value_cancel))
	
