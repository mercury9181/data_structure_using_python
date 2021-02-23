import unittest
from operator import itemgetter


def merge_ranges(meetings):

    # Merge meeting ranges
    a=sorted(meetings)
    merged_mettings =[a[0]]
    # print(merged_mettings)
    
    for c_start,c_end in a[1:]:
        last_start, last_end = merged_mettings[-1]
        
        if c_start <= last_end :
            merged_mettings[-1] = (last_start,max(last_end,c_end))
        else:
            merged_mettings.append((c_start,c_end))
        
    return merged_mettings


tup = [(8,3),(3,4),(3,9),(5,9),(1,4)]
a= merge_ranges(tup)
print(a)