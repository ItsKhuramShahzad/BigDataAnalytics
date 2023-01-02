#!/usr/bin/python3
import sys
Dict = {}
for line in sys.stdin:
	data = line.strip().split("\t")
	thiskey= data[0]
	cancellation = data[1]
	if thiskey in Dict.keys():
		val= Dict[thiskey]
		val+= float (cancellation)
		Dict.update({thiskey: val})
	else:
		val_1= float (cancellation)
		Dict[thiskey]= val_1
airline=  ""
airline_cancellation =0;
sorted_dict =sorted(Dict.items(), key=lambda x: x[1], reverse=True)
flag =0
for x in sorted_dict:
	if x!= "arr_cancelled":
		airline= x[0]
		airline_cancellation= x[1]
		flag+=1
		print("\nThe Airport: {0}  with most Cancelled Flights in 2016 are: {1} "
		.format(airline, airline_cancellation ))
		if flag==1:
			break
			