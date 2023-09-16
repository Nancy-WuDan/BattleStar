# -*- coding: utf-8 -*-

import sys
import pygame
import Settings
from Ship import Ship
import game_functions as gf
from pygame.sprite import Group
from Alien import Alien
from Settings import GameStats


def run_game():
    # 初始化游戏对象
    pygame.init()
    new_setting = Settings.Settings()

    # display是Pygame中用于管理屏幕和窗口的模块
    # 显示模块、设置屏幕分辨率、创建游戏窗口、更新窗口内容、处理事件等功能的函数
    screen = pygame.display.set_mode((new_setting.screen_width,new_setting.screen_height))
    ship = Ship(screen, new_setting)
    pygame.display.set_caption("Alien Invasion")

    bullets = Group()
    aliens = Group()
    gf.create_fleet(new_setting, screen, aliens)
    stats = GameStats(new_setting)

    # 一直监听鼠标和键盘的操作
    while True:
        # -----------------PROCESS 1： 监听用户操作-----------------
        gf.check_events(new_setting, screen, ship, bullets)
        ship.update()
        gf.update_bullets(new_setting, screen, bullets, aliens)
        gf.update_aliens(new_setting,stats,screen,ship,aliens,bullets)
        # ----------------PROCESS 2: 绘制窗口-------------------------
        gf.update_screen(new_setting, screen, ship, bullets, aliens)

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    run_game()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
