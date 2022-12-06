from tinydb import TinyDB, Query
import json
from controllers import *
from models import *
from datetime import date, datetime

with open("C:/Users/start/Desktop/Shared/FUN/Python/Freelancer/public/data/projects.json") as f:
    df = json.load(f)
    clts = {}
    for k, v in df.items():
        kk = int(k.split('_')[1])
        clts[kk] = v
    
    for k in range(1, 136):
        if k not in clts.keys(): continue
        v = clts[k]
        client = int(v['client'].split('_')[1])
        curr = v['payments'][-1]['currency']
        comm = v['comment']
        desc = v['description']
        sd = v['start']
        dd = v['due']
        ed = v['end']
        # print(f"{client}: {sd}, {dd}, {ed}")
        # print(k, v)

        prj = ProjectModel(client)
        prj.comment = comm
        prj.description = desc
        prj.currency = Currency.decode("usd" if v['payments'][-1]['currency'] == "$" else "mad")
        prj.delivery_date = datetime.strptime(ed, "%d-%m-%Y").date()
        prj.due_date = datetime.strptime(dd, "%d-%m-%Y").date()

        s = 0
        for p in v['payments']:
            if p['method'] == 'Fiverr': s += p['paid'] * .8
            else: s += p['paid']

            ac = "FVRR"
            if p['method'] == "CIH": ac = "CIH"
            elif p['method'] == "PayPal": ac = "PYPL"
            elif p['method'] == "Fiverr": ac = "FVRR"
            acc = BankAccountController.search(ac, 'c')[0].id          
            pm = PaymentModel(prj.id, acc)
            pm.amount = p['paid'] if acc != 3 else p['recieved']
            pm.date = datetime.strptime(p['date'], "%d-%m-%Y").date()
            pm.currency = Currency.decode("usd" if p['currency'] == "$" else "mad")
            
            PaymentController.insert(pm)

        prj.price = s
        prj.state = ProjectState.decode("ongoing" if v['state'] == "started" else v['state'])
        prj.title = v['title']
        prj.start_date = datetime.strptime(sd, "%d-%m-%Y").date()

        ProjectController.insert(prj)