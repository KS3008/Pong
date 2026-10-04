import pygame
import random

from screen import screen
from screen import clock
from objects.ball import ball
from objects.sticks import stick1, stick2

pygame.init()

running = True

# POSITIONS
# ball
ball_x = 300 - ball.get_width() // 2
ball_y = random.randint(0, 600 - ball.get_height())

ball_v = 4

# sticks
stick_v = 4

# GAME LOOP

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # PLAYER MOVEMENTS
    keys = pygame.key.get_pressed()

    # player1 movements
    if keys[pygame.K_w]:
        stick1.y -= stick_v
    elif keys[pygame.K_s]:
        stick1.y += stick_v

    # player2 movements
    if keys[pygame.K_UP]:
        stick2.y -= stick_v
    elif keys[pygame.K_DOWN]:
        stick2.y += stick_v

    # DRAW
    screen.fill((255, 0, 255))
    pygame.draw.rect(screen, (0,0,255), stick1)
    pygame.draw.rect(screen, (255,0,0), stick2)
    screen.blit(ball, (ball_x, ball_y))

    # BALL MOVEMENTS
    ball_y += ball_v 
    ball_x += ball_v
    if ball_y >= 600 - ball.get_height()  or ball_y <= 0:
        ball_v = ball_v * (-1)

    if ball_x <= -ball.get_width() or ball_x >= 600:
        ball_x = 300 - ball.get_width() // 2
        ball_y = random.randint(0, 600 - ball.get_height())
    
    clock.tick(60)
    
    pygame.display.flip()


pygame.quit()