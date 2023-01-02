#!/usr/bin/python3
import sys
Dict = {}
for line in sys.stdin:
	data = line.strip().split("\t")
	thiskey= data[0]
	flights = data[1]
	if thiskey in Dict.keys():
		val= float(Dict[thiskey])
		val+= float (flights)
		Dict.update({thiskey: float (val)})
	else:
		Dict[thiskey]= float (flights)
busiest_airline=  ""
airline_flights =0;
flag= True
for x in Dict:
	if flag:
		busiest_airline= x
		airline_flights= airline_flights= Dict[x]
		flag= False
	elif float (Dict[x]) > airline_flights:
		busiest_airline=x
		airline_flights= Dict[x]
print("\nAirline Carrier : {0}\t has flown most flights over the 10 year period are: {1}"
.format(busiest_airline, airline_flights))
