# -*- coding: utf-8 -*-

class Settings():
    def __init__(self):
        self.screen_width = 800
        self.screen_height = 600
        self.bg_color = (220, 220, 220)
        self.ship_speed_factor = 0.1
        self.ship_limit = 1

        self.bullet_speed_factor = 0.3
        self.bullet_width = 2
        self.bullet_height = 5
        self.bullet_color = 60,60,60
        self.bullets_allowed = 100

        self.alien_speed_factor = 0.1
        self.fleet_drop_speed = 50
        self.fleet_direction = 1


class GameStats():
    def __init__(self, new_setting):
        self.new_setting = new_setting
        self.reset_stats()

    def reset_stats(self):
        self.ships_left = self.new_setting.ship_limit