"""This module holds all the game settings for global access"""

WIDTH = 1024
HEIGHT = 768
FPS = 60
TITLE = "PyRogue"

# size of the map
MAP_WIDTH = 62
MAP_HEIGHT = 45
 
# parameters for dungeon generator
ROOM_MAX_SIZE = 10 
ROOM_MIN_SIZE = 6
MAX_ROOMS = 30

class Colors:
    """ Holds RGB values for basic colors """

    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)
    RED = (255, 0, 0)
    GREEN = (0, 255, 0)
    BLUE = (0, 0, 255)
