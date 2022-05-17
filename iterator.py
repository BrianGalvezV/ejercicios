class rango():
    def __init__(self, low, higt) -> None:
        self.currer = low
        self.alto = higt

    def __iter__(self):
        return self
    
    def __next_(self):
        while self.currer > self.alto:
            return StopIteration
        self.currer += 1


for j in rango(5,9):
    pass