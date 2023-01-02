#!/usr/bin/python3
import sys
import collections
Dict = {}
for line in sys.stdin:
        data = line.strip().split("\t")
        thiskey= data[0]
        arr_delay = data[1]
        val=0
        if thiskey in Dict.keys():
                val= Dict[thiskey]
                val+= int (arr_delay)
                Dict.update({thiskey: val})
        else:
                val+= int (arr_delay)
                Dict[thiskey]= val
airline=  ""
airline_delay =0;
sorted_dict =sorted(Dict.items(), key=lambda x: x[1], reverse=True)
flag =0
for x in sorted_dict:
        if x!= "airport":
                airline= x[0]
                airline_delay= x[1]
                flag+=1
                print(" ({0}) The Airline: {1}  Total Amount of Delay Minutes Grouped are: {2} "
                .format(flag, airline, airline_delay ))
                if flag==10:
                        break
