# -*- coding: utf-8 -*-

import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    def __init__(self, new_setting, screen):
        super(Alien, self).__init__()
        self.screen = screen
        self.new_setting = new_setting

        self.image = pygame.transform.scale(pygame.image.load('./image/alien/alien.jpg'), (20, 20))
        self.rect = self.image.get_rect()

        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

    def blitme(self):
        self.screen.blit(self.image, self.rect)

    def update(self):
        self.x += (self.new_setting.alien_speed_factor * self.new_setting.fleet_direction)
        self.rect.x = self.x


    def check_edges(self):
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right:
            return True
        elif self.rect.left <= 0:
            return True
        else:
            return False