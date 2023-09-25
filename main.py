# Imports
import pygame

# SETUP DISPLAY
# Pygame intialization
pygame.init()
WIDTH, HEIGHT = 800, 500
win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Hangman")

# Button variables
RADIUS = 20
GAP = 15
letters = []
startx = round((WIDTH - (RADIUS * 2 + GAP) * 13) / 2)
starty = 400

for i in range(26):
    x = startx + GAP * 2 + ((RADIUS * 2 + GAP) * (i % 13))
    y = starty + ((i // 13) * (GAP + RADIUS * 2))
    letters.append([x, y])


# LOAD IMAGES
images = []
for i in range(7):
    image = pygame.image.load("hangman" + str(i) + ".png")
    images.append(image)
# print(images)

# Game variables
hangman_status = 0

# COLORS
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# SETUP GAME LOOP
# Define the speed our game goes at
FPS = 60
clock = pygame.time.Clock()

# Variable condition for our while loop
run = True

# Draw function
def draw():
    win.fill(WHITE)

    # Draw buttons
    for letter in letters:
        x, y = letter
        pygame.draw.circle(win, BLACK, (x, y), RADIUS, 3)

    win.blit(images[hangman_status], (150, 100))
    pygame.display.update()


# Game loop
while run:
    clock.tick(FPS)

    draw()

    # Checking for events withing the game
    for event in pygame.event.get():
        # If the x is clicked to close the game window
        if event.type == pygame.QUIT:
            run = False
        # Mouse click
        if event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            print(pos)


# Close the window
pygame.quit()