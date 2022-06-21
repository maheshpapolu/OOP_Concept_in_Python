# to define a class using the class keyword in simple way
class Point:
    def move(self):
        """
        define a method called move in class point
        :return:
        """
        print("move")

    def draw(self):
        """
        define a draw method called draw in class point
        :return:
        """
        print("draw")


point1 = Point()  # creating an object for class point
point1.draw()   # calling a method in the point class
