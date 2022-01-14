""" The Account and Bank classes

"""

class Account(object):
    ID_COUNT = 1

    def __init__(self, name, **kwargs):
        self.id = self.ID_COUNT
        self.name = name
        self.__dict__.update(kwargs)
        Account.ID_COUNT += 1

    def transfer(self, amount):
        self.value += amount


class Bank(object):
    """A class to handle accounts and perform transfers"""

    def __init__(self):
        self.account = []

    def add(self, account):
        """A function to add an account to the Account list"""
        if isinstance(account, Account) and account not in self.account:
            self.account.append(account)

    def corrupted(self, account):
        """A function to check if an account is corrupted"""
        if len(account.__dict__) % 2 == 0:
            return 1
        if 'name' not in account.__dict__.keys():
            return 1
        if 'id' not in account.__dict__.keys():
            return 1
        if 'value' not in account.__dict__.keys():
            return 1
        zip_check = 0
        addr_check = 0
        for key in account.__dict__.keys():
            if key.startswith('zip'):
                zip_check = 1
            if key.startswith('addr'):
                addr_check = 1
            if key.startswith('b'):
                return 1
        if zip_check == 0 or addr_check == 0:
            return 1
        return 0

    def transfer(self, origin, dest, amount):
        """A function to transfer funds from one account to another"""
        or_elem = 0
        de_elem = 0
        for elem in self.account:
            if origin == elem.id or origin == elem.name:
                or_elem = elem
            if dest == elem.id or dest == elem.name:
                de_elem = elem
        if or_elem == 0 or de_elem == 0:
            print("Couldn't find account.")
            return False
        if self.corrupted(or_elem) or self.corrupted(de_elem):
            print("Corrupted account.")
            return False
        if amount <= 0 or or_elem.value < amount:
            print("Invalid amount.")
            return False
        or_elem.transfer(-amount)
        de_elem.transfer(amount)
        print("Transfer successful.")
        return True

    def fix_account(self, account):
        """A function to fix an account"""
        corrupted = 0
        zip_check = 0
        addr_check = 0
        for elem in self.account:
            if account in elem.__dict__.values():
                corrupted = elem
        if corrupted == 0:
            print("Couldn't find account.")
            return False
        keys = list(corrupted.__dict__.keys())
        if 'name' not in keys:
            corrupted.__dict__['name'] = 'Restored account'
        if 'id' not in keys:
            corrupted.__dict__['id'] = Account.ID_COUNT
            Account.ID_COUNT += 1
        if 'value' not in keys:
            corrupted.__dict__['value'] = 0
        for key in keys:
            if key.startswith('zip'):
                zip_check = 1
            if key.startswith('addr'):
                addr_check = 1
            if key.startswith('b'):
                corrupted.__dict__.pop(key)
        if zip_check == 0:
            corrupted.__dict__['zip'] = '00000'
        if addr_check == 0:
            corrupted.__dict__['addr'] = '42 rue des Corruptions'
        if len(corrupted.__dict__) % 2 == 0:
            for key in corrupted.__dict__.keys():
                if key == 'name' or key == 'id' or key == 'value':
                    pass
                elif key.startswith('zip') or key.startswith('addr'):
                    pass
                else:
                    corrupted.__dict__.pop(key)
                    break
        if self.corrupted(corrupted):
            print("Couldn't fix account.")
            return False
        else:
            print("Successfully fixed account !")
            return True
