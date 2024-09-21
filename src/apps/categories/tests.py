# class Person:
#     def __init__(self, name, last_name, age, passport):
#         self.name = name
#         self.last_name = last_name
#         self.age = age
#         self.passport = passport
#
#     def get_info(self):
#         info = f"{self.name} {self.last_name} {self.age}"
#         info += f"{self.passport}"
#         return info
#
#     def get_age(self, year):
#         return year - self.age
#
#
# class Student(Person):
#     def __init__(self, name, last_name, age, passport, id_number):
#         super().__init__(name, last_name, age, passport)
#         self.id_number = id_number
#         self.degree = 1
#
#     def get_id(self):
#         return self.id_number
#
#     def get_degree(self):
#         return self.degree
#
# student1 = Student("Genry", "Morgan", 2000, "ff5654151",
#                    "12578584")
#
# print(student1.get_id())
# print(student1.get_age(2024))

class Employee:
    def __init__(self, name, salary):
        self.name = name          # Public
        self._department = "Sales"  # Protected
        self.__salary = salary    # Private

    def get_salary(self):
        return self.__salary

emp = Employee("John", 50000)
print(emp.name)          # Accessible
print(emp._department)   # Accessible but discouraged
print(emp.get_salary())  # Accessible
# print(emp.__salary)    # Raises AttributeError
