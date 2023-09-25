# Imports
import pygame
import os

# Pygame intialization
pygame.init()

# Set the screen size
WIDTH, HEIGHT = 800, 500
pygame.display.set_mode((WIDTH, HEIGHT))

# Define the name of our game
pygame.display.set_caption("Hangman")

# Define the speed our game goes at
FPS = 60
clock = pygame.time.Clock()

# Variable condition for our while loop
run = True

# Game loop
while run:
    clock.tick(FPS)

    # Checking for events withing the game
    for event in pygame.event.get():
        