from abc import ABC,abstractmethod
import random

class Player(ABC):
    def __init__(self):
        self.moves = []
        self.position = (0, 0)
        self.path = [self.position]

    @abstractmethod
    def level_up(self):
        pass

    def make_move(self):
        random_move = random.choice(self.moves)
        self.position = (self.position[0] + random_move[0],self.position[1] + random_move[1])
        
        self.path.append(self.position)
        return self.position

    

class Pawn(Player):
    def __init__(self):
        super().__init__()
        self.moves = [(0,1),(0,-1),(-1,0),(1,0)]
    def level_up(self):
        self.moves.extend([(1,1),(1,-1),(-1,-1),(-1,1)])

p = Pawn()
print(p.position)
p.make_move()
print(p.position)
print(p.path)
p.level_up()
print(p.moves)
p.make_move()
print(p.position)
print(p.path)