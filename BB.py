import pygame
import sys

# Initialize Pygame
pygame.init()

# Define screen size and create the display window
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Stick Figure Cartoon - Two Dogs and a Little Girl")

# Set clock for controlling frame rate
clock = pygame.time.Clock()

# Define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
BROWN = (139, 69, 19)
GRAY = (128, 128, 128)


# Dog class (simple stick figure dog)
class Dog:
    def __init__(self, x, y, color=BROWN):
        self.x = x
        self.y = y
        self.color = color
        self.size = 50  # Base size for body parts

    def draw(self, surface):
        # Body
        pygame.draw.circle(surface, self.color, (self.x, self.y), 20)

        # Head
        pygame.draw.circle(surface, self.color, (self.x, self.y - 30), 15)

        # Legs
        pygame.draw.line(surface, self.color, (self.x - 10, self.y + 20), (self.x - 20, self.y + 40), 4)
        pygame.draw.line(surface, self.color, (self.x + 10, self.y + 20), (self.x + 20, self.y + 40), 4)

        # Tail
        pygame.draw.line(surface, self.color, (self.x - 20, self.y), (self.x - 30, self.y - 10), 4)

    def move(self, dx, dy):
        self.x += dx
        self.y += dy


# Girl class (stick figure girl)
class Girl:
    def __init__(self, x, y, color=RED):
        self.x = x
        self.y = y
        self.color = color

    def draw(self, surface):
        # Head
        pygame.draw.circle(surface, self.color, (self.x, self.y), 20)

        # Body
        pygame.draw.line(surface, self.color, (self.x, self.y + 20), (self.x, self.y + 80), 5)

        # Arms
        pygame.draw.line(surface, self.color, (self.x - 30, self.y + 40), (self.x + 30, self.y + 40), 5)

        # Legs
        pygame.draw.line(surface, self.color, (self.x, self.y + 80), (self.x - 20, self.y + 120), 5)
        pygame.draw.line(surface, self.color, (self.x, self.y + 80), (self.x + 20, self.y + 120), 5)

    def move(self, dx, dy):
        self.x += dx
        self.y += dy


# Create two dogs and a girl
dog1 = Dog(100, 400, BROWN)
dog2 = Dog(200, 400, GRAY)
girl = Girl(400, 400, RED)

# Main animation loop
while True:
    screen.fill(WHITE)  # Clear screen with white background

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Move characters for simple animation
    dog1.move(1, 0)  # Dog 1 moves right
    dog2.move(-1, 0)  # Dog 2 moves left
    girl.move(0, -1)  # Girl moves upward

    # Wrap movement if going off-screen
    if dog1.x > width: dog1.x = -50
    if dog2.x < -50: dog2.x = width
    if girl.y < 0: girl.y = height

    # Draw the characters
    dog1.draw(screen)
    dog2.draw(screen)
    girl.draw(screen)

    # Update the display
    pygame.display.flip()

    # Control frame rate (30 frames per second)
    clock.tick(30)
