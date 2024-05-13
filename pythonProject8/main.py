import pygame
import time
import random

pygame.init()

# Initialize display
display_width = 800
display_height = 600
display = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption('Snake Game')

# Define colors (R, G, B)
black = (0,0,0)
white = (255,255,255)
red = (255,0,0)
green = (0,255,0)

# Define snake properties
snake_block = 10
snake_speed = 30

# Define font and size
font_style = pygame.font.SysFont(None, 50)
score_font = pygame.font.SysFont(None, 35)

def our_snake(snake_block, snake_list):
    for x in snake_list:
        pygame.draw.rect(display, green, [x[0], x[1], snake_block, snake_block])

def message(msg, color):
    mesg = font_style.render(msg, True, color)
    display.blit(mesg, [display_width/6, display_height/3])

# Game loop
def gameLoop():
    game_over = False
    game_close = False