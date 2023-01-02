#!/usr/bin/python3
import sys
value_flights=0
value_bad_weather=0

for line in sys.stdin:
	data = line.strip().split(",");
	key_airport= data[4]
	if data[5].strip().isdigit() and data[19].strip().isdigit():
		value_flights=  int (data[5].strip())
		value_bad_weather=  int (data[19].strip())	
	else: 
		value_flights=0
		value_bad_weather=0
	print("{0}\t{1}\t{2}".format(key_airport,value_flights, value_bad_weather))
	
	
