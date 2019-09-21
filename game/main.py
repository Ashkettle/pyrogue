"""
Main entrypoint for game
"""
import pygame
from pygame.locals import VIDEORESIZE, HWSURFACE, DOUBLEBUF, RESIZABLE
import game_settings
from map import Map



class Game:
    """Representation of the Game itself"""
    def __init__(self):
        """
        initialize pygame and create window
        """
        pygame.init()
        #pygame.mixer.init()  # for sound
        self.screen = pygame.display.set_mode((game_settings.WIDTH, game_settings.HEIGHT))
        self.draw_surface = self.screen.copy()
        pygame.display.set_caption(game_settings.TITLE)
        self.current_width = game_settings.WIDTH
        self.current_height = game_settings.HEIGHT

        self.map = Map()
        self.map.generate_map(game_settings.MAP_HEIGHT, game_settings.MAP_WIDTH)

        self.clock = pygame.time.Clock()



    def set_player_movement(self):
        """
        Update any player movement here
        """

    def start_game(self):
        """ Game Loop  """
        running = True
        while running:
            self.clock.tick(30)

            # Process input (events)
            for event in pygame.event.get():
                # check for closing window
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == VIDEORESIZE:
                    self.current_width = event.w
                    self.current_height = event.h
                    self.screen = pygame.display.set_mode((self.current_width, self.current_height),
                                                          HWSURFACE|DOUBLEBUF|RESIZABLE)
            # Update
            self.set_player_movement()
            #keys = pygame.key.get_pressed()
            #if keys[pygame.K_LEFT]:
            #   pass
            # Render
            self.draw_surface.fill(game_settings.Colors.BLACK)
            self.map.render(self.draw_surface)
            background = pygame.transform.scale(self.draw_surface,
                                                (self.current_width, self.current_height))
            self.screen.blit(background, (0, 0))

            pygame.display.update()
        pygame.quit()
if __name__ == "__main__":
    GAME = Game()
    GAME.start_game()
