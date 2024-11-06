import math

class Figure:
    sides_count = 0

    def __init__(self,color,*sides):
        self.__color = []
        self.__sides = []
        for i in range(len(color)):
            self.__color.append(color[i])
        if len(sides) == self.sides_count:
            for i in range(self.sides_count):
                self.__sides.append(sides[i])
        elif len(sides) == 1:
            for i in range(self.sides_count):
               self.__sides.append(sides[0])
        else:
            for i in range(self.sides_count):
               self.__sides.append(1)

    def get_color(self):
        return self.__color

    def __is_valid_color(self,r,g,b):
        if isinstance(r,int) and isinstance(g,int) and isinstance(b,int):
            if 0 <= r <= 255 and 0 <= g <= 255 and 0 <= b <= 255:
                return True
            else:
                return False
        else:
            return False

    def set_color(self,r,g,b):
        if self.__is_valid_color(r,g,b):
            self.__color[0] = r
            self.__color[1] = g
            self.__color[2] = b

    def get_sides(self):
        return  self.__sides

    def __len__(self):
        return sum(self.__sides)

    def set_sides(self, *new_sides):
        if len(new_sides) == self.sides_count:
            for i in range(self.sides_count):
                self.__sides[i] = new_sides[i]

class Circle(Figure):
    sides_count = 1
    _radius = 0
    def get_square(self):
        self._radius = self.get_sides()[0]
        return math.pi * self._radius ** 2

class Triangle(Figure):
    sides_count = 3
    def get_square(self):
        sides = self.get_sides()
        p = len(self)/2
        s = (p * (p - sides[0]) * (p - sides[1]) * (p - sides[2])) ** (1/2)
        return s

class Cube(Figure):
    sides_count = 12

    def  get_volume(self):
        side = self.get_sides()[0]
        v = side ** 3
        return v

circle1 = Circle((200, 200, 100), 10) # (Цвет, стороны)
cube1 = Cube((222, 35, 130), 6)
triangl1 = Triangle((22,22,22),3,4,5)
print(triangl1.get_square())
print(circle1.get_square())
# Проверка на изменение цветов:
circle1.set_color(55, 66, 77) # Изменится
print(circle1.get_color())
cube1.set_color(300, 70, 15) # Не изменится
print(cube1.get_color())


# Проверка на изменение сторон:
cube1.set_sides(5, 3, 12, 4, 5) # Не изменится
print(cube1.get_sides())
circle1.set_sides(15) # Изменится
print(circle1.get_sides())

# Проверка периметра (круга), это и есть длина:
print(len(circle1))

# Проверка объёма (куба):
print(cube1.get_volume())
