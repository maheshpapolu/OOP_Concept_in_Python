# create a class named person and define function, assign values for name and age.
class Person:
    def __init__(self, name, age):
        """
        __init__ function is called "constructor" it's assign values to object properties
        :param name:
        :param age:
        """
        self.name = name
        self.age = age


person = Person("Mahesh", 22)
print(person.name)
print(person.age)

