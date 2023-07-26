from random import randint
import pgzrun

WIDTH = 1000    
HEIGHT = 500

class Player(Actor):
    '''This is class Player, that inherits from Actor'''
    speed = 5

    def __init__(self, image):
        super().__init__(image)
        self.pos = (WIDTH/2, HEIGHT/2) 

    def movement(self):
        '''This is method movement, that controls player movement'''
        if keyboard.left:
            self.x -= self.speed
        if keyboard.right:
            self.x += self.speed
        if keyboard.up:
            self.y -= self.speed
        if keyboard.down:
            self.y += self.speed
        if keyboard.space:
            self.angle += self.speed 

class Enemy(Actor):
    speed = 2
    def __init__(self, image):
        super().__init__(image) # call parent class constructor
        self.pos = (-100, HEIGHT/2) # set initial position

    def tracking(self, p):
        # enemy tracks player
        if p.x > self.x:
            self.x += self.speed
        if p.x < self.x:
            self.x -= self.speed 
        if p.y > self.y:
            self.y += self.speed
        if p.y < self.y:
            self.y -= self.speed
        print(f'player {p.pos} enemy {self.pos}')
        if self.colliderect(p):
            exit()

class Fruit(Actor):
    
    def __init__(self, image):
        super().__init__(image)
        x = randint(50, WIDTH-50)
        y = randint(50, HEIGHT-50)

    def relocate(self):
        self.x = randint(50, WIDTH-50)
        self.y = randint(50, HEIGHT-50)

# game code start now

p = Player('hero')
e = Enemy('enemy')
c = Fruit('fruit')  
score = 0

def draw():
    screen.clear()
    p.draw()
    e.draw()
    c.draw()
    screen.draw.text(f'Score: {score}', (10, 10), color='white')

def update():
    p.movement()
    e.tracking(p)

pgzrun.go()

