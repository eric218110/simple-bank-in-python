from abc import ABC, abstractmethod


class Account(ABC):
    def __init__(self, agency: int, account, number: int, balance: int) -> None:
        self._agency = agency
        self._number = number
        self._account = account
        self._balance = balance

    @property()
    def agency(self) -> int:
        return self._agency

    @agency.setter
    def agency(self, agency: int) -> None:
        if not isinstance(agency, int):
            raise TypeError('Argument agency not type int')
        self._agency = agency

    @property()
    def number(self) -> int:
        return self._number

    @number.setter
    def number(self, number: int) -> None:
        if not isinstance(number, int):
            raise TypeError('Argument number not type int')
        self._number = number

    @property()
    def account(self) -> int:
        return self._account

    @account.setter
    def account(self, account: int) -> None:
        if not isinstance(account, int):
            raise TypeError('Argument account not type int')
        self._account = account

    @property()
    def balance(self) -> int:
        return self._balance

    @balance.setter
    def balance(self, balance: int) -> None:
        if not isinstance(balance, int):
            raise TypeError('Argument balance not type int')
        self._balance = balance

    @abstractmethod
    def withdraw(value: int) -> None:
        pass
