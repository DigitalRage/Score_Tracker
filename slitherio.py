import pygame
import random as r


def run():
    pygame.init()

    width, height = 800, 600
    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption("Slither.io - simple")
    clock = pygame.time.Clock()

    # Snake setup (use Vector2 for positions so vector math works)
    snake_pos = [pygame.Vector2(width // 2, height // 2)]
    snake_len = 10
    direction = pygame.Vector2(1, 0)
    speed = 3

    # Food setup
    food = pygame.Vector2(r.randint(20, width - 20), r.randint(20, height - 20))

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Handle input (don't allow 180-degree reversal)
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP] and direction.y != 1:
            direction = pygame.Vector2(0, -1)
        if keys[pygame.K_DOWN] and direction.y != -1:
            direction = pygame.Vector2(0, 1)
        if keys[pygame.K_LEFT] and direction.x != 1:
            direction = pygame.Vector2(-1, 0)
        if keys[pygame.K_RIGHT] and direction.x != -1:
            direction = pygame.Vector2(1, 0)

        # Move snake
        head = snake_pos[0] + direction * speed
        snake_pos.insert(0, head)
        if len(snake_pos) > snake_len:
            snake_pos.pop()

        # Check food collision
        if snake_pos[0].distance_to(food) < 10:
            snake_len += 5
            food = pygame.Vector2(r.randint(20, width - 20), r.randint(20, height - 20))

        # Check self collision
        for segment in snake_pos[1:]:
            if snake_pos[0].distance_to(segment) < 5:
                running = False

        # Draw everything
        screen.fill((0, 0, 0))  # clear screen
        for segment in snake_pos:
            pygame.draw.circle(screen, (0, 255, 0), (int(segment.x), int(segment.y)), 5)
        pygame.draw.circle(screen, (255, 0, 0), (int(food.x), int(food.y)), 5)

        pygame.display.flip()
        clock.tick(60)


if __name__ == "__main__":
    run()
    pygame.quit()