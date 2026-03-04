#import modules(pygame,random and time)

#pygame play game

#player variables for size and speed

#color codes

#set screen width and lifetime#main game loop 
#game over = false

#x,y coordinate creation 
#make circle food 

#loop for player control
#if player hits escape = pygame.quit
#if statement to pygame.key for controls and movement 
#if player is outside of screen area gameover = false 

#fill screen with black background
#update display

#set clock speed to palyer speed 
#if pygame = game over then print game over and time.sleep,game_loop 
#game_loop 
import pygame
import random
import time

def play_game():
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

    x = WIDTH // 2
    y = HEIGHT // 2
    x_change = SNAKE_SIZE  # Renamed for consistency
    y_change = 0

    snake_pixels = [[x, y]]
    score = 0

    food_x = random.randrange(0, WIDTH // SNAKE_SIZE) * SNAKE_SIZE
    food_y = random.randrange(0, HEIGHT // SNAKE_SIZE) * SNAKE_SIZE

    game_over = False
    while not game_over:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return score  # Early exit returns current score
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT and x_change != SNAKE_SIZE:
                    x_change, y_change = -SNAKE_SIZE, 0
                elif event.key == pygame.K_RIGHT and x_change != -SNAKE_SIZE:
                    x_change, y_change = SNAKE_SIZE, 0
                elif event.key == pygame.K_UP and y_change != SNAKE_SIZE:
                    x_change, y_change = 0, -SNAKE_SIZE
                elif event.key == pygame.K_DOWN and y_change != -SNAKE_SIZE:
                    x_change, y_change = 0, SNAKE_SIZE

        x += x_change
        y += y_change

        if x < 0 or x >= WIDTH or y < 0 or y >= HEIGHT:
            game_over = True

        head = [x, y]
        snake_pixels.append(head)

        if x == food_x and y == food_y:
            # Prevent food on snake (edge case)
            while [food_x, food_y] in snake_pixels:
                food_x = random.randrange(0, WIDTH // SNAKE_SIZE) * SNAKE_SIZE
                food_y = random.randrange(0, HEIGHT // SNAKE_SIZE) * SNAKE_SIZE
            score += 10
        else:
            snake_pixels.pop(0)

        if head in snake_pixels[:-1]:
            game_over = True

        screen.fill(BLACK)
        for px, py in snake_pixels:
            center = (px + SNAKE_SIZE // 2, py + SNAKE_SIZE // 2)
            pygame.draw.circle(screen, GREEN, center, SNAKE_SIZE // 2)

        food_center = (food_x + SNAKE_SIZE // 2, food_y + SNAKE_SIZE // 2)
        pygame.draw.circle(screen, RED, food_center, SNAKE_SIZE // 2)

        score_text = font.render(f"Score: {score}", True, WHITE)
        screen.blit(score_text, (10, 10))

        pygame.display.update()
        clock.tick(SPEED)

    # Game over display
    screen.fill(BLACK)
    game_over_text = font.render("Game Over!", True, RED)
    final_score_text = font.render(f"Final Score: {score}", True, WHITE)
    screen.blit(game_over_text, (WIDTH // 2 - game_over_text.get_width() // 2, HEIGHT // 2 - 60))
    screen.blit(final_score_text, (WIDTH // 2 - final_score_text.get_width() // 2, HEIGHT // 2))
    pygame.display.update()
    time.sleep(2)
    pygame.quit()

    return score