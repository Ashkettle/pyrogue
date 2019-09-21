"""Represents a single tile on the map"""

import os
import pygame

class Tile:
    """A single given tile on the map"""
 
    def __init__(self, walkable: bool, tilesprite: str=None, is_revealed: bool=False, block_sight: bool=None):
        self.walkable = walkable
        self.is_revealed = is_revealed
        self.tilesprite = tilesprite
 
        # by default, if a tile is not walkable, it also blocks sight
        if block_sight is None:
            block_sight = not walkable
        self.block_sight = block_sight

    def load_sprite_image_from_file(self,relative_path_file):
        """Sets the sprite"""
        #dirname = os.path.dirname(__file__)
        #filename = os.path.join(dirname, relative_path_file)
        self.tilesprite = pygame.image.load(relative_path_file)
        #self.tilesprite = pygame.image.load(filename)

    @staticmethod
    def get_new_tile():
        """Factory method to create a new tile with default settings"""
        return Tile(walkable=False, is_revealed=False, block_sight=False)

