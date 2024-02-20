""" a Rectangle subclass Square."""
Rectangle = __import__('9-rectangle').Rectangle

class Square(Rectangle):
    """Represents a square.

    This class is a subclass of Rectangle and represents a square. It inherits
    attributes and methods from the Rectangle class.

    Attributes:
        size (int): The size of the square's sides.
    """

    def __init__(self, size):
        """Initialize a new square.

        Args:
            size (int): The size of the new square.
        """
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(self.__size, self.__size)
    def __str__(self):
        ''' Return square description '''
        return ("[Square] {}/{}".format(self.__size, self.__size))
