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