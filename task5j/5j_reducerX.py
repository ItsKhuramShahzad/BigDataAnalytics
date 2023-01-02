#!/usr/bin/python3
import sys
Dict = {}
for line in sys.stdin:
	data = line.strip().split("\t")
	thiskey= data[0]
	flights = data[1]
	bad_weather = data[2]
	if thiskey in Dict.keys():
		val= Dict[thiskey]
		val_1 = val['0'];
		val_2 = val['1'];
		val_1+= int (flights)
		val_2+= float (bad_weather)
		new_entry = {"0": val_1, "1": val_2}
		Dict[thiskey].update(new_entry)
	else:
		val_1= int (flights)
		val_2= float (bad_weather)
		new_entry = {"0": val_1, "1": val_2}
		Dict[thiskey]= new_entry
airport=  ""
airport_flights =0;
airport_bad_weather=0
flag= True
for x in Dict:
	val= Dict[x]
	flights= val['0']
	bad_weather= val['1']
	if flag:
		airport= x
		airport_flights= val['0']
		airport_bad_weather= val['1']
		flag= False
	elif flights> airport_flights:
		airport= x
		airport_flights= val['0']
		airport_bad_weather= val['1']
print("\n Most Busiest Airport: {0}   has Probability that a Flight will be delayed due to Bad Weather  is: {1} "
.format(airport, (airport_bad_weather/airport_flights)))



