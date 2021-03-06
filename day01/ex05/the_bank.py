

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
            return (1)
        if 'name' not in account.__dict__.keys():
            return (1)
        if 'id' not in account.__dict__.keys():
            return (1)
        if 'value' not in account.__dict__.keys():
            return (1)
        zip_check = 0
        addr_check = 0
        for str in account.__dict__.keys():
            if str.startswith('zip'):
                zip_check = 1
            if str.startswith('addr'):
                addr_check = 1
            if str.startswith('b'):
                return (1)
        if zip_check == 0 or addr_check == 0:
            return (1)
        return (0)

    def transfer(self, origin, dest, amount):
        or_elem = 0
        de_elem = 0
        for elem in self.account:
            if origin == elem.id or origin == elem.name:
                or_elem = elem
            if dest == elem.id or dest == elem.name:
                de_elem = elem
        if or_elem == 0 or de_elem == 0:
            print("Couldn't find account.")
            return (False)
        if self.corrupted(or_elem) or self.corrupted(de_elem):
            print("Corrupted account.")
            return (False)
        if amount <= 0 or or_elem.value < amount:
            print("Invalid amount.")
            return (False)
        or_elem.transfer(-amount)
        de_elem.transfer(amount)
        print("Transfer successful.")
        return (True)

    def fix_account(self, account):
        corrupted = 0
        zip_check = 0
        addr_check = 0
        for elem in self.account:
            if account in elem.__dict__.values():
                corrupted = elem
        if corrupted == 0:
            print("Couldn't find account.")
            return (False)
        keys = list(corrupted.__dict__.keys())
        if 'name' not in keys:
            corrupted.__dict__['name'] = 'Restored account'
        if 'id' not in keys:
            corrupted.__dict__['id'] = Account.ID_COUNT
            Account.ID_COUNT += 1
        if 'value' not in keys:
            corrupted.__dict__['value'] = 0
        for str in keys:
            if str.startswith('zip'):
                zip_check = 1
            if str.startswith('addr'):
                addr_check = 1
            if str.startswith('b'):
                corrupted.__dict__.pop(str)
        if zip_check == 0:
            corrupted.__dict__['zip'] = '00000'
        if addr_check == 0:
            corrupted.__dict__['addr'] = '42 rue des Corruptions'
        if len(corrupted.__dict__) % 2 == 0:
            for str in corrupted.__dict__.keys():
                if str == 'name' or str == 'id' or str == 'value':
                    pass
                elif str.startswith('zip') or str.startswith('addr'):
                    pass
                else:
                    corrupted.__dict__.pop(str)
                    break
        if self.corrupted(corrupted):
            print("Couldn't fix account.")
            return (False)
        else:
            print("Successfully fixed account !")
            return (True)


acc1 = Account("First", bob=6, todd=4)
acc2 = Account("Second", zip='TAZ42', addr='69 rue des Rosiers')
bnk = Bank()
print(bnk.__dict__)
lst = acc1.__dir__()
bnk.add(acc1)
bnk.add(acc2)
acc1.__dict__.pop('id')
print(acc1.__dict__)
print(acc2.__dict__)
bnk.fix_account("First")
print(acc1.__dict__)
print(acc2.__dict__)
print(bnk.__dict__)
print(len(lst))
