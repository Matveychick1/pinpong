import pygame as pg
from pygame import *
pg.init()
font.init()
fps = 60
fpsClock = pg.time.Clock()
run = True
width, height = 800,800
screen = pg.display.set_mode((width, height))
background = pg.transform.scale(pg.image.load("timeout.jpg"), (width, height))

fontdlyalohov = font.Font(None,50)
count = fontdlyalohov.render("",True,(225,200,50))
#класс-родитель для других спрайтов
class GameSprite(pg.sprite.Sprite):
    def __init__(self, image, x, y, size_x, size_y, speed):
        #Вызываем конструктор класса (Sprite):
        pg.sprite.Sprite.__init__(self)
 
        #каждый спрайт должен хранить свойство image - изображение
        self.image = pg.transform.scale(pg.image.load(image), (size_x, size_y))
        self.speed = speed
        self.speed_x = speed
        self.speed_y = speed
        
 
        #каждый спрайт должен хранить свойство rect - прямоугольник, в который он вписан
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        #self.rect.x = player
 
    def draw(self, scr):
        scr.blit(self.image, (self.rect.x, self.rect.y))
class Player(GameSprite):
    def control_l(self):
        keys_pressed = pg.key.get_pressed()
        if keys_pressed[pg.K_w] and self.rect.y >= 0:
            self.rect.y -= self.speed
        if keys_pressed[pg.K_s] and self.rect.y <= 500:
            self.rect.y += self.speed
    def control_r(self):
        keys_pressed = pg.key.get_pressed()
        if keys_pressed[pg.K_UP] and self.rect.y >= 0:
            self.rect.y -= self.speed
        if keys_pressed[pg.K_DOWN] and self.rect.y <= 500:
            self.rect.y += self.speed

class Ball(GameSprite):
    def update(self):
        global pause, count
        self.rect.x += self.speed_x
        self.rect.y += self.speed_y
        if self.rect.x < 0 or self.rect.x > width - 50:
            if self.rect.x < 0:
                count = fontdlyalohov.render("второй выиграл",True,(225,200,50))
            if self.rect.x > width - 50:
                count = fontdlyalohov.render("первый выиграл",True,(225,200,50))
            pause = True
            self.speed_x *= -1
        if self.rect.y < 0 or self.rect.y > height - 50:
            self.speed_y *= -1
 
t1 = Player('11.png', 100, 300, 100, 300, 5)
t2 = Player('12.png', 600, 300, 100, 300, 5)

ball = Ball('aaa.png', 300, 300, 50, 50, 5)
pause = False

while run:
    screen.fill((0, 0, 0))
    screen.blit(background,(0,0))
    for event in pg.event.get():
        if event.type == pg.QUIT:
            run = False
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_SPACE:
                pause = not pause
    screen.blit(count,(200,20))
    if not pause:
        if pg.sprite.collide_rect(t1,ball) or pg.sprite.collide_rect(t2,ball):
            ball.speed_x *= -1

        t1.draw(screen)
        t2.draw(screen)
        t1.control_l()
        t2.control_r()
        
        
        ball.update()
        ball.draw(screen)
    
    pg.display.flip()
    fpsClock.tick(fps)



 