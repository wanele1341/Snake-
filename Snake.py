import pygame
import sys
import random

SW , SH = 1250, 700
Block_Size = 50
screen = pygame.display.set_mode((SW , SH))
pygame.display.set_caption("SNAKE.IO")
clock = pygame.time.Clock()

class Snake():
    def __init__(self):
        self.x , self.y = Block_Size ,Block_Size
        self.xdir = 1
        self.ydir = 0
        self.head = pygame.Rect(self.x , self.y , Block_Size, Block_Size)
        self.body = [pygame.Rect(self.x - Block_Size , self.y , Block_Size, Block_Size)]
        self.dead  = False

    def update(self):
        snake.body.append(snake.head)
        for i in range(len(snake.body) -1):
            snake.body[i].x , snake.body[i].y = snake.body[i+1].x ,snake.body[i+1].y
        snake.head.x += self.xdir * Block_Size
        snake.head.y += self.ydir * Block_Size
        snake.body.remove(snake.head)

class Apple():
    def __init__(self):
        self.x = int(random.randint (0, SW)/ Block_Size) * Block_Size
        self.y = int(random.randint (0 , SH)/ Block_Size) * Block_Size
        self.rect = pygame.Rect( self.x , self.y , Block_Size, Block_Size)

    def update(self):
        pygame.draw.rect( screen , (255 , 0 ,  0) , self.rect)

def drawGrid():
    for x in range (0 , SW , Block_Size):
        for y in range (0 , SH , Block_Size):
            rect =  pygame.Rect(x , y , Block_Size , Block_Size)
            pygame.draw.rect(screen , (100 , 100 , 100) , rect , 1)

drawGrid()

snake = Snake()
apple = Apple()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN:
                snake.ydir = 1
                snake.xdir = 0
            elif event.key == pygame.K_UP:
                snake.ydir = -1
                snake.xdir = 0
            elif event.key == pygame.K_RIGHT:
                snake.ydir = 0
                snake.xdir = 1
            elif event.key == pygame.K_LEFT:
                snake.ydir = 0
                snake.xdir = -1
        drawGrid()           
        snake.update()
        screen.fill('black')
        drawGrid()

        apple.update()

        pygame.draw.rect(screen , (255 ,0 ,0) , snake.head)
        
        for square in snake.body:
            pygame.draw.rect(screen , (255 ,0 ,0) , square)

        if apple.x == snake.head.x and snake.head.y == apple.y:
            snake.body.append(pygame.Rect(snake.head.x , snake.head.y , Block_Size, Block_Size))
            apple = Apple()

        pygame.display.update()
        clock.tick(10)

pygame.quit()
