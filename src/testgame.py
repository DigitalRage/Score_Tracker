#import pygame
#import random
#import time
#
#
#pygame.init()
#
#
#WIDTH, HEIGHT = 800, 600
#SNAKE_SIZE = 20
#SPEED = 10
#
#
#WHITE = (255, 255, 255)
#GREEN = (0, 255, 0)
#RED = (213, 50, 80)
#BLACK = (0, 0, 0)
#
#
#screen = pygame.display.set_mode((WIDTH, HEIGHT))
#pygame.display.set_caption('Python Snake.io')
#clock = pygame.time.Clock()
#
#def game_loop():
#    game_over = False
#    
#   
#    x, y = WIDTH // 2, HEIGHT // 2
#    dx, dy = 0, 0
#    
#    snake_pixels = []
#    snake_length = 1
#
# 
#    food_x = round(random.randrange(0, WIDTH - SNAKE_SIZE) / 20.0) * 100.0
#    food_y = round(random.randrange(0, HEIGHT - SNAKE_SIZE) / 20.0) * 100.0
#
#    while not game_over:
#        for event in pygame.event.get():
#            if event.type == pygame.QUIT:
#                pygame.quit()
#                quit()
#        
#            if event.type == pygame.KEYDOWN:
#                if event.key == pygame.K_LEFT and dx == 0:
#                    dx, dy = -SNAKE_SIZE, 0
#                elif event.key == pygame.K_RIGHT and dx == 0:
#                    dx, dy = SNAKE_SIZE, 0
#                elif event.key == pygame.K_UP and dy == 0:
#                    dx, dy = 0, -SNAKE_SIZE
#                elif event.key == pygame.K_DOWN and dy == 0:
#                    dx, dy = 0, SNAKE_SIZE
#
#
#        if x >= WIDTH or x < 0 or y >= HEIGHT or y < 0:
#            game_over = True
#
#        x += dx
#        y += dy
#        screen.fill(BLACK)
#
#     
#        pygame.draw.circle(screen, RED, (int(food_x + SNAKE_SIZE), int(food_y + SNAKE_SIZE)), SNAKE_SIZE)
#
#        
#        snake_pixels.append([x, y])
#        if len(snake_pixels) > snake_length:
#            del snake_pixels[0]
#
#        
#        for pixel in snake_pixels[:-1]:
#            if pixel == [x, y]:
#                game_over = True
#
#  
#        for pixel in snake_pixels:
#            pygame.draw.circle(screen, GREEN, (pixel[0], pixel[1]), SNAKE_SIZE, SNAKE_SIZE)
##pygame.draw.circle(screen, GREEN,(int(pixel[0],pixel[1]),SNAKE_SIZE, SNAKE_SIZE])
#        pygame.display.update()
#
#        
#        if x == food_x and y == food_y:
#            food_x = round(random.randrange(0, WIDTH - SNAKE_SIZE) / 20.0) * 20.0
#            food_y = round(random.randrange(0, HEIGHT - SNAKE_SIZE) / 20.0) * 20.0
#            snake_length += 1
#
#        clock.tick(SPEED)
#
#   
#    print("Game Over!")
#    time.sleep(1)
#    game_loop()
#
#game_loop()