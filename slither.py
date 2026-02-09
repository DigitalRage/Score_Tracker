import pygame
import sys
import random
import math
player_size = 16
player_color = (200, 40, 40)
speed = 6


def run_game(width: int = 800, height: int = 600, title: str = "Slither - Simple Move") -> None:
	pygame.init()
	screen = pygame.display.set_mode((width, height))
	pygame.display.set_caption(title)
	clock = pygame.time.Clock()
	max_trail_length = 100
	trail_positions = []
	player_x = width // 2 - player_size // 2
	player_y = height // 2 - player_size // 2

	
	dot_radius = 6
	dot_color = (240, 200, 40)
	dots = []

	def spawn_dot():
		"""Spawn a dot at a random position not too close to the player."""
		margin = 20
		while True:
			x = random.randint(margin + dot_radius, width - margin - dot_radius)
			y = random.randint(margin + dot_radius, height - margin - dot_radius)
			
			px = player_x + player_size // 2
			py = player_y + player_size // 2
			if math.hypot(px - x, py - y) > player_size + dot_radius + 10:
				return (x, y)

	
	for _ in range(8):
		dots.append(spawn_dot())

	running = True
	while running:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				running = False
			elif event.type == pygame.KEYDOWN:
				if event.key == pygame.K_ESCAPE:
					running = False

		keys = pygame.key.get_pressed()
		dx = dy = 0
		if keys[pygame.K_LEFT] or keys[pygame.K_a]:
			dx -= speed
		if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
			dx += speed
		if keys[pygame.K_UP] or keys[pygame.K_w]:
			dy -= speed
		if keys[pygame.K_DOWN] or keys[pygame.K_s]:
			dy += speed

		player_x = max(0, min(width - player_size, player_x + dx))
		player_y = max(0, min(height - player_size, player_y + dy))

		
		head_pos = (player_x + player_size // 2, player_y + player_size // 2)
		trail_positions.append(head_pos)
		if len(trail_positions) > max_trail_length:
			trail_positions.pop(0)

		
		eaten = []
		for i, (dx_pos, dy_pos) in enumerate(dots):
			if math.hypot(head_pos[0] - dx_pos, head_pos[1] - dy_pos) <= (player_size // 2 + dot_radius):
				eaten.append(i)

		
		for idx in sorted(eaten, reverse=True):
		
			add_len = random.randint(3, 8)
			max_trail_length += add_len
			
			dots.pop(idx)
			dots.append(spawn_dot())

	
		screen.fill((30, 30, 30))

	
		for pos in trail_positions:
			
			trail_size = 6
			pygame.draw.rect(screen, player_color, (pos[0] - trail_size // 2, pos[1] - trail_size // 2, trail_size, trail_size))

		
		for (x, y) in dots:
			pygame.draw.circle(screen, dot_color, (x, y), dot_radius)

		
		pygame.draw.rect(screen, player_color, (player_x, player_y, player_size, player_size))

		
		font = pygame.font.SysFont(None, 24)
		txt = font.render(f"Trail: {len(trail_positions)}/{max_trail_length}", True, (200, 200, 200))
		screen.blit(txt, (8, 8))

		pygame.display.flip()
		clock.tick(60)



run_game()

