from abc import ABC, abstractmethod


class Account(ABC):
    def __init__(self, agency, account, balance) -> None:
        self.agency = agency
        self.account = account
        self.balance = balance

    def deposit(self, value: int) -> None:
        self.balance += value
        self.showMessage()

    def showMessage(self) -> None:
        print('************************')
        print(f'Agência: {self.agency}')
        print(f'Conta: {self.account}')
        print(f'Saldo: {self.balance}')
        print('************************')

    @abstractmethod
    def withdraw(self, value: int) -> None: pass
