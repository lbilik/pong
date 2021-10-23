import pygame
pygame.init()
from random import uniform
#123
#123

mw_w = 500
mw_h = 500

mw = pygame.display.set_mode((mw_w, mw_h))
mw.fill((0,255,0))
clock = pygame.time.Clock()
FPS = 60

class Sprite:
    def __init__(self, image_name, x, y, width, hight, speed):
        self.image = pygame.transform.scale(
            pygame.image.load(image_name), (width, hight))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.speed = speed

    def reset(self):
        mw.blit(self.image, (self.rect.x, self.rect.y))

class Rockets(Sprite):
    #def init(self, image_name, x, y, width,
        #hight, speed, ball_speed1, ball_speed2):
        #super().init(self, image_name, x, y, width, hight, speed)
        #self.b_speed1 = ball_speed1
        #self.b_speed2 = ball_speed2
    def instant_(self):
        self.speed_x = 3
        self.speed_y = 3
    def rocket_l(self):
        key_ = pygame.key.get_pressed()
        if key_[pygame.K_w] and self.rect.y > 0:
            self.rect.y -= self.speed
        if key_[pygame.K_s] and self.rect.y < mw_h - 106:
            self.rect.y += self.speed

    def rocket_r(self):
        key_ = pygame.key.get_pressed()
        if key_[pygame.K_UP] and self.rect.y > 0:
            self.rect.y -= self.speed
        if key_[pygame.K_DOWN] and self.rect.y < mw_h - 106:
            self.rect.y += self.speed

    def move(self):
        speed1 = 3
        speed2 = 3
        self.rect.x += ball.speed_x
        self.rect.y += ball.speed_y
        if self.rect.x > 500:
            speed1 *= -1

        if self.rect.y > mw_h - 26 or self.rect.y < 0:
            speed2 *= -1


rct_l = Rockets('rc.png', 5, 0, 16, 106, 3)
rct_r = Rockets('rc.png', mw_w - 20, 0, 16, 106, 3)
ball = Rockets('ball.png', 220, 4, 26, 26, 5)
ball.instant_()

game = True
speed1 = 3
speed2 = 3
while game:

    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            game = False

    if game:
        mw.fill((0,255,0))
        rct_l.rocket_l()
        rct_r.rocket_r()
        #ball.move()

   
    ball.rect.x += speed1
    ball.rect.y += speed2

    if ball.rect.x > mw_w - 26 or ball.rect.x < 0:
        speed1 *= -1

    if ball.rect.y > mw_h - 26 or ball.rect.y < 0:
        speed2 *= -1
    
    if pygame.sprite.collide_rect(rct_l,ball):
        ball.speed_y = uniform(-5,5)
        ball.speed_x *= -1

    if pygame.sprite.collide_rect(rct_r,ball):
        ball.speed_y = uniform(-5,5)
        ball.speed_x *= -1

    rct_l.reset()
    rct_r.reset()
    ball.reset()

#wwww

    pygame.display.update()
    clock.tick(FPS)