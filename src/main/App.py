from src.domain.Bank import Bank
from src.domain.Client import Client
from src.domain.AccountCurrent import AccountCurrent
from src.domain.AccountThrift import AccountThrift


class App:
    def run():
        bank = Bank()
        clientJoe = Client('Joe', 35)
        clientMaria = Client('Maria', 42)
        clientAnna = Client('Anna', 25)

        accountOne = AccountThrift(1111, 1111, 0)
        accountTwo = AccountThrift(2222, 1111, 0)
        accountThree = AccountCurrent(1234, 1111, 0)

        clientJoe.addAccount(accountOne)
        clientMaria.addAccount(accountTwo)
        clientAnna.addAccount(accountThree)

        bank.addAccount(accountOne)
        bank.addClient(clientJoe)

        if (bank.authenticate(accountOne)):
            clientJoe.account.deposit(20)
            clientJoe.account.withdraw(10)
        else:
            print('Não autorizado !')

