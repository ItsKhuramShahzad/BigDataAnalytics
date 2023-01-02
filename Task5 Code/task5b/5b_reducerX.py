#!/usr/bin/python3
import sys
Dict = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0, 10: 0, 11: 0, 12: 0}
for line in sys.stdin:
	data = line.strip().split("\t")
	thiskey= data[0]
	flights = data[1]
	if thiskey.strip().isdigit():
		val= int(Dict[int (thiskey)])
		val+= float (flights)
		Dict.update({int (thiskey): int (val)})
busiest_month=  1
busiest_month_flights =Dict[1];
for x in Dict:
	if int (Dict[x]) > busiest_month_flights:
		busiest_month=x
		busiest_month_flights= Dict[x]
	
print("\nThe busiest Month is : {0}\tTotal flight of this month : {1}"
.format(busiest_month, busiest_month_flights))
