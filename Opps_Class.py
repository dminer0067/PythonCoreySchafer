class Employee:
    def __init__(self,first,last,pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first+"."+last + "@email.com"
        
    def fullname(self):
        return "{} {}".format(self.first,self.last)
        

emp1 = Employee("test1","user1",120000)
emp2 = Employee("test2","user2",150000)

# print(emp1)
# print(emp2)

# emp1.first = "Nirmal"
# emp1.last = "Patel"
# emp1.email = "Nirmal.patel@mail.com"
# emp1.pay = 80000

# emp2.first = "Test"
# emp2.last = "User"
# emp2.email = "Test.User@mail.com"
# emp2.pay = 150000

# print(emp1.fullname())
# print(emp2.fullname())

print(Employee.fullname(emp1))

print(Employee.fullname(emp2))

# print(emp1.email)
# print(emp2.email)