import pygame
import random
import csv
import math
import time
import matplotlib.pyplot as plt

# define polygon class
class Polygon:
    def __init__(self, points, color):
        self.points = [tuple(point) for point in points] #
        self.color = color
        self.center = self.calculate_center()
        self.velocity = [random.randint(-100, 100) / 100, random.randint(-100, 100) / 100]
        self.rect = pygame.Rect(*self.points[0], 0, 0).unionall([pygame.Rect(*p, 0, 0) for p in self.points])
    def calculate_center(self):
        x_coords = [point[0] for point in self.points]
        y_coords = [point[1] for point in self.points]
        center_x = sum(x_coords) / len(self.points)
        center_y = sum(y_coords) / len(self.points)
        return (center_x, center_y)

    def move(self):
       
        pass    

    def draw(self, screen):
        pygame.draw.polygon(screen, self.color, self.points)
        
"""def midpoint_displacement(points, displace):
    new_points = [points[0]]
    for i in range(len(points)-1):
        x1, y1 = points[i]
        x2, y2 = points[i+1]
        mid_x = (x1 + x2) // 2
        mid_y = (y1 + y2) // 2 + random.randint(-displace, displace)
        new_points.append((mid_x, mid_y))
        new_points.append(points[i+1])
    return new_points  """      

# read in polygons from CSV file
polygons = {}
with open('polygon_coordinates.csv', mode='r') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    for row in csv_reader:
        if row['polygon'] not in polygons:
            polygons[row['polygon']] = []
        polygons[row['polygon']].append((int(float(row['x'])), int(float(row['y']))))

# create Polygon objects
polygons_list = []
for polygon in polygons.values():
    polygons_list.append(Polygon(polygon, (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))))
# Initialize Pygame
pygame.init()

# Define screen dimensions
WIDTH = 1100
HEIGHT = 700
screen = pygame.display.set_mode((WIDTH,HEIGHT))

background_image = pygame.image.load("C:/Pygame/background.jpg").convert()
background_image = pygame.transform.scale(background_image, (WIDTH, HEIGHT))



# Define colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)

# Define circle dimensions and positions
CIRCLE_RADIUS = 60
CIRCLE_X1 = 300
CIRCLE_Y1 = 200
CIRCLE_X2 = 700
CIRCLE_Y2 = 200
CIRCLE_X3 = 300
CIRCLE_Y3 = 400
CIRCLE_X4 = 550
CIRCLE_Y4 = 350


# Define enemy dimensions
ENEMY_SIZE = 5

# set up clock
clock = pygame.time.Clock()
average_velocity = [sum(polygon.velocity[0] for polygon in polygons_list) / len(polygons_list),
                    sum(polygon.velocity[1] for polygon in polygons_list) / len(polygons_list)]

# Define screen surface
#screen = pygame.display.set_mode((WIDTH, HEIGHT))

# Define fractal algorithm function
def generate_fractal_points(start_x, start_y, end_x, end_y, depth, displace):
    points = []
    if depth == 0:
        return [(start_x, start_y)]
    else:
        mid_x = (start_x + end_x) // 2
        mid_y = (start_y + end_y) // 2

        cx = (start_x + end_x) / 2
        cy = (start_y + end_y) / 2

        for x in range(start_x, end_x + 1, displace):
            for y in range(start_y, end_y + 1, displace):
                zx = zy = 0
                c = complex((x - cx) / (end_x - cx), (y - cy) / (end_y - cy))

                for i in range(depth):
                    if abs(zx + zy) > 2.0:
                        break
                    zx, zy = zx * zx - zy * zy + c.real, 2 * zx * zy + c.imag

                if i == depth - 1:
                    points.append((x, y))

        points += generate_fractal_points(start_x, start_y, mid_x, mid_y, depth - 1, displace)
        points += generate_fractal_points(mid_x, start_y, end_x, mid_y, depth - 1, displace)
        points += generate_fractal_points(start_x, mid_y, mid_x, end_y, depth - 1, displace)
        points += generate_fractal_points(mid_x, mid_y, end_x, end_y, depth - 1, displace)

    return points



# Generate enemy movement using fractal algorithm
fractal_depth = 5
displace = 200

enemy_points = generate_fractal_points(0, 0, WIDTH - ENEMY_SIZE, HEIGHT - ENEMY_SIZE, fractal_depth, displace)
current_point_index = 0
target_x, target_y = enemy_points[current_point_index]
enemy_x, enemy_y = target_x, target_y

# Initialize CSV file
"""with open('withoutloop.csv', mode='w+', newline='') as csvfile:
    fieldnames = ['x_axis', 'y_axis']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()"""

# Define the main game loop
running = True
enemy_positions_x = []
enemy_positions_y = []
prev_positions = []  # Keep track of previous positions of enemy
reverse_direction=False
speed = 12  # Set speed of enemy movement
last_update_time = time.time()  # Store the timestamp of the last CSV update
update_interval = 2  # Update the CSV every 2 seconds
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    dx = target_x - enemy_x
    dy = target_y - enemy_y
    dist = (dx ** 2 + dy ** 2) ** 0.5
    if dist < speed:
        # Enemy has reached the target position, move to the next target position
        current_point_index = (current_point_index + 1) % len(enemy_points)
        target_x, target_y = enemy_points[current_point_index]
        #prev_positions.append((enemy_x, enemy_y))
    else:
        # Move the enemy towards the target position
        enemy_x += int(speed * dx / dist)
        enemy_y += int(speed * dy / dist)
     # Store the enemy positions
    enemy_positions_x.append(enemy_x)
    enemy_positions_y.append(enemy_y)    
     # Check if the enemy collides with any polygon
    enemy_rect = pygame.Rect(enemy_x, enemy_y, ENEMY_SIZE, ENEMY_SIZE)
    for polygon in polygons_list:
        if enemy_rect.colliderect(polygon.rect):
            # Collision detected, reverse the enemy's direction
            dx = enemy_x - polygon.center[0]
            dy = enemy_y - polygon.center[1]
            dist = (dx ** 2 + dy ** 2) ** 0.5
            
            # Calculate the new target position away from the polygon
            target_x = enemy_x + int(dx / dist * ENEMY_SIZE)
            target_y = enemy_y + int(dy / dist * ENEMY_SIZE)
            
            # Update the enemy's position away from the polygon
            enemy_x = target_x
            enemy_y = target_y   
    # Draw the circles and the enemy
    screen.blit(background_image, (0,0))
    
    
    pygame.draw.circle(screen, BLACK, (CIRCLE_X1, CIRCLE_Y1), CIRCLE_RADIUS)
    pygame.draw.circle(screen, BLACK, (CIRCLE_X2, CIRCLE_Y2), 110)
    pygame.draw.circle(screen, BLACK, (CIRCLE_X3, CIRCLE_Y3), 90)
    pygame.draw.circle(screen, BLACK, (CIRCLE_X4, CIRCLE_Y4), 80)
    pygame.draw.rect(screen, RED, (enemy_x, enemy_y, ENEMY_SIZE, ENEMY_SIZE))
       
    

    with open('path.csv', mode='a', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow([enemy_x, enemy_y])
    
    
    # Check if the enemy is inside any of the circles
   # current_time = time.time()
    #if current_time - last_update_time >= update_interval:
        # Check if the enemy is inside any of the circles
    if ((enemy_x - CIRCLE_X1)**2 + (enemy_y - CIRCLE_Y1)**2) <= CIRCLE_RADIUS**2:
        with open('withoutloop.csv', mode='a', newline='') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow([enemy_x, enemy_y])
    elif ((enemy_x - CIRCLE_X2)**2 + (enemy_y - CIRCLE_Y2)**2) <= CIRCLE_RADIUS**2:
        with open('withoutloop.csv', mode='a', newline='') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow([enemy_x, enemy_y])
    elif ((enemy_x - CIRCLE_X3)**2 + (enemy_y - CIRCLE_Y3)**2) <= CIRCLE_RADIUS**2:
        with open('withoutloop.csv', mode='a', newline='') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow([enemy_x, enemy_y])
    elif ((enemy_x - CIRCLE_X4)**2 + (enemy_y - CIRCLE_Y4)**2) <= CIRCLE_RADIUS**2:
        with open('withoutloop.csv', mode='a', newline='') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow([enemy_x, enemy_y])
        
        # Update the last CSV update time
        #last_update_time = current_time

  
    for polygon in polygons_list:
        pygame.draw.polygon(screen, polygon.color, polygon.points)

    # Update the screen
    pygame.display.flip()
    
    # Set the game clock speed
    clock.tick(60)
plt.plot(enemy_positions_x, enemy_positions_y,color='blue',linewidth = 3, label = 'line1-dotted',linestyle='dotted')
plt.xlabel('X Position')
plt.ylabel('Y Position')
plt.title('Enemy Movement')
plt.grid(True)
plt.show()





