#!/usr/bin/python3
import sys
f = open("data.txt", "w")
for line in sys.stdin:
	data = line.strip().split(",");
	key_month= data[1]
	if data[5].strip().isdigit():
		value_flights= float (data[5].strip())
	else:
		value_flights=0
	print("{0}\t{1}".format(key_month,value_flights))
				

