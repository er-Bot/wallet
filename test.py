from tinydb import TinyDB, Query
import json

db = TinyDB("db/db.json")

cntr = db.table("Clietn")

with open("C:/Users/start/Desktop/Shared/FUN/Python/Freelancer/public/data/countries.json") as f:
    df = json.load(f)

    for k, v in df.items():
        cntr.insert({'name': v['name'], 'code': v['code'], 'dial': v['dial-code']})