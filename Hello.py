print("Hello")

# for x in range(1,10):
#     print(x)
    
sqr = (x*x*x for x in range(1,11))
sqlist = []

for n in sqr:
    sqlist.append(n)
    
print(sqlist)


