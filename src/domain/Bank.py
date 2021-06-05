class Bank:
    def __init__(self):
        self.agencyList = [1111, 2222, 3333]
        self.clientList = []
        self.accountList = []

    def addAccount(self, account):
        self.accountList.append(account)

    def addClient(self, client):
        self.clientList.append(client)

    def authenticate(self, client):
        if client not in self.clientList:
            return False

        if client.account not in self.accountList:
            return False

        if client.account.agency not in self.agencyList:
            return False
        return True
