"""
Main entrypoint for game
"""
import pygame
import settings


class Game:
    """Representation of the Game itself"""
    def __init__(self):
        """
        initialize pygame and create window
        """
        pygame.init()
        #pygame.mixer.init()  # for sound
        self.screen = pygame.display.set_mode((settings.WIDTH, settings.HEIGHT))
        pygame.display.set_caption(settings.TITLE)
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

            # Update
            self.set_player_movement()
            #keys = pygame.key.get_pressed()
            #if keys[pygame.K_LEFT]:
            #   pass
            # Render
            self.screen.fill(settings.Colors.BLACK)
            pygame.display.update()
        pygame.quit()
if __name__ == "__main__":
    GAME = Game()
    GAME.start_game()
