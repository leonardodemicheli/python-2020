from dreieck import Dreieck


class Gleichseitiges_Dreick(Dreieck):
    def __init__(self, a):
        self.a = a
        self.b = a
        self.c = a
        self.alpha = 60
        self.beta = 60
        self.gamma = 60
