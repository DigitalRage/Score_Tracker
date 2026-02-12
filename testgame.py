import pygame
import math
import random

# --- SETTINGS ---
WIDTH, HEIGHT = 1100, 800
WORLD_SIZE = 3000  # Total playable area
FPS = 60
SNAKE_COLOR = (0, 255, 200)
FOOD_COLOR = (255, 50, 150)
BG_COLOR = (5, 5, 12)

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
font = pygame.font.SysFont("Verdana", 24, bold=True)

# --- GAME STATE ---
world_x, world_y = WORLD_SIZE // 2, WORLD_SIZE // 2
angle = 0
base_speed = 4
snake_len = 60
path = []  # Stores (world_x, world_y)
score = 0
is_alive = True

# Food & Particles
foods = [[random.randint(0, WORLD_SIZE), random.randint(0, WORLD_SIZE)] for _ in range(50)]
particles = []

def draw_world_grid(cam_x, cam_y):
    # Draw a grid that scrolls relative to the camera
    spacing = 100
    start_x = int(-cam_x % spacing)
    start_y = int(-cam_y % spacing)
    for x in range(start_x, WIDTH, spacing):
        pygame.draw.line(screen, (20, 25, 45), (x, 0), (x, HEIGHT), 1)
    for y in range(start_y, WIDTH, spacing):
        pygame.draw.line(screen, (20, 25, 45), (0, y), (WIDTH, y), 1)

def kill_player():
    global is_alive
    is_alive = False
    for _ in range(30): # Explosion particles
        particles.append([[world_x, world_y], [random.uniform(-10, 10), random.uniform(-10, 10)], 40])

# --- MAIN LOOP ---
while True:
    screen.fill(BG_COLOR)
    
    # Camera offset: This centers the snake head on the screen
    cam_x = world_x - WIDTH // 2
    cam_y = world_y - HEIGHT // 2

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit(); exit()
        if event.type == pygame.KEYDOWN and not is_alive:
            # Reset Game
            world_x, world_y = WORLD_SIZE // 2, WORLD_SIZE // 2
            path, snake_len, score, is_alive = [], 60, 0, True

    if is_alive:
        # 1. Controls & Speed
        keys = pygame.key.get_pressed()
        speed = base_speed * 2 if keys[pygame.K_SPACE] else base_speed
        if keys[pygame.K_LEFT]: angle -= 0.08
        if keys[pygame.K_RIGHT]: angle += 0.08

        # 2. Movement
        world_x += speed * math.cos(angle)
        world_y += speed * math.sin(angle)
        
        # World Boundaries
        if world_x < 0 or world_x > WORLD_SIZE or world_y < 0 or world_y > WORLD_SIZE:
            kill_player()

        path.append((world_x, world_y))
        if len(path) > snake_len: path.pop(0)

        # 3. Self-Collision (Skip the first 20 segments to avoid hitting your own neck)
        head_pos = (world_x, world_y)
        for i, segment in enumerate(path[:-25]):
            if math.hypot(head_pos[0] - segment[0], head_pos[1] - segment[1]) < 12:
                kill_player()

        # 4. Food Collection
        for f in foods[:]:
            if math.hypot(world_x - f[0], world_y - f[1]) < 30:
                score += 10
                snake_len += 15
                foods.remove(f)
                foods.append([random.randint(0, WORLD_SIZE), random.randint(0, WORLD_SIZE)])

    # --- DRAWING ---
    draw_world_grid(cam_x, cam_y)

    # Draw Food
    for f in foods:
        fx, fy = f[0] - cam_x, f[1] - cam_y
        if -50 < fx < WIDTH + 50 and -50 < fy < HEIGHT + 50:
            pygame.draw.circle(screen, FOOD_COLOR, (int(fx), int(fy)), 10)
            pygame.draw.circle(screen, (255, 255, 255), (int(fx), int(fy)), 4)

    # Draw Snake
    for i, p in enumerate(path[::4]):
        sx, sy = p[0] - cam_x, p[1] - cam_y
        size = 12 + math.sin(i * 0.3 + pygame.time.get_ticks() * 0.01) * 3
        # Outline/Glow
        pygame.draw.circle(screen, SNAKE_COLOR, (int(sx), int(sy)), int(size), 2)
        # Core
        color_val = min(255, 150 + i)
        pygame.draw.circle(screen, (0, color_val, 200), (int(sx), int(sy)), int(size - 4))

    # Particles
    for p in particles[:]:
        p[0][0] += p[1][0]; p[0][1] += p[1][1]; p[2] -= 1
        if p[2] <= 0: particles.remove(p)
        else: pygame.draw.circle(screen, SNAKE_COLOR, (int(p[0][0]-cam_x), int(p[0][1]-cam_y)), 4)

    # UI
    txt = font.render(f"SCORE: {score}   {'SPACE TO BOOST' if is_alive else 'GAME OVER - PRESS ANY KEY'}", True, (255, 255, 255))
    screen.blit(txt, (20, 20))

    pygame.display.flip()
    clock.tick(FPS)