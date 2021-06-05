from src.domain.Account import Account


class AccountCurrent(Account):
    def __init__(self, agency: int, account, number: int, balance: int, limitExtra: int = 100) -> None:
        super.__init__(agency, account, number, balance)
        self.limitExtra = limitExtra

    def withdraw(self, value: int) -> None:
        if (self.balance + self.limitExtra) < value:
            print('Saldo insuficiente')
            return
        self.balance -= value
        self.showMessage()
