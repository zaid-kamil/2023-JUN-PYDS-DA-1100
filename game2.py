from random import randint
import pgzrun

WIDTH = 1000    
HEIGHT = 500

class Player(Actor):
    '''This is class Player, that inherits from Actor'''
    speed = 5
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
    x = randint(50, WIDTH-50)
    y = randint(50, HEIGHT-50)

    def relocate(self):
        self.x = randint(50, WIDTH-50)
        self.y = randint(50, HEIGHT-50)

