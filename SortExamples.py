from audioop import reverse
from re import X

from sqlalchemy import true


x = [1,3,8,21,18,15,26,5,11,14]


print("Original list : ",x)

slist = sorted(x)
print("Sorted : ",slist)

rlist = sorted(x,reverse=True)
print("Reverse : ",rlist)

tup = (1,3,8,21,18,15,26,5,11,14)
stup = sorted(tup)
print("Tuple sort : ",stup)

