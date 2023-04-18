
class Employee():
    def __init__(self, fname, lname, doe, salary, department):
        self.fname = fname
        self.lname = lname
        self.doe = doe
        self.salary = salary
        self.department = department

    def emp_id(self):
        return f'{self.fname} {self.lname}\'s id is {self.eid}'

    def emp_name(self):
        return f'Employee\'s name is {self.fname} {self.lname}.'

    def date_of_employment(self):
        return f'{self.fname} {self.lname}\'s date of employment began on {self.doe}.'

    def emp_department(self):
        return f"{self.fname} {self.lname}'s department is {self.department}"

    def emp_salary(self):
        return f'{self.fname} {self.lname}\'s salary is {self.salary}.'

    def full_emp_info(self):
        return dict({'id':self.eid, 'First Name':self.fname, 'Last Name':self.lname, 'Date of Employment':self.doe, 'Salary':self.salary})

    def to_dict(self): # Creates dictionary of values to print to send to db
        return {
            'fname': self.fname,
            'lname': self.lname,
            'doe': self.doe,
            'salary': self.salary,
            'department': self.department
        }

#     def __call__(self, *args, **kwargs):
#         print('Call function', args, kwargs)

# @Employee(eid, fname, lname, doe, salary)
# def emp_info():
#     # emp_dict = dict({'id':self.eid, 'First Name':self.fname, 'Last Name':self.lname, 'Date of Employment':self.doe, 'Salary':self.salary})
#     print('Hello')

# emp1 = Employee('Johnny', 'Walker', '04-12-2023', 75000, 'Engineering')
# emp1.date_of_employment()
# emp2 = Employee(id, 'Yan', 'Ho', '04-12-2023', 75000)

# print(emp1.emp_id())
# print(emp2.emp_id())
# print(emp1.emp_name())
# print(emp2.date_of_employment())
# print(emp1.emp_salary())
