class House:
    def __init__(self,name,number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors
    def __new__(cls, *args, **kwargs):
        cls.houses_history.append(args[0])
        return object.__new__(cls)
    def go_to (self,new_floor):
        if new_floor > self.number_of_floors or new_floor < 1:
            print("Такого этажа не существует")
        else:
            for i in range(1,new_floor+1):
                print(i)
    def __len__(self):
        return self.number_of_floors
    def __str__(self):
        return f'Название: {self.name}, количество этажей: {self.number_of_floors}'
    def __eq__(self, other):
        if isinstance(other, int):
            return True if self.number_of_floors == other else False
        if isinstance(other, House):
            return True if self.number_of_floors == other.number_of_floors else False
    def __lt__(self, other):
        if isinstance(other, int):
            return True if self.number_of_floors < other else False
        if isinstance(other, House):
            return True if self.number_of_floors < other.number_of_floors else False
    def __le__(self, other):
        if isinstance(other, int):
            return True if self.number_of_floors <= other else False
        if isinstance(other, House):
            return True if self.number_of_floors <= other.number_of_floors else False
    def __gt__(self, other):
        if isinstance(other, int):
            return True if self.number_of_floors > other else False
        if isinstance(other, House):
            return True if self.number_of_floors > other.number_of_floors else False
    def __ge__(self, other):
        if isinstance(other, int):
            return True if self.number_of_floors >= other else False
        if isinstance(other, House):
            return True if self.number_of_floors >= other.number_of_floors else False
    def __ne__(self, other):
        if isinstance(other, int):
            return True if self.number_of_floors != other else False
        if isinstance(other, House):
            return True if self.number_of_floors != other.number_of_floors else False
    def __add__(self, value):
        self.number_of_floors = self.number_of_floors + value
        return self
    def __iadd__(self, other):
        if isinstance(other, int):
            return House.__add__(self, other)
        if isinstance(other, House):
            return House.__add__(self,other.number_of_floors)
    def __radd__(self, other):
        if isinstance(other, int):
            return House.__add__(self, other)
        if isinstance(other, House):
            return House.__add__(self, other.number_of_floors)
    houses_history = []
    def __del__(self):
        self.houses_history.remove(self.name)
        print(f'{self.name} снесён, но он останется в истории')

h1 = House('ЖК Эльбрус', 10)
print(House.houses_history)
h2 = House('ЖК Акация', 20)
print(House.houses_history)
h3 = House('ЖК Матрёшки', 20)
print(House.houses_history)

# Удаление объектов
del h2
del h3

print(House.houses_history)

