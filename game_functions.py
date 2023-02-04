import sys
import pygame

def check_events():
    """Repond to keypresses and mouth events."""
    for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()