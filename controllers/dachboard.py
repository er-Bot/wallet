from controllers.payment import PaymentController
from controllers.bank_account import BankAccountController
from controllers.payment import PaymentController

class DashboardController:
    
    def count_profit_by_project(projects):
        s = 0
        for pr in projects:
            for py in PaymentController.search_by(pr.id, 'project'):
                if py.account == 3:
                    s += .8 * py.amount
                elif py.account == 2:
                    s += py.amount
                else:
                    s += .1 * py.amount
        return s


    def count_profit_by_account():
        l = {}
        for ac in BankAccountController.all():
            s = 0
            for py in PaymentController.search_by(ac.id, 'account'):
                s += py.amount
            l[ac.code] = {
                'total': s,
                'currency': ac.currency
            }
        return l

    # def count_profit_by_month(m, y):
    #     s = 0
    #     for py in PaymentController.search_by(ac.id, 'account'):
    #             s += py.amount
    #         l[ac.code] = {
    #             'total': s,
    #             'currency': ac.currency
    #         }