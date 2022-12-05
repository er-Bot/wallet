from client_controller import Client
from project_controller import Project
from bank_account_controller import BankAccount


class IOManager:
    def __init__(self) -> None:
        print(f"+{'-'*80}+")
        print(f"|{'Welcome to Erbo-WALLET':^80}|")
        print(f"+{'-'*80}+")

        self.navigate('0')

    def navigate(self, mc):
        if mc == '0': self.display_main_menu()
        elif mc == '1': self.display_dashboard()
        elif mc == '2': self.display_freelance()
        elif mc == '20': self.navigate('0')
        elif mc == '21': self.display_client_menu()
        elif mc == '210': self.navigate('2')
        elif mc == '211': 
            Client.display_clients()
            self.navigate('21')
        elif mc == '212': 
            Client.add_client()
            self.navigate('21')
        elif mc == '213': 
            Client.update_client()
            self.navigate('21')
        elif mc == '214': 
            Client.remove_client()
            self.navigate('21')
        elif mc == '22': self.display_project_menu()
        elif mc == '220': self.navigate('2')
        elif mc == '221': 
            Project.display_projects()
            self.navigate('22')
        elif mc == '222': 
            Project.display_client_projects()
            self.navigate('22')
        elif mc == '223': 
            Project.add_project()
            self.navigate('22')
        elif mc == '224': 
            Project.update_project()
            self.navigate('22')
        elif mc == '225': 
            Project.remove_project()
            self.navigate('22')
        elif mc == '4': self.display_banking()
        elif mc == '40': self.navigate('0')
        elif mc == '41': self.display_bank_menu()
        elif mc == '410': self.navigate('4')
        elif mc == '411': 
            BankAccount.display_accounts()
            self.navigate('41')
        elif mc == '412': 
            BankAccount.add_account()
            self.navigate('41')
        elif mc == '413': 
            BankAccount.update_account()
            self.navigate('41')
        elif mc == '414': 
            BankAccount.remove_account()
            self.navigate('41')
        

    def display_main_menu(self):
        print(f"+{'-'*80}+")
        print(f"|{'  1. Dashboard':<80}|")
        print(f"|{'  2. Freelance':<80}|")
        print(f"|{'  3. Spendings':<80}|")
        print(f"|{'  4. Banking':<80}|")
        print(f"|{'  x. Exit':<80}|")
        print(f"+{'-'*80}+")

        mc = input(">>> ")
        self.navigate(mc)

    def display_dashboard(self):
        pass

    def display_freelance(self):
        print(f"+{'-'*80}+")
        print(f"|{'  1. Clients':<80}|")
        print(f"|{'  2. Projects':<80}|")
        print(f"|{'  0. Back':<80}|")
        print(f"+{'-'*80}+")

        mc = input(">>> ")
        self.navigate('2'+mc)

    def display_banking(self):
        print(f"+{'-'*80}+")
        print(f"|{'  1. Bank Accounts':<80}|")
        print(f"|{'  2. Payments':<80}|")
        print(f"|{'  3. Transactions':<80}|")
        print(f"|{'  0. Back':<80}|")
        print(f"+{'-'*80}+")

        mc = input(">>> ")
        self.navigate('4'+mc)

    def display_client_menu(self):
        print(f"+{'-'*80}+")
        print(f"|{'  1. Show clients':<80}|")
        print(f"|{'  2. Add client':<80}|")
        print(f"|{'  3. Edit client':<80}|")
        print(f"|{'  4. Remove client':<80}|")
        print(f"|{'  0. Back':<80}|")
        print(f"+{'-'*80}+")

        mc = input(">>> ")
        self.navigate('21'+mc)

    def display_project_menu(self):
        print(f"+{'-'*80}+")
        print(f"|{'  1. Show projects':<80}|")
        print(f"|{'  2. Show client projects':<80}|")
        print(f"|{'  3. Add project':<80}|")
        print(f"|{'  4. Edit project':<80}|")
        print(f"|{'  5. Remove project':<80}|")
        print(f"|{'  0. Back':<80}|")
        print(f"+{'-'*80}+")

        mc = input(">>> ")
        self.navigate('22'+mc)

    def display_bank_menu(self):
        print(f"+{'-'*80}+")
        print(f"|{'  1. Show bank accounts':<80}|")
        print(f"|{'  2. Add bank account':<80}|")
        print(f"|{'  3. Edit bank account':<80}|")
        print(f"|{'  4. Remove bank account':<80}|")
        print(f"|{'  0. Back':<80}|")
        print(f"+{'-'*80}+")

        mc = input(">>> ")
        self.navigate('41'+mc)

            
    

if __name__ == "__main__":
    io_manager = IOManager()