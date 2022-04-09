#import copy
import random
from threading import Lock

DirNames = ('','вперед','назад','вправо','влево')
DisNames = ('','один шаг','два шага','три шага')

class SingletonMeta(type):
    _instances = {}
    _lock: Lock = Lock()

    def __call__(cls, *args, **kwargs):
        with cls._lock:
            if cls not in cls._instances or args or kwargs:
                instance = super().__call__(*args, **kwargs)
                cls._instances[cls] = instance
        return cls._instances[cls]


class Game(metaclass=SingletonMeta):
    def __init__(self, start=True):
        self.x = 2 #random.randrange(0, 4)
        self.y = 0 #random.randrange(0, 4)
        self.exit = (0, 0)
        self.world = self.generate_world()

    def move(self, direction: int, steps: int):
        reverse = 1 if direction in (1, 3) else -1
        s = 0
        for i in range(1,steps+1):
            if direction in (1, 2):
                if -1 < self.y + reverse < len(self.world) and self.world[self.y + reverse][self.x]:
                    self.y += reverse
                    s = i
                else:
                    break
            else: # direction in (3, 4):    
                if -1 < self.x + reverse < len(self.world[0]) and self.world[self.y][self.x + reverse]:
                    self.x += reverse
                    s = i
                else:
                    break
                     
            if self.x == self.exit[0] and self.y == self.exit[1]:
                return 'Done' # выход найден

        if s == 0:
            return f"{DirNames[direction].capitalize()} пойти нельзя"

        return f"Вы прошли {DirNames[direction]} на {DisNames[s]}"

    def generate_world(self):
        return ((1,1,1,1,0),(1,1,0,1,1),(0,1,0,0,0),(1,1,1,1,1),(1,0,1,0,1))


