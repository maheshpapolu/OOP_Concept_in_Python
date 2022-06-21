# crate a class named as animal
class Animal:
    def __init__(self, name, age):
        """
        create a constructor to assign  values for name and age
        :param name:
        :param age:
        """
        self.name = name
        self.age = age

    def myfunc(self):
        """
        create a function that belong to the object
        :return:
        """
        print("animal name is " + self.name, "and age is ", self.age)


animal = Animal("jimmy", 5)  # create object to the class Animal and assign to variable called animal
animal.age = 6      # we can also modify object properties
animal.myfunc()     # to call the function to greate the animal
