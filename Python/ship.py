# -*- coding: utf-8 -*-
"""
Created on Tue Jul 20 08:25:36 2021

@author: Aderoju Adeyemi
"""

import pygame
 
class Ship:
    """A class to manage the ship."""
 
    def __init__(self, ai_game):
        """Initialize the ship and set its starting position."""
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()
        
        # Movement flag
        self.moving_right = False
        self.moving_left = False
        self.settings = ai_game.setting
        
        # Load the ship image and get its rect.
        self.image = pygame.image.load('C:/Users/Aderoju Adeyemi/Documents/Program/Alien_Invasion/images/ship.bmp')
        self.rect = self.image.get_rect()
        
        # Store a decimal value for the ship's horizontal position
        self.x = float(self.rect.x)

        # Start each new ship at the bottom center of the screen.
        self.rect.midbottom = self.screen_rect.midbottom
        
    def update(self):
        """Update the ship's position based on the movement flag."""
        if self.moving_right:
            self.x += self.settings.ship_speed
        if self.moving_left:
            self.x -= self.settings.ship_speed
            
        # Update rect object from self.x.
        self.rect.x = self.x
    def blitme(self):
        """Draw the ship at its current location."""
        self.screen.blit(self.image, self.rect)
