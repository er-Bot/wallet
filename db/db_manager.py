from tinydb import TinyDB, Query

class DBManager:
    db = TinyDB("db/db.json")
    query = Query()

    projects = db.table("Project")
    clients = db.table("Client")
    countries = db.table("Country")
    payments = db.table("Payment")
    bank_accounts = db.table("BankAccount")
    transactions = db.table("Transaction")
    spendings = db.table("Spending")

    def has(v, s):
        return s.lower() in v.lower()

    def list_has(v, s):
        for vv in v:
            if s in vv:
                return True
        return False


