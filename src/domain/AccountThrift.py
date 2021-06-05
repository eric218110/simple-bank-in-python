from src.domain.Account import Account


class AccountThrift(Account):
    def withdraw(self, value: int) -> None:
        if self.balance < value:
            print('Saldo insuficiente')
            return
        self.balance -= value
        self.showMessage()
