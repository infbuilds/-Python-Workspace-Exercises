# Project: OOP Inheritance Practice | Part 2
# Description: Managing employee hierarchies using Developer and Executive subclasses.
class Employee:
    raise_rate = 1.1

    def __init__(self, first_name, last_name, salary):
        self.first_name = first_name
        self.last_name = last_name
        self.salary = salary
        self.email = f"{first_name.lower()}.{last_name.lower()}@email.com"

    def get_details(self):
        return "Name: {} {} Salary: {} Email: {}".format(self.first_name, self.last_name, self.salary, self.email)


# Employee Instances
emp1 = Employee("jesse", "kentry", 9000)
emp2 = Employee("Ayse", "Demir", 6000)
emp3 = Employee("Fatma", "Kara", 7000)


class Developer(Employee):
    def __init__(self, first_name, last_name, salary=15000, language="Python"):
        super().__init__(first_name, last_name, salary)
        self.language = language

    raise_rate = 1.2

    def get_details(self):
        return "Name: {} {} Salary: {} Email: {} Language: {}".format(self.first_name, self.last_name, self.salary, self.email, self.language)

    def get_language(self):
        return f"Programming Language: {self.language}"


# Developer Instances
dev1 = Developer("walter", "White", 11000000000, "Python, C++, CSS, HTML")
dev2 = Developer("John", "Kaya", 7000, "Java")

class executive(Employee):
    def __init__(self, first_name, last_name, salary,employees = None):
        super().__init__(first_name, last_name, salary)
        if employees == None:
            self.employees = []
        else:
            self.employees = employees
    def add_employee(self,employee):
        if employee not in self.employees:
            self.employees.append(employee)
    def remove_employee(self,employee):
        if employee in self.employees:
            self.employees.remove(employee)
    def show_employee(self):
        for employee in self.employees:
            print(employee.get_details())
excutive1 = executive("soul ", "goodman", 20000,)
excutive1.add_employee(emp1)
excutive1.add_employee(dev1)
excutive1.show_employee()
print("-" * 30)
excutive1.remove_employee(emp1)
excutive1.show_employee()
excutive2=executive("Gustavo","Fring",40000,[dev2,emp2,emp3])
excutive2.show_employee()


# Output Section
#print("-" * 30)
#print("Employee Information:")
#print(emp1.get_details())
#print(emp2.get_details())
#print(emp3.get_details())

#print("-" * 30)
#print("Developer Information:")
#print(dev1.get_details())
#print(dev1.get_language())
#print("-" * 30)
#print(dev2.get_details())
#print(dev2.get_language())
print(issubclass(executive,Employee))

