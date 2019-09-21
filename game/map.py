import pygame
import random
import settings
from tile import Tile
from rect import Rect


class Map:

    def __init__(self):
        self.floor = None
        self.height = None
        self.width = None
        self.tilesize = 16

    def render(self, surface):
        """render the sprite"""
        for x in range(self.width):
            for y in range(self.height):
                pos = (x * self.tilesize, y * self.tilesize)
                current_tile = self.floor[x][y]
                if current_tile.walkable and current_tile.is_revealed:
                    surface.blit(current_tile.tilesprite, pos)

    
    def set_floor_tile(self, loc):
        """Set a tile as a floor tile"""
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
        
        #Set map to all empty tiles
        self.floor =[[0 for y1 in range(height)] for x1 in range(width)]
        for x in range(self.width):
            for y in range(self.height):
                self.floor[x][y] = Tile.get_new_tile()

        # Create some rooms
        rooms = []
        num_rooms = 0
        
        for r in range(settings.MAX_ROOMS):
            # random width and height
            w = random.randint(settings.ROOM_MIN_SIZE, settings.ROOM_MAX_SIZE)
            h = random.randint(settings.ROOM_MIN_SIZE, settings.ROOM_MAX_SIZE)
            # random position without going out of the boundaries of the map
            x = random.randint(0, self.width - w - 1)
            y = random.randint(0, self.height - h - 1)
            
            new_room = Rect(x, y, w, h)
            # run through the other rooms and see if they intersect with this one
            failed = False
            for other_room in rooms:
                if new_room.intersect(other_room):
                    failed = True
                    break            
            if not failed:
                # this means there are no intersections, so this room is valid
                # "paint" it to the map's tiles
                self.create_room(new_room)  
                # center coordinates of new room, will be useful later
                (new_x, new_y) = new_room.center()         
                
                if not num_rooms == 0:
                    # all rooms after the first:
                    # connect it to the previous room with a tunnel
    
                    # center coordinates of previous room
                    (prev_x, prev_y) = rooms[num_rooms - 1].center()
    
                    # draw a coin (random number that is either 0 or 1)
                    if random.randint(0, 1) == 1:
                        # first move horizontally, then vertically
                        self.create_h_tunnel(prev_x, new_x, prev_y)
                        self.create_v_tunnel(prev_y, new_y, new_x)
                    else:
                        # first move vertically, then horizontally
                        self.create_v_tunnel(prev_y, new_y, prev_x)
                        self.create_h_tunnel(prev_x, new_x, new_y)
                
                # finally, append the new room to the list
                rooms.append(new_room)
                num_rooms += 1


 

                
