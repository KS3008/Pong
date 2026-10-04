import pygame

from screen import screen_width, screen_height

stick_width = 15
stick_height = 100

stick1 = pygame.Rect(0, screen_height / 2, stick_width, stick_height)
stick2 = pygame.Rect(screen_width - stick_width, screen_height / 2, stick_width, stick_height)