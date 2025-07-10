Employee Management System
from abc import ABC, abstractmethod

# Abstract base class
class Employee(ABC):
    company_name = "TechCorp"  # Class variable
    def __init__(self, name, salary):
        self._name = name         # Protected variable
        self.__salary = salary    # Private variable
