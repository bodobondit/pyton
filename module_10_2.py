import threading
import time

class Knight(threading.Thread):
    def __init__(self,name,power):
        super().__init__(name = name)
        self.power = power

    def run(self):
        print(f'{self.name}, на нас напали!')
        enemy = 100
        count = 0
        while enemy > 0:
            time.sleep(1)
            count += 1
            enemy -= self.power
            print(f'{self.name} сражается {count} день(дня), осталось {enemy} воинов')
        print(f'{self.name} одержал победу спустя {count} дней(дня)!')


first_knight = Knight('Sir Lancelot', 10)
second_knight = Knight("Sir Galahad", 20)

first_knight.start()
second_knight.start()

first_knight.join()
second_knight.join()

print('Все битвы закончились!')
