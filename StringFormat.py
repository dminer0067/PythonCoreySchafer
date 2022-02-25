import datetime

# person = {"name":"Jenny","age":19}

# sentence1 = "Hi There My Name is : {} and I am {} Years old...!".format(person["name"],person["age"])
# print(sentence1)

# sentence2 = "Hi There My Name is : {0} and I am {1} Years old...!".format(person["name"],person["age"])
# print(sentence2)

# sentence3 = "Hi There My Name is : {0[name]} and I am {1[age]} Years old...!".format(person,person)
# print(sentence3)

class person:
    def __init__(self,name,age):
        self.name = name
        self.age = age
        
p1 = person("Mike","26")
p2 = person("Kim","32")

sent1 = "My Name is : {0.name} and I am {0.age} Year's old...!".format(p1)
sent2 = "My Name is : {0.name} and I am {0.age} Year's old...!".format(p2)

print(sent1)
print(sent2)

# x = {"name" : "Mike","age" : "26"}

# x1 = "My Name is : {name} and I am {age} Year's old...!".format(**person)
# print(x1)

for i in range(1,111):
    sent = "The Value is : {:03}".format(i)
    print(sent)

pi = 3.146598483

pi_print = "The value of PI is : {:.3f}".format(pi)
print(pi_print)

mb = "1 MB is Equal to : {:,.2f} bytes".format(100**2)
print(mb)


mydate = datetime.datetime(2020,11,15,12,45,00)

print(mydate)

mydate1 = '{:%B %d, %Y}'.format(mydate)

print(mydate1)