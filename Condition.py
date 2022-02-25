lang = 'Java'
if(lang == 'Python'):
    print("Language is : ",lang)
elif(lang == 'Java'):
    print("Language is : ",lang)
else:
    print("Not Matching....!!")


user = 'test'
status = True

# or operator
if user == 'test' or status:
    print('Logged in')
else:
    print('Bad Request')

# and operator    
if user == 'test' and status:
    print('Logged in')
else:
    print('Bad Request')

if not status:
    print('Please login first')
else:
    print('Welcome...!!')



a = [1,2,3]
b = [1,2,3]
c = a

print(a==b)
print(id(a))
print(id(b))
print(a,b,c)
print("A and B : ",a is b)

print("A and C : ",a is c)