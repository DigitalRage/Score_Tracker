


game_map=[["e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e"],
["e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e"],
["e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e"],
["e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e"],
["e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e"],
["e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e"],
["e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e"],
["e","e","e","e","e","e","e","e","e","e","H","e","e","e","e","e","e","e","e","e"],
["e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e"],
["e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e"],
["e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e"],
["e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e"],
["e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e"],
["e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e"]]

class snake:
    def __init__(self,biggness):
        self.biggness=biggness
    def get_location_of_head(self):
        return get_locations("H")
    
direction="l"
import pygame
def get_locations(item):
    global game_map
    locations=[]
    for numx,x in enumerate(game_map):
        for numy,y in enumerate(x):
            if y==item:
                locations.append((xnum,ynum))
    return locations
def up():
    global direction
    if direction!="d":
        direction="u"
def down():
    global direction
    if direction!="u":
        direction="d"
def left():
    global direction
    if direction!="r":
        direction="l"
def right():
    global direction
    if direction!="l":
        direction="r"

def liam_game():
    pygame.init()

    screen = pygame.display.set_mode((1280,720))

    clock = pygame.time.Clock()

    while True:
        # Process player inputs.
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return finish
        mouse=pygame.mouse.get_pos()
        key=pygame.key.get_pressed()
        if key[pygame.K_w]:
            up()
        elif key[pygame.K_a]:
            left()
        elif key[pygame.K_s]:
            down()
        elif key[pygame.K_d]:
            right()
        # Do logical updates here.
        

        screen.fill("purple")  # Fill the display with a solid color

        # Render the graphics here.
        # ...

        pygame.display.flip()  # Refresh on-screen display
        clock.tick(60)         # wait until next frame (at 60 FPS)