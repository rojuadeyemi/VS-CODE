# -*- coding: utf-8 -*-
"""
Created on Tue Jul 20 08:23:03 2021

@author: Aderoju Adeyemi
"""

import sys
import pygame
from ship import Ship
from settings import Settings

class AlienInvasion:

    def __init__(self):

        """Initialize the game, and create game resources."""
        pygame.init()
        self.setting = Settings()
        self.screen = pygame.display.set_mode((self.setting.screen_width, self.setting.screen_height))
        self.ship = Ship(self)
        pygame.display.set_caption("Alien Invasion")

    def _check_events(self):

        """Respond to keypresses and mouse events."""

        for event in pygame.event.get():

            if event.type == pygame.QUIT:

                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)
    
    def _check_keydown_events(self, event):
        """Respond to keypresses."""
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = True
            
    def _check_keyup_events(self, event):
        """Respond to key releases."""
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False

    def _update_screen(self):

        """Update images on the screen, and flip to the new screen."""

        self.screen.fill(self.setting.bg_color)

        self.ship.blitme()

        pygame.display.flip()

    def run_game(self):
        while True:
            self._check_events()
            self._update_screen()
            self.ship.update()

if __name__ == '__main__':

# Make a game instance, and run the game.

    ai = AlienInvasion()

    ai.run_game()