import pygame
import random
import time

pygame.init()

WIDTH, HEIGHT = 800, 600
SNAKE_SIZE = 20
SPEED = 10

WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (213, 50, 80)
BLACK = (0, 0, 0)

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Python Snake.io')
clock = pygame.time.Clock()
font = pygame.font.SysFont("comicsansms", 25)


def game_loop():
    game_over = False


    x = WIDTH // 2
    y = HEIGHT // 2
    x_axis = SNAKE_SIZE
    Y_axis = 0

    snake_pixels = [[x, y]]
    score = 0


    XFOOD = random.randrange(0, WIDTH // SNAKE_SIZE) * SNAKE_SIZE
    YFOOD = random.randrange(0, HEIGHT // SNAKE_SIZE) * SNAKE_SIZE

    while not game_over:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.KEYDOWN:
                
                if event.key == pygame.K_LEFT and x_axis != SNAKE_SIZE:
                    x_axis, Y_axis = -SNAKE_SIZE, 0
                elif event.key == pygame.K_RIGHT and x_axis != -SNAKE_SIZE:
                    x_axis, Y_axis = SNAKE_SIZE, 0
                elif event.key == pygame.K_UP and Y_axis != SNAKE_SIZE:
                    x_axis, Y_axis = 0, -SNAKE_SIZE
                elif event.key == pygame.K_DOWN and Y_axis != -SNAKE_SIZE:
                    x_axis, Y_axis = 0, SNAKE_SIZE

       
        x += x_axis
        y += Y_axis

        
        if x < 0 or x >= WIDTH or y < 0 or y >= HEIGHT:
            game_over = True

        
        head = [x, y]
        snake_pixels.append(head)

        
        if x == XFOOD and y == YFOOD:
            XFOOD = random.randrange(0, WIDTH // SNAKE_SIZE) * SNAKE_SIZE
            YFOOD = random.randrange(0, HEIGHT // SNAKE_SIZE) * SNAKE_SIZE
            score += 10
        else:
            snake_pixels.pop(0)  

        if head in snake_pixels[:-1]:
            game_over = True

     
        screen.fill(BLACK)

        for px, py in snake_pixels:
            center = (px + SNAKE_SIZE // 2, py + SNAKE_SIZE // 2)
            pygame.draw.circle(screen, GREEN, center, SNAKE_SIZE // 2)

        food_center = (XFOOD + SNAKE_SIZE // 2, YFOOD + SNAKE_SIZE // 2)
        pygame.draw.circle(screen, RED, food_center, SNAKE_SIZE // 2)

   
        score_text = font.render(f"Score: {score}", True, WHITE)
        screen.blit(score_text, (10, 10))

        pygame.display.update()
        clock.tick(SPEED)


    screen.fill(BLACK)
    over_text = font.render("Game Over!", True, RED)
    final_score = font.render(f"Final Score: {score}", True, WHITE)
    screen.blit(over_text, (WIDTH // 2 - over_text.get_width() // 2, HEIGHT // 2 - 60))
    screen.blit(final_score, (WIDTH // 2 - final_score.get_width() // 2, HEIGHT // 2))
    pygame.display.update()
    time.sleep(2)

while True:
    game_loop()