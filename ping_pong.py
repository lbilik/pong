import pygame
import random
pygame.init()

#Koment
#123
mw_w = 500
mw_h = 500

mw = pygame.display.set_mode((mw_w, mw_h))
mw.fill((0,255,0))
clock = pygame.time.Clock()
FPS = 60

class Sprite():
    def __init__(self, image_name, x, y, width, hight, speed = 4):
        self.image = pygame.transform.scale(
            pygame.image.load(image_name), (width, hight))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.speed = speed

    def reset(self):
        mw.blit(self.image, (self.rect.x, self.rect.y))

class Rockets(Sprite):
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

class Ball(Sprite):

    def inst_speed(self):
        self.Speed_x = self.speed
        self.Speed_y = self.speed
    
    def pong_x(self):
        if self.rect.x > mw_w - 26:
            self.Speed_x = random.uniform(3.5, 5.5) * -1
        elif self.rect.x < 0:
            self.Speed_x = random.uniform(3.0, 5.5)

    def move(self):
        self.rect.x += self.Speed_x
        self.rect.y += self.Speed_y

        if self.rect.y > mw_h - 26:
            self.Speed_y = random.uniform(3.0, 5.5) * -1
        elif self.rect.y < 0:
            self.Speed_y = random.uniform(3.0, 5.5)

rct_l = Rockets('rc.png', 5, 0, 16, 106)
rct_r = Rockets('rc.png', mw_w - 20, 0, 16, 106)
ball = Ball('ball.png', random.randint(50,mw_w-50), random.randint(80,mw_w-80),26,26, random.choice([-3,3]))
ball.inst_speed()

def ping_pong():
    if pygame.sprite.collide_rect(rct_l, ball):
        ball.Speed_x = random.uniform(3, 5)
        ball.Speed_y = random.uniform(-4, 4)
        '''
        if random.random() > 0.5:
            ball.Speed_y *= -1
        else:
            ball.Speed_y *= 1
        '''
    if pygame.sprite.collide_rect(rct_r, ball):
        ball.Speed_x = -random.uniform(3, 5)
        ball.Speed_y = random.uniform(-4, 4)
        '''
        if random.random() > 0.5:
            ball.Speed_y *= -1
        else:
            ball.Speed_y *= 1
        '''

game = True

while game:

    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            game = False

    ping_pong()

    if game:
        mw.fill((0,255,0))
        rct_l.rocket_l()
        rct_r.rocket_r()
        ball.move()
        ball.pong_x()

    rct_l.reset()
    rct_r.reset()
    ball.reset()

    pygame.display.update()
    clock.tick(FPS)


