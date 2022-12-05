from db.db_manager import DBManager
from tinydb import Query

class BankAccount:
    db = DBManager()
    query = Query()

    def display_accounts():
        bank_accounts = BankAccount.db.bank_accounts.all()
        if len(bank_accounts) == 0:
            print(f"+{'-'*80}+")
            print(f"|{'  No Bank Acounts Found!':<80}|")
            print(f"+{'-'*80}+")
            return

        print(f"+{'-'*80}+")
        for account in BankAccount.db.bank_accounts.all():
            aid, name, type, currency, amount = account['id'], account['name'], account['type'], account['currency'], account['amount']
            print(f"|{f'  BankAccount [BAC{aid:04d}]':<80}|")
            print(f"|{f'   +- Name     : {name}':<80}|")
            print(f"|{f'   +- Type     : {type}':<80}|")
            print(f"|{f'   +- Currency : {currency}':<80}|")
            print(f"|{f'   +- Amount   : {amount}':<80}|")
            print(f"+{'-'*80}+")

    def add_account():
        aid = int(input("ID       : "))
        name = input("Name     : ")
        type = input("Type     : ")
        curr = input("Currency : ")
        amnt = float(input("Amount   : "))
        
        BankAccount.db.bank_accounts.insert({'id': aid, 'name': name, 'type': type, 'currency': curr, 'amount': amnt})

    def update_account():
        aid = int(input("ID : "))

        print(f"+{'-'*80}+")
        print(f"|{f'  BankAccount [BAC{aid:04d}]':<80}|")
        print(f"|{f'   1. Update Name':<80}|")
        print(f"|{f'   2. Update Type':<80}|")
        print(f"|{f'   3. Update Currency':<80}|")
        print(f"|{f'   4. Update Amount':<80}|")
        print(f"+{'-'*80}+")

        cm = input('>>> ')
        if cm == '1':
            name = input("Name : ")
            BankAccount.db.bank_accounts.update({'name': name}, BankAccount.query.id == aid)
        if cm == '2':
            type = input("Type : ")
            BankAccount.db.bank_accounts.update({'type': type}, BankAccount.query.id == aid)
        if cm == '3':
            curr = input("Currency : ")
            BankAccount.db.bank_accounts.update({'currency': curr}, BankAccount.query.id == aid)
        if cm == '4':
            amnt = input("Amount : ")
            BankAccount.db.bank_accounts.update({'amount': amnt}, BankAccount.query.id == aid)

    def remove_account():
        cid = int(input("ID : "))
        BankAccount.db.bank_accounts.remove(BankAccount.query.id == cid)
