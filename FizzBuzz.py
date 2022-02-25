
f = []
b = []
fb = []
num = []
for x in range(1,111):
    if x % 5 == 0 and x % 3 == 0:
        fb.append(x)
    elif x % 3 == 0:
        f.append(x)
    elif x % 5 == 0:
        b.append(x)
    else:
        num.append(x)
        
print("Fizz Buzz = ",fb)
print("Fizz = ",f)
print("Buzz = ",b)
print("Num = ",num)