from kreis import Kreis
from rechteck import Rechteck
from quadrat import Quadrat
from dreieck import Dreieck

k = Kreis(2)

print(k.umfang())
print(k.info())

r = Rechteck(5, 3)

print(r.flaeche())
print(r.umfang())
print(r.info())

q = Quadrat(4)

print(q.flaeche())
print(q.info())

d = Dreieck (3, 4, 5, 90, 45)