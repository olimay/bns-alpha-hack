class Game:
    def __init__(self):
        self.realtime = False

class Tableau:
    def __init__(self):
        self.height = 5
        self.width = 5

class Card:
    def __init__(self):
        self.height = 1
        self.width = 1
        self.hp = 0

class Player(Card):
    def __init__(self):

class Boss:
    # not a card
    def __init__(self):

class Powerup(Card):
    def __init__(self):

class Enemy(Card):
    def __init__(self):

class Grunt(Enemy):
    # enemy with lower hitpoints, movement 1
    def __init__(self):

class Soldier(Enemy):
    # enemy with higher hitpoints, movement 1
    def __init__(self):

class Skirmisher(Enemy):
    # enemy that can jump over obstacles
    def __init__(self):

class Artillery(Enemy):
    # enemy that can fire ranged attacks, movement 1
    def __init__(self):

class Fortress(Enemy):
    # immobile enemy with high hitpoints

class Obstacle(Enemy):
    def __init__(self):

class Coin(Card):
    def __init__(self):
