

class Account(object):
    ID_COUNT = 1
    def __init__(self, name, **kwargs):
        self.id = self.ID_COUNT
        self.name = name
        self.__dict__.update(kwargs)
        if not hasattr(self, 'value'):
            self.value = 0
        Account.ID_COUNT += 1

    def transfer(self, amount):
        self.value += amount

class Bank(object):

    def __init__(self):
        self.account = []

    def add(self, account):
        if isinstance(account, Account):
            self.account.append(account)

    def corrupted(self, account):
        if len(account.__dict__) % 2 == 0:
            return (0)


        
        if 'name' not in account.__dict__.keys():
            return (0)
        if 'id' not in account.__dict__.keys():
            return (0)
        if 'value' not in account.__dict__.keys():
            return (0)
        return (1)

    def transfer(self, origin, dest, amount):
        or_elem = 0
        de_elem = 0
        for elem in self.account:
            if origin == elem.id or origin == elem.name:
                or_elem = elem
            if dest == elem.id or dest == elem.name:
                de_elem = elem
        if or_elem == 0 or de_elem == 0:
            return (False)
        if corrupted(or_elem) or corrupted(de_elem):
            return (False)
        if not isinstance(amount, float) amount > 0 and or_elem.value > amount:
            return (False)
        or_elem.transfer(-amount)
        de_elem.transfer(amount)
        return (True)

    def fix_account(self, account):
        pass
# """
# fix the corrupted account
# @account: int(id) or str(name) of the account
# @return True if success, False if an error occured
# """

acc1 = Account("First", value=50)
acc2 = Account("Second")
bnk = Bank()
lst = acc1.__dir__()
bnk.add(acc1)
bnk.add(acc2)
bnk.transfer("First", 2, 50)
# print(acc1.__dict__)
# print(acc2.__dict__)
# print(bnk.__dict__)
# print(len(lst))
