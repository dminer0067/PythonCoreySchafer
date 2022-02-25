#string in Python.

msg = "Hello world"

print(msg)


#escape character
msg2 = 'Bobby\'s World' 
msg3 = "Bobby's World"

print(len(msg2) + len(msg3))
print(len(msg2[0:4]))

print(msg[6:])

print("Lower case : ",msg.lower())
print("Upper case : ",msg.upper())

print("Count L : ",msg.count("l"))

print("Starting from : ",msg.find("world"))

replacemsg = msg.replace("world","Universe")
print("Replacing string : ",replacemsg)

greeting = "Good morning"
name = "Mike"

print(greeting + " "+name + "..." +"!")

formarstr1 = 'Hi {}, {}, welcome...!'.format(greeting,name)
print(formarstr1)

#new way to format the string called f sting

formarstr2 = f'Hi {greeting} {name}'
print(formarstr2)

#all supported method 
print(dir(name))
#Help for any specific function
print(help(str))


print(help(str.lower()))
