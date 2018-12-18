class Employee():
    """雇员信息，包括名，姓和年薪"""
    def __init__(self,first,last,salary=0):
        self.first = first
        self.last = last
        self.salary = salary

    def give_raise(self,pay_rise=5000):
        self.salary += pay_rise
        employee = self.first + self.last + ' ' + str(self.salary)
        return employee
