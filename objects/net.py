import pygame

from screen import screen_width

net_width = 5
net_x = screen_width / 2 - net_width / 2
net_y = 5
net = pygame.Rect(net_x, net_y, net_width, 15)