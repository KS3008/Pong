import pygame

ball = pygame.image.load('objects/ball.png').convert_alpha()
ball = pygame.transform.scale(ball, 
                              (ball.get_width() // 15,
                               ball.get_height() // 15))