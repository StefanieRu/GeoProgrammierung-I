## Aufgabe 1: Vererbung

import math
class Punkt:
    def __init__(self, x, y):
        self.x = x
        self.y = y
#---------------------------------#
class Figur:
    def __init__(self):
        self.name = "Figur"

    def Umfang(self):
        return 0

    def __str__(self):
        return self.name

class Dreieck(Figur):
    def __init__(self, punktA, punktB, punktC):
        super().__init__()
        self.A = punktA
        self.B = punktB
        self.C = punktC
        self.name = "Dreieck"

    def Umfang(self):
        return ((((self.A.x-self.B.x)**2+(self.A.y-self.B.y)**2)**0.5)+(((self.A.x-self.C.x)**2+(self.A.y-self.C.y)**2)**0.5)+(((self.B.x-self.C.x)**2+(self.B.y-self.C.y)**2)**0.5))

    
    
class Rechteck(Figur):
    def __init__(self, punktR1, punktR2):
        super().__init__()
        self.R1 = punktR1
        self.R2 = punktR2
        self.name = "Rechteck"

    def Umfang(self):
        return ((abs(self.R1.x-self.R2.x)+abs(self.R1.y-self.R2.y))*2)
    
class Kreis(Figur):
    def __init__(self, mittelpunkt, radius):
        super().__init__()
        self.m = mittelpunkt
        self.r = radius
        self.name = "Kreis"

    def Umfang(self):
        return math.pi * self.r*2
    
## Eingabe bis maximal 6 Ecken.
class Polygon(Figur):
    def __init__(self, Ecke1, Ecke2, Ecke3, Ecke4, Ecke5, Ecke6):
        super().__init__()
        self.E1 = Ecke1
        self.E2 = Ecke2
        self.E3 = Ecke3
        self.E4 = Ecke4
        self.E5 = Ecke5
        self.E6 = Ecke6
        self.name = "Polygon"


    def Umfang(self):
               return ((((self.E1.x-self.E2.x)**2+(self.E1.y-self.E2.y)**2)**0.5)+(((self.E2.x-self.E3.x)**2+(self.E2.y-self.E3.y)**2)**0.5)+(((self.E3.x-self.E4.x)**2+(self.E3.y-self.E4.y)**2)**0.5)+(((self.E4.x-self.E5.x)**2+(self.E4.y-self.E5.y)**2)**0.5)+(((self.E5.x-self.E6.x)**2+(self.E5.y-self.E6.y)**2)**0.5)+(((self.E6.x-self.E1.x)**2+(self.E6.y-self.E1.y)**2)**0.5))



d = Dreieck(Punkt(0,0), Punkt(3,4),Punkt(3,0))
print(d.name, "Punkt A ",d.A.x, d.A.y, " Punkt B ", d.B.x, d.B.y, " Punkt C ", d.C.x, d.C.y, " U=",d.Umfang())

r = Rechteck(Punkt(0,0),Punkt(5,3))
print(r.name, "Punkt 1 ", r.R1.x, r.R1.y, " Punkt 2 ", r.R2.x, r.R2.y, " U=",r.Umfang())

k = Kreis(Punkt(0,0),10)
print(k.name, " Mittelpunkt ", k.m.x, k.m.y, " Radius ", k.r, " U=", k.Umfang())

p = Polygon(Punkt(0,0),Punkt(1,1),Punkt(2,2),Punkt(3,3),Punkt(4,4),Punkt(5,5))
print(p.name, "Ecke 1 ", p.E1.x, p.E1.y, "Ecke 2 ", p.E2.x, p.E2.y, "Ecke 3 ", p.E3.x, p.E3.y, "Ecke 4 ", p.E4.x, p.E4.y, "Ecke 5 ", p.E5.x, p.E5.y, "Ecke 6 ", p.E6.x, p.E6.y, "U=",p.Umfang())