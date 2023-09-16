# -*- coding: utf-8 -*-
import random
import sys
import time

import pygame
from Bullet import Bullet
from Alien import Alien

def check_keydown_events(event, new_setting, screen, ship, bullets):
    if event.key == pygame.K_RIGHT:
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        ship.moving_left = True
    elif event.key == pygame.K_SPACE:
        fire_bullet(new_setting, screen, ship, bullets)


def check_keyup_events(event, ship):
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False

    if event.key == pygame.K_LEFT:
        ship.moving_left = False


def check_events(new_setting, screen, ship, bullets):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, new_setting, screen, ship, bullets)

        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ship)


def fire_bullet(new_setting, screen, ship, bullets):
    if len(bullets) < new_setting.bullets_allowed:
        new_bullet = Bullet(new_setting, screen, ship)
        bullets.add(new_bullet)


def update_bullets(new_setting, screen, bullets, aliens):
    check_bullet_alien_collisions(new_setting, screen, bullets, aliens)
    bullets.update()
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)


def check_bullet_alien_collisions(new_setting, screen, bullets, aliens):
    collisions = pygame.sprite.groupcollide(bullets, aliens, True, True)
    if len(aliens) == 0:
        bullets.empty()
        create_fleet(new_setting, screen, aliens)



def ship_hit(new_setting,stats,screen,ship,aliens,bullets):
    stats.ships_left -= 1
    aliens.empty()
    bullets.empty()
    create_fleet(new_setting, screen, aliens)
    ship.center_ship()
    if stats.ships_left > 0:
        stats.ships_left -= 1
        time.sleep(0.5)
    else:
        stats.game_active = False


def check_aliens_bottom(new_setting, stats, screen, ship, aliens, bullets):
    screen_rect = screen.get_rect()
    for alien in aliens.sprites():
        if alien.rect.bottom >= screen_rect.bottom:
            ship_hit(new_setting, stats, screen, ship, aliens, bullets)
            break


def update_aliens(new_setting, stats, screen, ship, aliens, bullets):
    check_fleet_edges(new_setting, aliens)
    aliens.update()
    if pygame.sprite.spritecollideany(ship, aliens):
        ship_hit(new_setting, stats, screen, ship, aliens, bullets)

    check_aliens_bottom(new_setting, stats, screen, ship, aliens, bullets)

def update_aliens(new_setting,stats,screen,ship,aliens,bullets):
    check_fleet_edges(new_setting,aliens)
    aliens.update()
    #pygame.sprite.spritecollideany(ship, aliens)
    #是Pygame库中的一个函数，用于检测一个精灵是否与一组精灵中的任意一个发生了碰撞。
    # 其中，ship是一个精灵对象，aliens是一个精灵组对象。
    # 如果ship与aliens中的任意一个精灵发生了碰撞，该函数会返回True，否则返回False。
    if pygame.sprite.spritecollideany(ship,aliens):
        ship_hit(new_setting, stats, screen, ship, aliens, bullets)


def change_fleet_direction(new_setting,aliens):
    for alien in aliens.sprites():
        alien.rect.y += new_setting.fleet_drop_speed

    new_setting.fleet_direction *=-1


def check_fleet_edges(new_setting,aliens):
    for alien in aliens.sprites():
        if alien.check_edges():
            change_fleet_direction(new_setting,aliens)
            break


def create_fleet(new_setting,screen,aliens):
    for row_number in range(3):
        for alien_number in range(12):
            alien = Alien(new_setting,screen)
            alien.x = alien.rect.width+2*alien.rect.width*alien_number
            alien.rect.x = alien.x
            alien.rect.y = alien.rect.height+2*alien.rect.height*row_number
            aliens.add(alien)


def update_screen(new_setting, screen, ship, bullets, aliens):
    # 设备背景色，Nancy TBD: 如何设置背景图片？
    screen.fill(new_setting.bg_color)

    for bullet in bullets.sprites():
        bullet.draw_bullet()


    ship.blitme()
    aliens.draw(screen)

    # 不断的刷新屏幕，保持动态效果
    pygame.display.flip()