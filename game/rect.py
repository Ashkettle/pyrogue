"""Helper class for a RECT"""

#I know the variables don't follow snake case, but x/y are what they really are.
# pylint: disable=C0103


class Rect:
    """a rectangle on the map. used to characterize a room."""

    def __init__(self, x: int, y: int, width: int, height: int):
        """Create a new Rectangle"""
        self.x1 = x
        self.y1 = y
        self.x2 = x + width
        self.y2 = y + height

    def center(self):
        """Find the center of the rectangle"""
        center_x = (self.x1 + self.x2) // 2
        center_y = (self.y1 + self.y2) // 2
        return (center_x, center_y)

    def intersect(self, other):
        """returns true if this rectangle intersects with another one"""
        return (self.x1 <= other.x2 and self.x2 >= other.x1 and
                self.y1 <= other.y2 and self.y2 >= other.y1)
