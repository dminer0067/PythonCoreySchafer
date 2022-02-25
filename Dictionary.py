student = {
    "id":1,
    "name":"Naman",
    "age":22,
    "courses":["Maths","Science"]
}

print(student)
print("Age is : ",student["age"])

print(type(student))

print(type(student["courses"]))

print(student.get('phone','NA'))

student["phone"] = "555-555-55555"
print(student)

student["age"] = 20
print(student)

#Update Value of key & Value in Dictionary
student.update({"name":"Kaman","age":18})

print(student)

#Delete key from Dictionary
del student["age"]
print(student)

for key,value in student.items():
    print(key,value)