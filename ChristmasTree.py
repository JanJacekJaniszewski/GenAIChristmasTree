import pygame
import random

# Initialize Pygame
pygame.init()

# Set the screen size
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))

# Set the background color
background_color = (0, 0, 0)
screen.fill(background_color)

# Define the Christmas tree parameters
tree_color = (0, 128, 0)
tree_x = screen_width // 2
tree_y = screen_height - 50
tree_height = 300
tree_width = 150

# Draw the Christmas tree triangles
for i in range(5):
    triangle_height = tree_height // 5
    triangle_width = tree_width + (i * 30)
    triangle_x = tree_x - (triangle_width // 2) + (tree_width // 2)
    triangle_y = tree_y - tree_height + (i * triangle_height)
    pygame.draw.polygon(screen, tree_color, [(triangle_x, triangle_y), (triangle_x + triangle_width, triangle_y),
                                             (triangle_x + (triangle_width // 2), triangle_y - triangle_height)])

# Draw some ornaments
ornament_colors = [(255, 0, 0), (0, 0, 255), (255, 255, 0)]
ornament_radius = 15
ornament_positions = []
for i in range(3):
    ornament_x = random.randint(tree_x - (tree_width // 2), tree_x + (tree_width // 2))
    ornament_y = random.randint(tree_y - tree_height + ornament_radius, tree_y - ornament_radius)
    pygame.draw.circle(screen, ornament_colors[i], (ornament_x, ornament_y), ornament_radius)

# Draw a star on top of the tree
star_color = (255, 255, 0)
star_x = tree_x
star_y = tree_y - tree_height + 20
star_radius = 30
pygame.draw.polygon(screen, star_color, [(star_x, star_y - star_radius), (star_x + star_radius / 4, star_y - star_radius / 4),
                                          (star_x + star_radius, star_y), (star_x + star_radius / 4, star_y + star_radius / 4),
                                          (star_x, star_y + star_radius), (star_x - star_radius / 4, star_y + star_radius / 4),
                                          (star_x - star_radius, star_y), (star_x - star_radius / 4, star_y - star_radius / 4)])

# Draw some snowflakes
snowflake_color = (255, 255, 255)
snowflake_radius = 5
for i in range(200):
    snowflake_x = random.randint(0, screen_width)
    snowflake_y = random.randint(0, screen_height)
    pygame.draw.circle(screen, snowflake_color, (snowflake_x, snowflake_y), snowflake_radius)

# Update the display
pygame.display.update()

# Wait for the user to close the window
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

# Quit Pygame
pygame.quit()
