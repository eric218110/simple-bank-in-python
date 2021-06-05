from src.domain.Account import Account


class AccountCurrent(Account):
    limit = 100

    def withdraw(self, value: int) -> None:
        if (self.balance + AccountCurrent.limit) < value:
            print('Saldo insuficiente')
            return
        self.balance -= value
        self.showMessage()
