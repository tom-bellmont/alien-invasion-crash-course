import pygame
from settings import Settings
from ship import Ship
import game_functions as gf

def run_game():
    """
    Initialize pygame, settings and screen object.
    """ 

    # Initialise game and create a screen object.
    pygame.init()
    ai_settings = Settings()
    # Call pygame.display.set_mode() to create a display window called "screen"
    screen = pygame.display.set_mode(
        (ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")

    # Make a ship
    ship = Ship(screen)

    # Start the main loop for the game.
    while True:
        # Watch for keyboard and mouse events.
        gf.check_events()

        # Redraw the screen during each pass through the loop.
        screen.fill(ai_settings.bg_colour)
        ship.blitme()

        # Make the most recently drawn screen visible.
        pygame.display.flip()

run_game()