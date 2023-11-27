#!/usr/bin/python3
"""A class that defines a rectangle"""


class Rectangle:
    """A class that represents a rectangle"""
    
    def __init__(self, width, height):
        """Initializes the instances of the class

        Args:
            width (_int_): _takes and define the width_
            height (_type_): _takes and define the height_
        """
        self.__width = width
        self.__height = height
        
    @property
    def height(self):
        """sets the height attribute

        Args:
            value (_int_): _stores the value of the height_
            
        """
        return self.__height
    
    @height.setter
    def height(self, value):
        """the height setter
    

        Args:
            value (_int_): _holds the value for height_

        Raises:
            TypeError: _when the value is not an integer_
            ValueError: _when the value is < 0_
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must >= 0")
        
        self.__height = value

        
        
    @property
    def width(self):
        """defines the property width of the class
        """
        
        return self.__width
    
    @width.setter
    def width(self, value):
        """Sets the property width

        Args:
            value (_int_): _stores the value of the width_
        """
        
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
            
        self.__width = value
        
  