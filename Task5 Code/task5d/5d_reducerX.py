#!/usr/bin/python3
import sys
Dict = {}
for line in sys.stdin:
	data = line.strip().split("\t")
	thiskey= data[0]
	flights = data[1]
	if thiskey in Dict.keys():
		val= int(Dict[thiskey])
		val+= int (flights)
		Dict.update({thiskey: int (val)})
	else:
		Dict[thiskey]= int (flights)
busiest_airport=  ""
busiest_airport_flights =0;
flag= True
for x in Dict:
	if flag:
		busiest_airport= x
		busiest_airport_flights= Dict[x]
		flag= False
	elif int (Dict[x]) > busiest_airport_flights:
		busiest_airport=x
		busiest_airport_flights= Dict[x]
print("\n The Airport: {0}  has been the most busiest over the 10 year period , flights: {1}"
.format(busiest_airport, busiest_airport_flights))
