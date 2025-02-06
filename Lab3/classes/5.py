class Account:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Внесено {amount}. Текущий баланс: {self.balance}")
        else:
            print("Сумма депозита должна быть положительной.")

    def withdraw(self, amount):
        if amount > 0:
            if amount <= self.balance:
                self.balance -= amount
                print(f"Снято {amount}. Текущий баланс: {self.balance}")
            else:
                print("Недостаточно средств.")
        else:
            print("Сумма снятия должна быть положительной.")

owner = input("Введите имя владельца счета: ")
balance = float(input("Введите начальный баланс счета: "))
account = Account(owner, balance)

while True:
    action = input("deposit or withdraw").lower()
    
    if action == 'deposit':
        amount = float(input("Введите сумму для депозита: "))
        account.deposit(amount)
    
    elif action == 'withdraw':
        amount = float(input("Введите сумму для снятия: "))
        account.withdraw(amount)
    
    elif action == 'exit':
        break
    
    else:
        print("Неверная команда. Попробуйте снова.")
