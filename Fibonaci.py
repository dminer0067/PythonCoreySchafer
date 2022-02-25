a,b = 0,1
#fibonacci series
for x in range(1,10):
    print (a)
    a,b = b,a+b
    
def fibo(num):
    a,b = 0,1
    for x in range(1,num):
        yield "{}".format(a)
        a,b = b,a+b
for item in fibo(20):
    print(item)