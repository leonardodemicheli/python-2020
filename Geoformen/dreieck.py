from geoform import GeoForm


class Dreieck(GeoForm):
    def __init__(self, a, b, c, alpha, beta):
        self.a = a
        self.b = b
        self.c = c
        self.alpha = alpha
        self.beta = beta
        self.gamma = 180 - (alpha + beta)

    def umfang(self):
        return (self.a + self.b + self.c)