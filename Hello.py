print("Hello")

# for x in range(1,10):
#     print(x)
    
sqr = (x*x*x for x in range(1,11))
sqlist = []

for n in sqr:
    sqlist.append(n)
    
print(sqlist)


def fun():
    a = input("Insert value of A : ")
    return a

x = fun()
print(x)

print("Making changes in Hello.py file.")

print("Do not Save this change")
print("Save this change")