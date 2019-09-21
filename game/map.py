"""Map and Level Creation"""
import random
import game_settings
from tile import Tile
from rect import Rect

#I know the variables don't follow snake case, but x/y are what they really are.
# pylint: disable=C0103


class Map:
    """Representation of a Map containing a single level of a dungeon"""
    def __init__(self):
        self.floor = None
        self.height = None
        self.width = None
        self.tilesize = 16

    def render(self, surface):
        """render the map"""
        for x in range(self.width):
            for y in range(self.height):
                pos = (x * self.tilesize, y * self.tilesize)
                current_tile = self.floor[x][y]
                if current_tile.walkable and current_tile.is_revealed:
                    surface.blit(current_tile.tilesprite, pos)

    @staticmethod
    def _set_floor_tile(loc):
        """Set a tile as a floor tile"""
        loc.walkable = True
        loc.block_sight = False
        loc.is_revealed = True
        loc.load_sprite_image_from_file('./assets/floor.png')


    def _create_room(self):
        """Return a new random room"""
        # random width and height
        w = random.randint(game_settings.ROOM_MIN_SIZE, game_settings.ROOM_MAX_SIZE)
        h = random.randint(game_settings.ROOM_MIN_SIZE, game_settings.ROOM_MAX_SIZE)
        # random position without going out of the boundaries of the map
        x = random.randint(0, self.width - w - 1)
        y = random.randint(0, self.height - h - 1)

        return Rect(x, y, w, h)

    @staticmethod
    def _does_room_intersect(rooms, room_to_check):
        """returns true if room intersects with any other rooms already created"""
        intersects = False
        for other_room in rooms:
            if room_to_check.intersect(other_room):
                intersects = True
                break
        return intersects

    def _commit_new_room(self, room):
        """go through the tiles in the rectangle and make them passable"""
        for x in range(room.x1 + 1, room.x2):
            for y in range(room.y1 + 1, room.y2):
                Map._set_floor_tile(self.floor[x][y])


    def create_h_tunnel(self, x1, x2, y):
        """horizontal tunnel. min() and max() are used in case x1>x2 """
        for x in range(min(x1, x2), max(x1, x2) + 1):
            Map._set_floor_tile(self.floor[x][y])


    def create_v_tunnel(self, y1, y2, x):
        """vertical tunnel"""
        for y in range(min(y1, y2), max(y1, y2) + 1):
            Map._set_floor_tile(self.floor[x][y])

    def _initialize_map(self):
        """Initialize the map to all empty tiles"""
        self.floor = [[0 for y1 in range(self.height)] for x1 in range(self.width)]
        for x in range(self.width):
            for y in range(self.height):
                self.floor[x][y] = Tile.get_new_tile()

    def generate_map(self, height, width):
        """create a new map level"""
        self.height = height
        self.width = width

        self._initialize_map()

        # Create some rooms
        rooms = []
        num_rooms = 0


        # I know I'm not using r directly,
        # but it's used to iterate easily through my room count
        # pylint: disable=W0612
        for r in range(game_settings.MAX_ROOMS):
            new_room = self._create_room()

            if not Map._does_room_intersect(rooms, new_room):
                # this means there are no intersections, so this room is valid
                # "paint" it to the map's tiles
                self._commit_new_room(new_room)
                # center coordinates of new room, will be useful later
                (new_x, new_y) = new_room.center()
                if  num_rooms != 0:
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
