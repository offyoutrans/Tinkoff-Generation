class Field:
    def __init__(self, n):
        self.n = n
        self.field = [['' for i in range(n)] for i in range(n)]
        self.gamers = [Gamer(), Gamer()]
        self.t = 0
    def turn(self):

    
class Gamer:
    def __init__(self):
        self.lines = {'lr':[], 'rl':[], 'hor':[], 'ver':[]}
    def turn(self, x, y):
        for i in lines['lr']:
            lowx, lowy, highx, highy length = i
            if 