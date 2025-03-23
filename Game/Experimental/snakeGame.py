import pygame
import time
import random

# Initialize pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 600, 400

#Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

#Initialize game screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Game")

#Clock for controlling the frame rate
clock = pygame.time.Clock()

#Snake block size
BLOCK_SIZE = 10

#Font for text
def get_font(size):
    return pygame.font.SysFont("bahnschrift", size)

class SnakeGame:
    def __init__(self):
        self.snake_pos = [100, 50]
        self.snake_body = [[100, 50], [90, 50], [80, 50]]
        self.food_pos = [random.randrange(1, WIDTH // BLOCK_SIZE) 
                         * BLOCK_SIZE, random.randrange(1, HEIGHT 
                        // BLOCK_SIZE) * BLOCK_SIZE]
        self.food_spawn = True
        self.direction = "RIGHT"
        self.change_to = self.direction
        self.score = 0

    def move(self):
        if self.change_to == 'UP' and not self.direction == 'DOWN':
            self.direction = 'UP'
        if self.change_to == 'DOWN' and not self.direction == 'UP':
            self.direction = 'DOWN'
        if self.change_to == 'LEFT' and not self.direction == 'RIGHT':
            self.direction = 'LEFT'
        if self.change_to == 'RIGHT' and not self.direction == 'LEFT':
            self.direction = 'RIGHT'
        if self.direction == 'UP':
            self.snake_pos[1] -= BLOCK_SIZE
        if self.direction == 'DOWN':
            self.snake_pos[1] += BLOCK_SIZE
        if self.direction == 'LEFT':
            self.snake_pos[0] -= BLOCK_SIZE
        if self.direction == 'RIGHT':
            self.snake_pos[0] += BLOCK_SIZE

    def check_collision(self):
        #Check if snake collided with the boundries
        if (self.snake_pos[0] < 0 or self.snake_pos[0] >= WIDTH or
            self.snake_pos[1] < 0 or self.snake_pos[1] >= HEIGHT):
            return True
        
        #Check if the snake has collided with itself
        for block in self.snake_body[1:]:
            if self.snake_pos == block:
                return True

        return False
    
    def spawn_food(self):
        if not self.food_spawn:
            self.food_pos = [random.randrange(1, WIDTH // BLOCK_SIZE) * BLOCK_SIZE,
                             random.randrange(1, HEIGHT // BLOCK_SIZE) * BLOCK_SIZE]
        self.food_spawn = True

    def grow_snake(self):
        self.snake_body.insert(0, list(self.snake_pos))

        if self.snake_pos == self.food_pos:
            self.score += 10
            self.food_spawn = False
        else:
            self.snake_body.pop()

    def display_snake(self):
        for block in self.snake_body:
            pygame.draw.rect(screen, GREEN, pygame.Rect(block[0], block[1], BLOCK_SIZE, BLOCK_SIZE))

    def display_food(self):
        pygame.draw.rect(screen, RED, pygame.Rect(self.food_pos[0], self.food_pos[1], BLOCK_SIZE, BLOCK_SIZE))

    def show_score(self):
        font = get_font(20)
        score_surface = font.render(f"Score: {self.score}", True, WHITE)
        screen.blit(score_surface, [10, 10])

#Main function
def game_loop():
    game = SnakeGame()
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    game.change_to = 'UP'
                if event.key == pygame.K_DOWN:
                    game.change_to = 'DOWN'
                if event.key == pygame.K_LEFT:
                    game.change_to = 'LEFT'
                if event.key == pygame.K_RIGHT:
                    game.change_to = 'RIGHT'

        game.move()

        if game.check_collision():
            running = False

        game.spawn_food()
        game.grow_snake()

        screen.fill(BLACK)
        game.display_snake()
        game.display_food()
        game.show_score()

        pygame.display.flip()

        clock.tick(15)
    
    time.sleep(1)
    pygame.quit()

    #Run the game
    game_loop()
