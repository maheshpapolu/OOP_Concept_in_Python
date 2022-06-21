# create a parent class or base class name as Person
class Person:
    def __init__(self, fullname, reg_no):
        """
        create a constructor to the class person
        :param fullname:
        :param reg_no:
        """
        self.fullname = fullname
        self.reg = reg_no

    def print_details(self):
        """
        crate a function
        :return:
        """
        print(self.fullname, self.reg)


class Student(Person):  # create a child class named as student , and put a parameter as parent class
    # if you don't want to add  any properties and methods to the class use pass keyword to execute the  block of code
    pass


class AnotherStudent(Person):  # another child class
    def __init__(self, fullname, reg_no):  # overrides the inheritance of the parent's using __init__ function
        Person.__init__(self, fullname, reg_no)


person = Person("mahesh", 101)  # create an object by using the parent class Person
student = Student("Jon", 202)  # create an object by using the  child class student
person.print_details()
student.print_details()
another_student = AnotherStudent("Robert", 303)  # method override using the parent class function
another_student.print_details()
