#!/usr/bin/python3
"""A class that inherits properties from my Base module"""
from models.base import Base


class Rectangle(Base):
    """A class that inherits properties from the Base model

    Args:
        Base : A defined model in the models directory
        """

    def __init__(self, width, height, x=0, y=0, id=None):
        """INitializes the instance of the class

        Args:
            width (int): _takes the width of the rectangle_
            height (int): _takes the height of the rectangle
            x (int, optional):  Defaults to 0.
            y (int, optional): Defaults to 0.
            id (_int_, optional): Defaults to None.
        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """takes in the width property an return the value of the width
        """
        return self.__width

    @width.setter
    def width(self, value):
        """gets the property of the width

        Args:
            value (_int_): _holds the value of the width_
        """
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """takes in the height property
        """

        return self.__height

    @height.setter
    def height(self, value):
        """gets the height property

        Args:
            value (_int_): _takes in the value for the height property_
        """

        if type(value) != int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """takes the x property"""
        return self.__x

    @x.setter
    def x(self, value):
        """sets the x property

         Args:
        value (_int_): takes in and store the value for x_
        """

        if type(value) != int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must >= 0")

        self.__x = value

    @property
    def y(self):
        """takes the x property"""
        return self.__y

    @y.setter
    def y(self, value):
        """sets the y property

       Args:
        value (_int_): takes in and store the value for y_
        """

        if type(value) != int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")

        self.__y = value

    def area(self):
        """A function that returns the area of a rectangle"""
        return (self.__width * self.__height)

    def display(self):
        """print the rectangle instance with '#'
        """
        rectangle = ""
        print_symbol = '#'
        
        print("\n" * self.y, end="")
        for i in range(self.height):
            rectangle += (" " * self.x) + (print_symbol*self.width) + "\n"
        print(rectangle, end="")
        
    def __str__(self):
        """returns a string format of the rectangle
        """
        return "[{}] ({}) {}/{} - {}/{}".format(type(self).__name__, self.id,
                                                self.__x, self.__y,
                                                self.__width, self.__height)
        
    
    def update(self, *args, **kwargs):
        """assigns key attributes to elements
        """
        if len(args) == 0:
            for key, val in kwargs.items():
                self.__setattr__(key,val)
            return
        
        try:
            self.id = args[0]
            self.width = args[1]
            self.height= args[2]
            self.x = args[3]
            self.y = args[4]
        except IndexError:
            pass
        
    
    def to_dictionary(self):
        """Method that returns the dictionary representation of a rectangle
        """
        return {'id': getattr(self, "id"), 'width': getattr(self, "width"),
                'height': getattr(self, "height"), 'x': getattr(self, "x"),
                'y': getattr(self, "y")}
    
    
    