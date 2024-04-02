# Aufgabe 1: Magische Methoden
class Vector3:
    def __init__(self,x,y,z):
        self.x = x
        self.y = y
        self.z = z

    def __str__(self):
        return f"({self.x},{self.y},{self.z})"
    
    def __add__(self, other):
        if type(other) == int or type(other) == float:
            return Vector3(self.x + other, self.y + other, self.z + other)
        else:
            return Vector3(self.x + other.x, self.y + other.y, self.z + other.z)
        
    def __radd__(self, other):
        return Vector2(self.x + other, self.y + other, self.z + other)

    def __sub__(self, other):
        if type(other) == int or type(other) == float:
            return Vector3(self.x - other, self.y - other, self.z - other)
        else:
            return Vector3(self.x - other.x, self.y - other.y, self.z - other.z)
        
    def __rsub__(self, other):
        return Vector3(self.x - other, self.y - other, self.z - other)
    
    def __mul__(self, other):
        if type(other) == int or type(other) == float:
            return Vector3(self.x * other, self.y * other, self.z * other)
        else:
            return Vector3(self.x * other.x, self.y * other.y, self.z * other.z)
        
    def __rmul__(self, other):
        return Vector3(self.x * other, self.y * other, self.z * other)
    
    def cross(self, other):
        return Vector3(self.y*other.z - self.z*other.y, self.z*other.x - self.x*other.z, self.x*other.y - self.y*other.x)
    
    
    def dot(self, other):
        return (self.x*other.x + self.y*other.y + self.z*other.z)
    
    def normalize(self):
        return Vector3(self.x*(1/(self.x**2+self.y**2+self.z**2)**0.5), self.y*(1/(self.x**2+self.y**2+self.z**2)**0.5), self.z*(1/(self.x**2+self.y**2+self.z**2)**0.5))
                       

##Kontrolle, Ausführung

a = Vector3(5,9,3)
b = Vector3(4,0,10)

print(str(a))
print(str(b))
print(a+b)
print(a-b)
print(a*b)
print(a.cross(b))
print(a.dot(b))
print(a.normalize())
    