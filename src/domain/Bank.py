class Bank:
    def __init__(self):
        self.agencyList = [1111, 2222, 3333]
        self.clientList = []
        self.accountList = []

    def addAccount(self, account):
        print(account)
        self.accountList.append(account)

    def addClient(self, client):
        self.clientList.append(client)

    def authenticate(self, client):

        return True
