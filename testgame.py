import pygame
import math
import random

# Setup
pygame.init()
WIDTH, HEIGHT = 1000, 700
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Neon Snake.io")
clock = pygame.time.Clock()

# Colors
BG_COLOR = (10, 10, 20)
SNAKE_COLOR = (0, 255, 200)
FOOD_COLOR = (255, 50, 150)

# Game Variables
x, y = WIDTH // 2, HEIGHT // 2
angle = 0
base_speed = 3
snake_length = 40
path = []
particles = []

# Food
food = [random.randint(50, WIDTH-50), random.randint(50, HEIGHT-50)]

def draw_glow_circle(surf, color, pos, radius):
    """Creates a soft neon glow effect."""
    for i in range(3, 0, -1):
        alpha = 100 // i
        s = pygame.Surface((radius * 4, radius * 4), pygame.SRCALPHA)
        pygame.draw.circle(s, (*color, alpha), (radius * 2, radius * 2), radius + (i * 4))
        surf.blit(s, (pos[0] - radius * 2, pos[1] - radius * 2))

running = True
while running:
    screen.fill(BG_COLOR)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # 1. Input & Boosting
    keys = pygame.key.get_pressed()
    speed = base_speed * 2 if keys[pygame.K_SPACE] else base_speed
    if keys[pygame.K_LEFT]: angle -= 0.08
    if keys[pygame.K_RIGHT]: angle += 0.08

    # 2. Movement & Screen Wrap
    x = (x + speed * math.cos(angle)) % WIDTH
    y = (y + speed * math.sin(angle)) % HEIGHT

    # 3. Path Management
    path.append((x, y))
    if len(path) > snake_length:
        path.pop(0)

    # 4. Food & Particles
    if math.hypot(x - food[0], y - food[1]) < 25:
        snake_length += 15
        # Create particles
        for _ in range(10):
            particles.append([[food[0], food[1]], [random.uniform(-2, 2), random.uniform(-2, 2)], 10])
        food = [random.randint(50, WIDTH-50), random.randint(50, HEIGHT-50)]

    # 5. Drawing Particles
    for p in particles[:]:
        p[0][0] += p[1][0]
        p[0][1] += p[1][1]
        p[2] -= 0.2
        if p[2] <= 0: particles.remove(p)
        else: pygame.draw.circle(screen, FOOD_COLOR, (int(p[0][0]), int(p[0][1])), int(p[2]))

    # 6. Drawing Food
    draw_glow_circle(screen, FOOD_COLOR, food, 8)
    pygame.draw.circle(screen, (255, 255, 255), food, 4)

    # 7. Drawing Snake (Shadow/Glow first, then Body)
    for i, pos in enumerate(path[::4]):
        # Dynamic pulse effect for the body
        pulse = math.sin(pygame.time.get_ticks() * 0.01 + i) * 2
        draw_glow_circle(screen, SNAKE_COLOR, pos, 8 + pulse)
        pygame.draw.circle(screen, (255, 255, 255), (int(pos[0]), int(pos[1])), 6)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()