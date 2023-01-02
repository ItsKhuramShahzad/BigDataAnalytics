#!/usr/bin/python3
import sys
Dict = {}
for line in sys.stdin:
	data = line.strip().split("\t")
	thiskey= data[0]
	security_delay = data[1]
	if thiskey in Dict.keys():
		val= Dict[thiskey]
		val+= float (security_delay)
		Dict.update({thiskey: val})
	else:
		val_1= float (security_delay)
		Dict[thiskey]= val_1		
airport=  ""
security_delay=0
flag= True
for x in Dict:
	val= Dict[x]
	if flag:
		airport= x
		security_delay= val
		flag= False
	elif float (val) > security_delay:
		val= Dict[x]
		airport= x
		security_delay= val		
print("\n The Airport: {0}  has the highest security delay is : {1} minuites"
.format(airport, security_delay))

