#!/usr/bin/python3
import sys
Dict = {}
for line in sys.stdin:
	data = line.strip().split("\t")
	thiskey= data[0]
	flights = data[1]
	cancellation = data[2]
	if thiskey in Dict.keys():
		val= Dict[thiskey]
		val_1 = val['0'];
		val_2 = val['1'];
		val_1+= int (flights)
		val_2+= float (cancellation)
		new_entry = {"0": val_1, "1": val_2}
		Dict[thiskey].update(new_entry)
		#print("airport: {0}\t{1}\t {2}".format(thiskey, val_1, val_2))	
	else:
		val_1= int (flights)
		val_2= float (cancellation)
		new_entry = {"0": val_1, "1": val_2}
		Dict[thiskey]= new_entry
airport=  ""
airport_flights =0;
airport_cancellation=0
flag= True
for x in Dict:
	val= Dict[x]
	flights= val['0']
	cancellation= val['1']
	if flag:
		airport= x
		airport_flights= val['0']
		airport_cancellation= val['1']
		flag= False
	elif float (cancellation) > airport_cancellation:
		val= Dict[x]
		airport= x
		airport_flights= val['0']
		airport_cancellation= val['1']
print("\n The Airport: {0}  has the Largest Flights to Cancellation Ratio [ {1} : {2} ] = {3}"
.format(airport, airport_flights, airport_cancellation,airport_flights/airport_cancellation ))

