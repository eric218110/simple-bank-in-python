from abc import ABC, abstractmethod


class Account(ABC):
    def __init__(self, agency: int, account, number: int, balance: int) -> None:
        self.agency = agency
        self.number = number
        self.account = account
        self.balance = balance

    def deposit(self, value: int) -> None:
        self.balance += value
        self.showMessage()

    def showMessage(self) -> None:
        print(f'Agência: {self.agency}')
        print(f'Conta: {self.account}')
        print(f'Saldo: {self.balance}')

    @abstractmethod
    def withdraw(self, value: int) -> None: pass
