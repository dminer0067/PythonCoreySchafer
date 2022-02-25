x = 'Global X'

def test():
    y = 'Local Y'
    x = 'Local x'
    print(x)
    
test()
print(x)
#print(y) #y's scope is inside test()
