from abc import ABCMeta, abstractmethod


class IDepartment(metaclass=ABCMeta):
    @abstractmethod
    def __init__(self):
        """ Implement in child class """

    @abstractmethod
    def print_department(self):
        """ Implement in child class """


class Engineering(IDepartment):
    def __init__(self, employees):
        self.employees = employees

    def print_department(self):
        print(f"Engineering Department: {self.employees}")


class Science(IDepartment):
    def __init__(self, employees):
        self.employees = employees

    def print_department(self):
        print(f"Science Department: {self.employees}")


class Parent_Department(IDepartment):
    def __init__(self, employees):
        self.employees = employees
        self.base_employees = employees
        self.sub_department = []

    def add(self, dept):
        self.sub_department.append(dept)
        self.employees += dept.employees

    def print_department(self):
        print("Parent Department")
        print(f"Parent Department Base Employees: {self.base_employees}")
        for dept in self.sub_department:
            dept. print_department()
        print(f"Total number of employees: {self.employees}")

dept1 = Engineering(200)
dept2 = Science(150)

parent_dept = Parent_Department(20)
parent_dept.add(dept1)
parent_dept.add(dept2)

parent_dept.print_department()
