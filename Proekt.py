from pygame import *
from random import randint
from time import time as timer 
font.init()
font1 = font.SysFont("Arial", 80)
win = font1.render('YOU WIN!', True, (255, 255, 255))
lose_left = font1.render('The left side lost', True, (180, 0, 0))
lose_raight = font1.render('The right side lost', True, (180, 0, 0))


font2 = font.Font(None, 36)


img_back = "galaxy.jpg" #фон игры
img_bullet = "bullet.png" #пуля




class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, size_x, size_y, player_speed):
        sprite.Sprite.__init__(self)
        self.size_y = size_y
        self.size_x = size_x
        self.image = transform.scale(image.load(player_image), (size_x, size_y))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def update_l(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y < win_height - self.size_y:
            self.rect.y += self.speed

    def update_r(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < win_height - self.size_y:
            self.rect.y += self.speed

class Ball(GameSprite):
    def speeds(self, speed_x, speed_y):
        self.speed_x = speed_x
        self.speed_y = speed_y

    def update(self):
        if self.rect.y > 470 or self.rect.y < 0:
            self.speed_y *= -1
            print(self.speed_y)
        self.rect.x += self.speed_x
        self.rect.y += self.speed_y
 
#создаём окошко
win_width = 700
win_height = 500
display.set_caption("Ping500")
window = display.set_mode((win_width, win_height))
background = transform.scale(image.load("background.jpg"), (win_width, win_height))
player1 = Player("free.png", 30, win_height/2, 20, 100, 10)
player2 = Player("free.png", win_width - 50, win_height/2, 20, 100, 10)
apple = Ball("apple.png", win_width / 2, win_height/ 2 , 30, 30, 10)
apple.speeds(5,5)
finish = False

run = True 
rel_time = False
num_fire = 0 

while run:
   #событие нажатия на кнопку “Закрыть”
    for e in event.get():
        if e.type == QUIT:
            run = False
        elif e.type == KEYDOWN:
            if e.key == K_SPACE:
                pass

    if not finish:
        #обновляем фон
        window.blit(background,(0,0))

        #производим движения спрайтов
        player1.update_l()
        player2.update_r()
        apple.update()

        #обновляем их в новом местоположении при каждой итерации цикла
        player1.reset()
        player2.reset()
        apple.reset()



        if sprite.collide_rect(apple, player1) or sprite.collide_rect(apple, player2):
            apple.speed_x *= -1


        if apple.rect.x ==  700:
            window.blit(lose_raight, (10, 20))
            finish = True
        if apple.rect.x == 0:
            window.blit(lose_left, (10,20))
            finish = True

        display.update()



    time.delay(50)
display.update()
