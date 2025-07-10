Employee Management System
from abc import ABC, abstractmethod

# Abstract base class
class Employee(ABC):
    company_name = "TechCorp"  # Class variable
    def __init__(self, name, salary):
        self._name = name         # Protected variable
        self.__salary = salary    # Private variable
    @abstractmethod
    def work(self):
        pass
def get_salary(self):
        return self.__salary

    def set_salary(self, amount):
        if amount > 0:
            self.__salary = amount
 @property
    def name(self):
        return self._name

    @name.setter
    def name(self, new_name):
        if new_name:
            self._name = new_name
# Developer subclass
class Developer(Employee):
    def __init__(self, name, salary, language):
        super().__init__(name, salary)
        self.language = language

    def work(self):
        print(f"{self.name} writes code in {self.language}.")

    def debug(self):
        print(f"{self.name} is debugging code.")
# Manager subclass
class Manager(Employee):
    def __init__(self, name, salary, team=None):
        super().__init__(name, salary)
        self.team = team if team else []

    def work(self):
        print(f"{self.name} manages the team.")

    def add_team_member(self, member):
        self.team.append(member)
# Polymorphism function
def employee_activity(emp: Employee):
    emp.work()


# Main program
if __name__ == "__main__":
    dev = Developer("Alice", 80000, "Python")
    mgr = Manager("Bob", 100000)

    mgr.add_team_member(dev)
