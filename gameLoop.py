import pygame
import random

pygame.init()

from screen import screen, screen_height, screen_width
from screen import clock

from objects.ball import ball
from objects.sticks import stick1, stick2
from objects.net import net, net_y

from sounds.ball_sound import random_sounds


running = True

# COUNTERS
game_font = pygame.font.Font(None, 90)
count1 = 0
count2 = 0

# POSITIONS
# ball
ball_x = 300 - ball.get_width() // 2
ball_y = random.randint(0, 600 - ball.get_height())

ball_v_x = 4
ball_v_y = 4

ball_rect = ball.get_rect()

# sticks
stick_v = 8

# GAME LOOP

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # PLAYER MOVEMENTS
    keys = pygame.key.get_pressed()

    # player1 movements
    if keys[pygame.K_w] and stick1.y >= 0:
        stick1.y -= stick_v
    elif keys[pygame.K_s] and stick1.bottom < screen_height:
        stick1.y += stick_v

    # player2 movements
    if keys[pygame.K_UP] and stick2.y >= 0:
        stick2.y -= stick_v
    elif keys[pygame.K_DOWN] and stick2.bottom < screen_height:
        stick2.y += stick_v

    # DRAW
    screen.fill((0, 0, 0))
    # scores
    scores = f"{count1}      {count2}"
    scores_print = game_font.render(str(scores), True, (255,255,255))
    screen.blit(scores_print, (screen_width / 2 - scores_print.width / 2, 50))
    # players
    pygame.draw.rect(screen, (0,0,133), stick1)
    pygame.draw.rect(screen, (255,0,0), stick2)
    # net
    for net_y in range(5, screen_height, 20):
        net.y = net_y
        pygame.draw.rect(screen, (0,0,133), net)
    # ball
    screen.blit(ball, (ball_x, ball_y))
        

    # BALL MOVEMENTS
    ghost_rect = ball_rect.copy()
    ball_y += ball_v_y 
    ball_x += ball_v_x
    ball_rect.x = ball_x
    ball_rect.y = ball_y

    if ball_y >= 600 - ball.get_height()  or ball_y <= 0:
        ball_v_y = ball_v_y * (-1)

    
    # PLAYER 1 points
    if ball_x <= -ball.get_width():
        count2 += 1
        ball_x = 300 - ball.get_width() // 2
        ball_y = random.randint(0, 600 - ball.get_height())
    
        ball_v_x = random.choice([4, -4])
        ball_v_y = random.choice([4, -4])

    # PLAYER 2 points
    if ball_x >= screen_width:
        count1 += 1
        ball_x = 300 - ball.get_width() // 2
        ball_y = random.randint(0, 600 - ball.get_height())

        ball_v_x = random.choice([4, -4])
        ball_v_y = random.choice([4, -4])

    # HITBOX and BALL SOUND
    if ball_rect.colliderect(stick1) and ball_v_x < 0:
        chosen_sound = random.choice(random_sounds)
        chosen_sound.play()
        if ghost_rect.bottom <= stick1.top:
            ball_v_y = ball_v_y * -1
        elif ghost_rect.top >= stick1.bottom:
            ball_v_y = ball_v_y * -1
        else:
             ball_v_x = ball_v_x * -1

    if ball_rect.colliderect(stick2) and ball_v_x > 0:
            chosen_sound = random.choice(random_sounds)
            chosen_sound.play()
            if ghost_rect.bottom <= stick2.top:
                ball_v_y = ball_v_y * -1
            elif ghost_rect.top >= stick2.bottom:
                ball_v_y = ball_v_y * -1 
            else:
                ball_v_x = ball_v_x * -1


    
    clock.tick(60)
    
    pygame.display.flip()


pygame.quit()