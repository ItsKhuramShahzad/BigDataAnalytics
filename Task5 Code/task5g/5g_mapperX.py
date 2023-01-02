#!/usr/bin/python3
import sys
value_flights=0
value_cancel=0
for line in sys.stdin:
	data = line.strip().split(",");
	key_year= data[0]
	key_airport= data[2]
	if key_year == "2016":
		if  data[15].strip().isdigit():
			arr_cancelled=  float (data[15].strip())
		else: 
			arr_cancelled=0
		print("{0}\t{1}".format(key_airport,arr_cancelled))
	
