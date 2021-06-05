from src.domain.Person import Person


class Client(Person):
    def __init__(self, name: str, age: int):
        super().__init__(name, age)
        self._account = None

    def addAccount(self, account):
        self._account = account
