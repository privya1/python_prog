class Point():
    """
    This is the program of a point co-ordinate in 2D space
    """
    def __init__(self, x = 0, y = 0):
        self.x = x
        self.y = y
    """
    This initializing the values of point co-ordinate
    """

    def move(self, x, y):
        self.x = x
        self.y = y
    """
    This is moving the values of point co-ordinate to a new value
    """

    def reset(self):
        self.x = 0
        self.y = 0
    """
    This is moving the point co-ordinate to origin
    """

    def print(current):
        print(current.x, current.y)
    """
    This is to print the current values of point co-ordinate
    """

p = Point(4,5)
"""
This is to create an object p with values 4 and 5
"""

p.print()
p.move(2,3)
p.print()
p.reset()
p.print()
"""
This is printing the values of point co-ordinate, moving to new location and resetting to origin.
"""
