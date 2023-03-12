from pygame import *

#Заготовки изображений
img_back = "Background.png" # фон игры
img_player = 'Player_1.png'
img_enemy = 'Ball.png'


#класс-родитель для других спрайтов
class GameSprite(sprite.Sprite):
 #конструктор класса
    def __init__(self, player_image, player_x, player_y, size_x, size_y, player_speed):
       #Вызываем конструктор класса (Sprite):
       sprite.Sprite.__init__(self)


       #каждый спрайт должен хранить свойство image - изображение
       self.image = transform.scale(image.load(player_image), (size_x, size_y))
       self.speed = player_speed


       #каждый спрайт должен хранить свойство rect - прямоугольник, в который он вписан
       self.rect = self.image.get_rect()
       self.rect.x = player_x
       self.rect.y = player_y
 #метод, отрисовывающий героя на окне
    def reset(self):
       window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
   #метод для управления спрайтом стрелками клавиатуры
    def Player(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < 400 :
            self.rect.y += self.speed
    def Player_S(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y < 400 :
            self.rect.y += self.speed

class Enemy(GameSprite):
   #движение врага
    def update(self):
        self.rect.y += self.speed
        global lost
        #исчезает, если дойдет до края экрана
        if self.rect.y > win_height:
            self.rect.x = randint(80, win_width - 80)
            self.rect.y = 0
            lost = lost + 1

#Создаём окошко
win_width = 700
win_height = 500
display.set_caption("Pong")
window = display.set_mode((win_width, win_height))
background = transform.scale(image.load(img_back), (win_width, win_height))

#Создание спрайтов
Player_One = Player(img_player,20, 100, 20, 100,3)
Player_Two = Player(img_player,670, 100,20,100,3)

Ball = Enemy(img_enemy, 350, 250, 60,60, 3)

finish = False
run = True #флаг сбрасывается кнопкой закрытия окна
while run:
   #событие нажатия на кнопку “Закрыть”
    for e in event.get():
        if e.type == QUIT:
         run = False

    if not finish:
      #обновляем фон
        window.blit(background,(0,0))

        Player_One.reset()
        Player_Two.reset()
        Player_One.Player_S()
        Player_Two.Player()
        
        Ball.reset()

    display.update()