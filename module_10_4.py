import time
from queue import Queue
from random import randint
from threading import Thread

class Table:
    def __init__(self,number):
        self.number = number
        self.guest = None

class Guest(Thread):
    def __init__(self,name):
        super().__init__(name = name)
    def run(self):
        ran = randint(3,10)
        time.sleep(ran)

class Cafe:
    def __init__(self,*tables,):
        self.queue = Queue()
        self.tables = [*tables]
    def guest_arrival(self,*guests):
        seat_in_table = False
        for guest in guests:
            for table in self.tables:
                if table.guest is None:
                    table.guest = guest
                    guest.start()
                    print(f'{guest.name} сел(-а) за стол номер {table.number}')
                    seat_in_table = True
                    break
                else:
                    seat_in_table = False
            if not seat_in_table:
                self.queue.put(guest)
                print(f'{guest.name}  в очереди')
    def discuss_guests(self):
        while not self.queue.empty(): 
            for table in self.tables:
                if not table.guest is None:
                    if table.guest.is_alive():
                        print(f'{table.guest.name} покушал(-а) и ушёл(ушла)')
                        print(f'Стол номер {table.number} свободен')
                        table.guest = None
                    if not self.queue.empty():
                        table.guest = self.queue.get()
                        print(f'{table.guest.name} вышел(-ла) из очереди и сел(-а) за стол номер {table.number}')
                        table.guest.start()
# Создание столов
tables = [Table(number) for number in range(1, 6)]
# Имена гостей
guests_names = [
'Maria', 'Oleg', 'Vakhtang', 'Sergey', 'Darya', 'Arman',
'Vitoria', 'Nikita', 'Galina', 'Pavel', 'Ilya', 'Alexandra'
]
# Создание гостей
guests = [Guest(name) for name in guests_names]
# Заполнение кафе столами
cafe = Cafe(*tables)
# Приём гостей
cafe.guest_arrival(*guests)
# Обслуживание гостей
cafe.discuss_guests()
