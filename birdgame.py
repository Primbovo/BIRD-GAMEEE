from pygame import*
window = display.set_mode((700,500))
display.set_caption("Bird-Game      How to play:Don't let the hand slap you and try to collect 4 stars.")
background = transform.scale(image.load("sky.png"),(700,500))
lb = transform.scale(image.load("diedbird.jpeg"),(700,500))
wb = transform.scale(image.load("happybird.jpeg"),(700,500))
game = True
clock = time.Clock()
class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed,s,ss):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (s,ss))    
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y 
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))
class Player(GameSprite):
    def update(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_UP] and self.rect.y > 3:
            self.rect.y -= self.speed
        if keys_pressed[K_DOWN] and self.rect.y < 645:
            self.rect.y += self.speed
        if keys_pressed[K_LEFT] and self.rect.x > 3:
            self.rect.x -= self.speed
        if keys_pressed[K_RIGHT] and self.rect.x < 645:
            self.rect.x += self.speed

class Enemy(sprite.Sprite):
    direction = "DOWN"
    def __init__(self,player_image, player_x,player_speed,s,ss,u,d):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (s,ss))    
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.u = u
        self.d = d
    def update(self):
        if self.rect.y <= self.u:
            self.direction = "UP"
        if self.rect.y >= self.d:
            self.direction = "DOWN"
        if self.direction == "UP":
            self.rect.y += 5
        else:
            self.rect.y -= 6


plan = Player("bird.png",290,420,40,50,50)
plans = sprite.Group()
plans.add(plan)
d = 0
font.init()
font1 = font.Font(None,36)
point = 0
hand1 = Enemy("lu.png",200,15,100,100,50,100)
hand2 = Enemy("su.png",600,15,100,100,50,150)
hand3 = Enemy("lb.png",550,15,100,100,300,450)
hand4 = Enemy("sb.png",30,15,100,100,250,400)
hand5 = Enemy("lu.png",60,15,100,100,25,69)
hand6 = Enemy("randomhand.png",300,15,100,100,100,170)
hands = sprite.Group()
hands.add(hand1)
hands.add(hand2)
hands.add(hand3)
hands.add(hand4)
hands.add(hand5)
hands.add(hand6)
Star1 = GameSprite("star.png",400,10,100,50,50)
Star2 = GameSprite("star.png",300,300,100,50,50)
Star3 = GameSprite("star.png",400,200,100,50,50)
Star4 = GameSprite("star.png",100,400,100,50,50)
Stars = sprite.Group()
Stars.add(Star1)
Stars.add(Star2)
Stars.add(Star3)
Stars.add(Star4)
finish = False
while game :
    text_win = font1.render("You WIN",True,(1,1,1))
    text_lose = font1.render("You LOSE",True,(1,1,1))
    for e in event.get():
        if e.type == QUIT:
            game = False
    if not finish:
        window.blit(background,(0,0))
        hands.update()
        hands.draw(window)
        plans.update()
        plans.draw(window)
        Stars.update()
        Stars.draw(window)
        COL = sprite.groupcollide(plans,Stars,False,True)
        Fail = sprite.groupcollide(plans,hands,True,True)
        for e in COL:
            point += 1
        if point == 4 :
            finish = True
            window.blit(wb,(0,0))
            window.blit(text_win, (200,200))
        for e in Fail :
            d += 1
        if d == 1 :
            finish = True
            window.blit(lb,(0,0))
            window.blit(text_lose, (200,200))

        display.update()
        time.delay(50)