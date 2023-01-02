#!/usr/bin/python3
import sys
for line in sys.stdin:
	data = line.strip().split(",");
	key_airport= data[4]
	if data[21].strip().isdigit():
		security_delay=  int (data[21].strip())	
	else: 
		security_delay=0
	print("{0}\t{1}".format(key_airport,security_delay))
	
	
