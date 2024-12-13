import pygame
import random

# Initialize the game
pygame.init()

# Set the screen dimensions
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Snake Game")

# Set the colors
black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
green = (0, 255, 0)

# Set the snake properties
snake_block_size = 20
snake_speed = 10

# Define the snake
def draw_snake(snake_block_size, snake_list):
    for x in snake_list:
        pygame.draw.rect(screen, black, [x[0], x[1], snake_block_size, snake_block_size])

# Display message
def message(msg, color, y_offset=0):
    font_style = pygame.font.SysFont("bahnschrift", 30)
    mesg = font_style.render(msg, True, color)
    screen.blit(mesg, [screen_width / 6, screen_height / 3 + y_offset])

# Run the game
def game_loop():
    game_over = False
    game_close = False

    x1 = screen_width // 2
    y1 = screen_height // 2

    x1_change = 0
    y1_change = 0

    snake_list = []
    length_of_snake = 1
    global snake_speed

    foodx = round(random.randrange(0, screen_width - snake_block_size) / 20.0) * 20.0
    foody = round(random.randrange(0, screen_height - snake_block_size) / 20.0) * 20.0

    clock = pygame.time.Clock()

    while not game_over:

        while game_close:
            screen.fill(white)
            message("Game Over! Press Q-Quit or C-Play Again", red)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        return  # Restart the game loop

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT and x1_change == 0:
                    x1_change = -snake_block_size
                    y1_change = 0
                elif event.key == pygame.K_RIGHT and x1_change == 0:
                    x1_change = snake_block_size
                    y1_change = 0
                elif event.key == pygame.K_UP and y1_change == 0:
                    y1_change = -snake_block_size
                    x1_change = 0
                elif event.key == pygame.K_DOWN and y1_change == 0:
                    y1_change = snake_block_size
                    x1_change = 0

        if x1 >= screen_width or x1 < 0 or y1 >= screen_height or y1 < 0:
            game_close = True

        x1 += x1_change
        y1 += y1_change
        screen.fill(white)
        pygame.draw.rect(screen, red, [foodx, foody, snake_block_size, snake_block_size])

        snake_head = [x1, y1]
        snake_list.append(snake_head)
        if len(snake_list) > length_of_snake:
            del snake_list[0]

        for x in snake_list[:-1]:
            if x == snake_head:
                game_close = True

        draw_snake(snake_block_size, snake_list)
        pygame.display.update()

        if x1 == foodx and y1 == foody:
            foodx = round(random.randrange(0, screen_width - snake_block_size) / 20.0) * 20.0
            foody = round(random.randrange(0, screen_height - snake_block_size) / 20.0) * 20.0
            length_of_snake += 1
            snake_speed += 1  # Increase speed

        clock.tick(snake_speed)

    pygame.quit()

# Run the game loop
game_loop()
