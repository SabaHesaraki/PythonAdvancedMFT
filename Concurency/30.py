import threading

class BankAccount:
    def __init__(self, balance=0):
        self.balance = balance
        self.lock = threading.RLock()

    def deposit(self, amount):
        with self.lock:
            self.balance += amount

    def withdraw(self, amount):
        with self.lock:
            self.balance -= amount

    def transfer(self, other, amount):
        with self.lock:
            self.withdraw(amount)
            other.deposit(amount)

a=BankAccount(100)
b=BankAccount(50)
a.transfer(b,30)

print("a:",a.balance)
print("b:",b.balance)