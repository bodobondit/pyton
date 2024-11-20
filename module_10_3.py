import threading
import time
from random import randint

lock = threading.Lock()

class Bank:
    def __init__(self,balance = 0,lock = lock):
        self.balance = balance
        self.lock = lock

    def deposit(self):
        for i in range(100):
            ran = randint(50,500)
            self.balance += ran
            print(f'Пополнение: {ran}. Баланс: {self.balance}')
            if self.balance >= 500 and self.lock.locked():
                self.lock.release()
            time.sleep(0.001)

    def take(self):
        for i in range(100):
            ran = randint(50,500)
            print(f'запрос на случайное число {ran}')
            if ran <= self.balance:
                self.balance -= ran
                print(f'Снятие: {ran}. Баланс: {self.balance}')
            else:
                print('Запрос отклонён, недостаточно средств')
                self.lock.acquire()
            time.sleep(0.001)

bk = Bank()

th1 = threading.Thread(target=Bank.deposit, args=(bk,))
th2 = threading.Thread(target=Bank.take, args=(bk,))

th1.start()
th2.start()
th1.join()
th2.join()

print(f'Итоговый баланс: {bk.balance}')

