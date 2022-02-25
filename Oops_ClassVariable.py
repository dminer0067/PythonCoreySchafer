class Employee:
    
    raise_amount = 1.08
    
    def __init__(self,first,last,pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first+"."+last + "@email.com"
        
    def fullname(self):
        return "{} {}".format(self.first,self.last)
    
    def apply_raise(self):
        self.pay = int(self.pay * Employee.raise_amount)
    
emp1 = Employee("Nirmal","Patel",15000)
emp2 = Employee("Test1","User1",12000)

print(Employee.raise_amount)

print(emp1.raise_amount)
print(emp2.raise_amount)

# print(emp1.pay)
# emp1.apply_raise()
# print(emp1.pay)

# print(emp1.fullname())
# print(emp2.fullname())