from geoform import GeoForm


class Kreis(GeoForm):
    PI = 3.1415926

    def __init__(self, radius):
        self.radius = radius

    def umfang(self):
        return 2 * self.radius * Kreis.PI

    def flaeche(self):
        return self.radius * self.radius * Kreis.PI