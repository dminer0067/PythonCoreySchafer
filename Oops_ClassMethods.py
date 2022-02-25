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
        
    @classmethod        
    def Raise_amount(cls,amount):
        cls.raise_amount = amount
    
    @classmethod
    def from_string(cls,emp_str):
        first,last,pay = emp_str1.split("-")
        return cls(first,last,pay)
        
emp1 = Employee("Nirmal","Patel",15000)
emp2 = Employee("Test1","User1",12000)

emp_str1 = "John-Doe-75000"
emp_str2 = "Steve-Smith-68000"
emp_str3 = "Mark-jo-72000"

newemp1 = Employee.from_string(emp_str1)

print(newemp1.first,newemp1.email)




# Employee.Raise_amount(2.05)

# print(Employee.raise_amount)

# print(emp1.raise_amount)
# print(emp2.raise_amount)

# # print(emp1.pay)
# # emp1.apply_raise()
# # print(emp1.pay)

# # print(emp1.fullname())
# # print(emp2.fullname())