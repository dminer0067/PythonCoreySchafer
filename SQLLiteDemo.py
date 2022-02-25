import sqlite3
from ClassEmployee import Employee

conn = sqlite3.connect("employee.db")

c = conn.cursor()

# c.execute("""CREATE TABLE EMPLOYEE(
    
#     first text,
#     last text,
#     pay integer
    
#     ) """)

emp1 = Employee('Karen','kesto',98000)
emp2 = Employee('Mary','kesto',72000)

# print(emp1.first)
# print(emp1.last)
# print(emp1.pay)

#c.execute("Insert into Employee Values(?,?,?)",(emp1.first,emp1.last,emp1.pay))


# c.execute("Insert into Employee Values(?,?,?)",(emp1.first,emp1.last,emp1.pay))
# conn.commit()

# c.execute("Insert into Employee Values(:first,:last,:pay)",{'first':emp2.first,'last':emp2.last,'pay':emp2.pay})
# conn.commit()
def insert_emp(emp):
    with conn:
        c.execute("Insert into Employee Values(:first,:last,:pay)",{'first':emp.first,'last':emp.last,'pay':emp.pay})
    


def get_emps_by_name(lastname):
    c.execute("Select * from Employee where last=:last",{'last':lastname})
    return c.fetchall()

def update_pay(emp, pay):
    with conn:
        c.execute("""UPDATE employees SET pay = :pay
                    WHERE first = :first AND last = :last""",
                  {'first': emp.first, 'last': emp.last, 'pay': pay})


def remove_emp(emp):
    with conn:
        c.execute("DELETE from employees WHERE first = :first AND last = :last",
                  {'first': emp.first, 'last': emp.last})

#c.execute("Select * from Employee where last=?",('Smith',))
#c.execute("Select * from Employee")
#print(c.fetchall())

#conn.commit()

# insert_emp(emp1)
# insert_emp(emp2)

# emps = get_emps_by_name("kesto")
# remove_emp(emp1)
# print(emps)

c.execute("Select * from Employee")
print(c.fetchall())

conn.close()