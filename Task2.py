
import pygame
import random
import sys

# --------------------------
# Initialize
# --------------------------
pygame.init()

WIDTH, HEIGHT = 600, 600
GRID_SIZE = 20
FPS = 10

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Game")

clock = pygame.time.Clock()

# Colors
BLACK = (25, 25, 25)
GREEN = (0, 220, 0)
RED = (255, 60, 60)
WHITE = (255, 255, 255)
GRAY = (70, 70, 70)

font = pygame.font.SysFont("Arial", 28)
big_font = pygame.font.SysFont("Arial", 50)

# --------------------------
# Functions
# --------------------------

def random_food():
    return (
        random.randrange(0, WIDTH, GRID_SIZE),
        random.randrange(0, HEIGHT, GRID_SIZE),
    )


def draw_text(text, font, color, x, y):
    img = font.render(text, True, color)
    screen.blit(img, (x, y))


def reset_game():
    global snake, direction, food, score, game_over, speed

    snake = [(300, 300)]
    direction = (0, 0)
    food = random_food()
    score = 0
    speed = 10
    game_over = False


# --------------------------
# Variables
# --------------------------

snake = [(300, 300)]
direction = (0, 0)
food = random_food()

score = 0
high_score = 0
speed = 10
game_over = False

# --------------------------
# Main Loop
# --------------------------

running = True

while running:

    # Events
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:

            if game_over:
                if event.key == pygame.K_r:
                    reset_game()

            else:
                if event.key in (pygame.K_UP, pygame.K_w):
                    if direction != (0, GRID_SIZE):
                        direction = (0, -GRID_SIZE)

                elif event.key in (pygame.K_DOWN, pygame.K_s):
                    if direction != (0, -GRID_SIZE):
                        direction = (0, GRID_SIZE)

                elif event.key in (pygame.K_LEFT, pygame.K_a):
                    if direction != (GRID_SIZE, 0):
                        direction = (-GRID_SIZE, 0)

                elif event.key in (pygame.K_RIGHT, pygame.K_d):
                    if direction != (-GRID_SIZE, 0):
                        direction = (GRID_SIZE, 0)

    if not game_over:

        if direction != (0, 0):

            head_x = snake[0][0] + direction[0]
            head_y = snake[0][1] + direction[1]

            new_head = (head_x, head_y)

            # Wall collision
            if (
                head_x < 0
                or head_x >= WIDTH
                or head_y < 0
                or head_y >= HEIGHT
            ):
                game_over = True

            # Self collision
            elif new_head in snake:
                game_over = True

            else:
                snake.insert(0, new_head)

                # Food collision
                if new_head == food:

                    score += 10

                    if score > high_score:
                        high_score = score

                    speed = min(25, speed + 0.5)

                    while True:
                        food = random_food()
                        if food not in snake:
                            break

                else:
                    snake.pop()

    # Draw
    screen.fill(BLACK)

    # Food
    pygame.draw.rect(
        screen,
        RED,
        (food[0], food[1], GRID_SIZE, GRID_SIZE),
        border_radius=5,
    )

    # Snake
    for i, segment in enumerate(snake):
        color = WHITE if i == 0 else GREEN
        pygame.draw.rect(
            screen,
            color,
            (segment[0], segment[1], GRID_SIZE, GRID_SIZE),
            border_radius=4,
        )

    # Score
    draw_text(f"Score: {score}", font, WHITE, 10, 10)
    draw_text(f"High Score: {high_score}", font, WHITE, 350, 10)

    # Game Over
    if game_over:
        draw_text(
            "GAME OVER",
            big_font,
            RED,
            WIDTH // 2 - 150,
            HEIGHT // 2 - 60,
        )

        draw_text(
            "Press R to Restart",
            font,
            WHITE,
            WIDTH // 2 - 120,
            HEIGHT // 2 + 10,
        )

    pygame.display.flip()

    clock.tick(speed)

pygame.quit()
sys.exit()
