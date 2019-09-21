import pygame
from tile import Tile
from rect import Rect


class Map:

    def __init__(self):
        self.floor = None
        self.height = None
        self.width = None
        self.tilesize = 16


    def set_floor_tile(self, loc):
        loc.walkable = True
        loc.block_sight = False
        loc.is_revealed = True
        loc.load_sprite_image_from_file('./assets/floor.png')

    def create_room(self, room):
        # go through the tiles in the rectangle and make them passable
        for x in range(room.x1 + 1, room.x2):
            for y in range(room.y1 + 1, room.y2):
                self.set_floor_tile(self.floor[x][y])
               
    
    def create_h_tunnel(self, x1, x2, y):
        # horizontal tunnel. min() and max() are used in case x1>x2
        for x in range(min(x1, x2), max(x1, x2) + 1):
            self.set_floor_tile(self.floor[x][y])
    
    
    def create_v_tunnel(self, y1, y2, x):
        # vertical tunnel
        for y in range(min(y1, y2), max(y1, y2) + 1):
            self.set_floor_tile(self.floor[x][y])

    def generate_map(self, height, width):
        """Initialize the map"""
        self.height = height
        self.width = width
        self.floor =[[0 for y1 in range(height)] for x1 in range(width)]
        for x in range(self.width):
            for y in range(self.height):
                self.floor[x][y] = Tile.get_new_tile()

        # Now create a room
        room = Rect(10, 10, 20, 30)
        self.create_room(room)

    
    def render(self, surface):
        """render the sprite"""
        for x in range(self.width):
            for y in range(self.height):
                pos = (x * self.tilesize, y * self.tilesize)
                current_tile = self.floor[x][y]
                if current_tile.walkable and current_tile.is_revealed:
                    surface.blit(current_tile.tilesprite, pos)
                
