import math

class Figure:
    sides_count = 0

    def __init__(self,color: list,*sides: int):
        self.__color = [*color] if self.__is_valid_color(*color) else [0,0,0]
        self.__sides = [*sides] if len(sides) == self.sides_count else [1] * self.sides_count
        if len(sides) == 1 and len(sides) != self.sides_count:
            self.__sides = sides * self.sides_count

    def get_color(self):
        return self.__color

    def __is_valid_color(self,r,g,b):
        if isinstance(r,int) and isinstance(g,int) and isinstance(b,int):
            if 0 <= r <= 255 and 0 <= g <= 255 and 0 <= b <= 255:
                return True
        return False
    def set_color(self,r,g,b):
        if self.__is_valid_color(r,g,b):
            self.__color = [r,g,b]

    def get_sides(self):
        return  self.__sides

    def __len__(self):
        return sum(self.__sides)
    def __is_valid_sides(self,*sides):
        for side in sides:
            if not isinstance(side, int):
                return False
        if len(sides) == self.sides_count:
            return True


    def set_sides(self, *new_sides):
        if self.__is_valid_sides(*new_sides):
            self.__sides = [*new_sides]

class Circle(Figure):
    sides_count = 1
    _radius = 0
    def get_square(self):
        self._radius = self.get_sides()[0]
        return math.pi * self._radius ** 2

class Triangle(Figure):
    sides_count = 3
    def get_square(self):
        a,b,c = self.get_sides()
        p = len(self)/2
        s = (p * (p - a) * (p - b) * (p - c)) ** (1/2)
        return s

class Cube(Figure):
    sides_count = 12
    def __init__(self,color: list,*sides: int):
        super().__init__(color,*sides)
        self.set_sides(*list(sides)*12)

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
