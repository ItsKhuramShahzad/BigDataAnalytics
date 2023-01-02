#!/usr/bin/python3
import sys
Dict = {}
for line in sys.stdin:
	data = line.strip().split("\t")
	thiskey= data[0]
	flights = data[1]
	delay = data[2]
	if thiskey in Dict.keys():
		val= Dict[thiskey]
		val_1 = val['0'];
		val_2 = val['1'];
		val_1+= int (flights)
		val_2+= float (delay)
		new_entry = {"0": val_1, "1": val_2}
		Dict[thiskey].update(new_entry)
		#print("airport: {0}\t{1}\t {2}".format(thiskey, val_1, val_2))	
	else:
		val_1= int (flights)
		val_2= float (delay)
		new_entry = {"0": val_1, "1": val_2}
		Dict[thiskey]= new_entry
airport=  ""
airport_flights =0;
airport_delay=0
total_delay=0

flag= True

for x in Dict:
	val= Dict[x]
	total_delay+= val['1']		
for x in Dict:
	val= Dict[x]
	flights= val['0']
	delay= val['1']
	if flag:
		airport= x
		airport_flights= val['0']
		airport_delay= val['1']
		flag= False
	elif float (flights) > airport_flights:
		val= Dict[x]
		airport= x
		airport_flights= val['0']
		airport_delay= val['1']
print("\n The Airport: {0}  the most busiest of all other airports flights: {1}, the average delay time: {2}"
.format(airport, airport_flights, (airport_delay/total_delay)*100 ))

