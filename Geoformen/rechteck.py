from geoform import GeoForm


class Rechteck(GeoForm):
    def __init__(self, laenge, breite):
        self.laenge = laenge
        self.breite = breite

    def umfang(self):
        return (self.laenge + self.breite) * 2

    def flaeche(self):
        return self.laenge * self.breite