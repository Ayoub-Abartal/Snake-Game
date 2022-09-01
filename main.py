import pygame , sys
from pygame.math import Vector2
import random

class Fruit(object):

    def __init__(self):
       self.randomize()

    #draw fruit
    def draw_fruit(self):
        #create rect
        fruit_rect = pygame.Rect(int(self.pos.x * cell_size), int(self.pos.y *  cell_size), cell_size,cell_size)
        #draw rect
        pygame.draw.rect(screen,(140,0,0),fruit_rect)

    def randomize(self):
        # create x and y position
        self.x = random.randint(0, cell_number - 1)
        self.y = random.randint(0, cell_number - 1)
        self.pos = Vector2(self.x, self.y)

class Snake(object):
    def __init__(self):
        #contains all the blocks that a snake have
        self.body = [Vector2(5,10),Vector2(4,10),Vector2(3,10)]
        self.direction = Vector2(1,0)
        self.new_block = False

    def draw_snake(self):
        for block in self.body:
            #create rect
            snake_rect = pygame.Rect(int(block.x * cell_size), int(block.y * cell_size), cell_size,cell_size)
            #draw rect
            pygame.draw.rect(screen, (0,0,150),snake_rect)

    def move_snake(self):
        if self.new_block == True:
            body_copy = self.body[:]
            body_copy.insert(0, body_copy[0] + self.direction)
            self.body = body_copy[:]
            self.new_block = False
        # copy the entire list except the last element
        else:
            body_copy = self.body[:-1]
            body_copy.insert(0, body_copy[0] + self.direction)
            self.body = body_copy[:]


    def addBlock(self):
        self.new_block = True

class Main(object):
    def __init__(self):
        self.snake = Snake()
        self.fruit = Fruit()

    def update(self):
        self.snake.move_snake()
        self.check_collision()
        self.check_fail()

    def drawElement(self):
        self.fruit.draw_fruit()
        self.snake.draw_snake()

    def check_collision(self):
        if self.fruit.pos == self.snake.body[0]:
            self.fruit.randomize()
            #adding a block to the snake
            self.snake.addBlock()

    def check_fail(self):
        #check if snake outside of the screen
        if not 0 <= self.snake.body[0].x < cell_number or not 0 <= self.snake.body[0].y < cell_number:
            self.game_over()
        #check if the screen hits itself
        for block in self.snake.body[1:]:
            if block == self.snake.body[0]:
                self.game_over()

    def game_over(self):
        pygame.quit()
        sys.exit()

#Game Variables
cell_size = 40
cell_number = 20

pygame.init()
screen = pygame.display.set_mode((cell_size*cell_number, cell_size*cell_number))
clock = pygame.time.Clock()


#
mainGame = Main()
SCREEN_UPDATE = pygame.USEREVENT
pygame.time.set_timer(SCREEN_UPDATE,150)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == SCREEN_UPDATE:
            mainGame.update()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                mainGame.snake.direction = Vector2(0,-1)
            if event.key == pygame.K_DOWN:
                mainGame.snake.direction = Vector2(0,1)
            if event.key == pygame.K_RIGHT:
                mainGame.snake.direction = Vector2(1,0)
            if event.key == pygame.K_LEFT:
                mainGame.snake.direction = Vector2(-1,0)

    screen.fill((175,215,70))
    mainGame.drawElement()
    pygame.display.update()
    clock.tick(60)