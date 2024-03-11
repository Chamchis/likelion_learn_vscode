class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"{amount}가 입금되었습니다.")

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            print(f"{amount}가 출금되었습니다.")
        else:
            print("잔액이 부족합니다.")

account = BankAccount("Alice")
account.deposit(1000)
account.withdraw(500)