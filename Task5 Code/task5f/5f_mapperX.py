#!/usr/bin/python3
import sys
value_flights=0
value_cancel=0
for line in sys.stdin:
        data = line.strip().split(",");
        key_airline= data[2]
        if  data[17].strip().isdigit():
                arr_delay=  int (data[17].strip())
        else: 
                arr_delay=0
        print("{0}\t{1}".format(key_airline, arr_delay))
        



