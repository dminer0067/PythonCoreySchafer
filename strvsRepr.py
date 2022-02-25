
import string


a = [1,2,3,4]
b = "python string"


# print str("a")
# print repr(a)

newstr = [] 

for f in b:
    newstr.append(f)
    
    if newstr[1:5] == "h":
        break

print(newstr)

    
