import sys
import math
import matplotlib.pyplot as plt

DRAW_NSTEPS = 10240

class Paint:
    def __init__(self, width=1000, height=1000):
        self.canvas = []
        for line in range(height):
            line_data = list()
            for col in range(width):
                line_data.append([255, 255, 255])
            self.canvas.append(line_data)

    def set_pixel(self, x, y, r=0, g=0, b=0):
        if x < 0 or y < 0:
            return
        if y >= len(self.canvas):
            return
        if x >= len(self.canvas[y]):
            return

        self.canvas[y][x] = [r, g, b]

    def show(self):
        plt.gca().invert_yaxis()
        plt.imshow(self.canvas)
        plt.show()
        sys.exit(0)

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def dist(self, autre):
        s =  (autre.x - self.x) ** 2
        s += (autre.y  - self.y) ** 2
        return math.sqrt(s)

    def draw(self, paint):
        paint.set_pixel(self.x, self.y)

class Ligne:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def get_length(self):
        return self.a.dist(self.b)

    def draw(self, paint):
        dx = (self.b.x - self.a.x) / DRAW_NSTEPS
        dy = (self.b.y - self.a.y) / DRAW_NSTEPS

        x = float(self.a.x)
        y = float(self.a.y)
        for step in range(DRAW_NSTEPS):
            paint.set_pixel(int(round(x, 0)), int(round(y, 0)))
            x += dx
            y += dy

class Parallelogramme:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

        self.x = c.x + (b.x - a.x)
        self.y = c.y + (b.y - a.y)
        self.d = Point(self.x, self.y)

    def draw(self, paint):
        ab = Ligne(self.a, self.b)
        ac = Ligne(self.a, self.c)
        cd = Ligne(self.c, self.d)
        bd = Ligne(self.b, self.d)

        ab.draw(paint)
        ac.draw(paint)
        cd.draw(paint)
        bd.draw(paint)

class Triangle:
    def __init__(self, a : Point, b : Point, c : Point):
        self.a = a
        self.b = b
        self.c = c

    def draw(self, paint):
        ab = Ligne(self.a, self.b)
        ac = Ligne(self.a, self.c)
        bc = Ligne(self.b, self.c)

        ab.draw(paint)
        ac.draw(paint)
        bc.draw(paint)

class RectangleTriangle:
    def __init__(self, a : Point, b : Point, angle : int):
        self.a = a
        self.b = b
        self.angle = math.radians(angle)

        self.ab = Ligne(self.a, self.b)
        self.bc = self.ab.get_length()/math.cos(self.angle)
        self.ac = self.bc * math.sin(self.angle)

        self.x = self.a.x + self.ac * (self.b.y - self.a.y)/self.ab.get_length()
        self.y = self.a.y + self.ac * (self.b.x - self.a.x)/self.ab.get_length()
        self.c = Point(self.x, self.y)

        self.triangle = Triangle(self.a, self.b, self.c)

paint = Paint()

#### Début du sujet
### Définition de classes ici
a = Point(100, 100)
b = Point(300, 100)
c = Point(100, 300)

### Instanciation d'objets géométriques ici
test = RectangleTriangle(a, b, 65)
test.triangle.draw(paint)
###

paint.show()
