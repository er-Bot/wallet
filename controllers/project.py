from db.db_manager import DBManager

class ProjectController:
    db = DBManager()

    def display_projects():
        projects = Project.db.projects.all()
        if len(projects) == 0:
            print(f"+{'-'*80}+")
            print(f"|{'  No Projects Found!':<80}|")
            print(f"+{'-'*80}+")
            return

        print(f"+{'-'*80}+")
        for project in Project.db.projects.all():
            pid, cid, state = project['id'], project['client_id'], project['state']
            strd, dued, deld = project['start_date'], project['due_date'], project['delivery_date']
            price, curr = project['price'], project['currency']
            title, desc, comm = project['title'], project['description'], project['comment']

            print(f"|{f'  Project [PRJ{pid:04d}] (CLT{cid:04d})':<80}|")
            print(f"|{f'   +- Title         : {title}':<80}|")
            print(f"|{f'   +- Desription    : {desc}':<80}|")
            print(f"|{f'   +- Comment       : {comm}':<80}|")
            print(f"|{f'   +- State         : {state}':<80}|")
            print(f"|{f'   +- Start Date    : {strd}':<80}|")
            print(f"|{f'   +- Due Date      : {dued}':<80}|")
            print(f"|{f'   +- Delivery Date : {deld}':<80}|")
            print(f"|{f'   +- Price         : {price}':<80}|")
            print(f"|{f'   +- Currency      : {curr}':<80}|")
            print(f"+{'-'*80}+")

    def display_client_projects():
        cid = int(input('Client ID: '))
        projects = Project.db.projects.search(Project.query.client_id == cid)
        if len(projects) == 0:
            print(f"+{'-'*80}+")
            print(f"|{'  No Projects Found!':<80}|")
            print(f"+{'-'*80}+")
            return

        print(f"+{'-'*80}+")
        for project in Project.db.projects.all():
            pid, cid, state = project['id'], project['client_id'], project['state']
            strd, dued, deld = project['start_date'], project['due_date'], project['delivery_date']
            price, curr = project['price'], project['currency']
            title, desc, comm = project['title'], project['description'], project['comment']

            print(f"|{f'  Project [PRJ{pid:04d}] (CLT{cid:04d})':<80}|")
            print(f"|{f'   +- Title         : {title}':<80}|")
            print(f"|{f'   +- Desription    : {desc}':<80}|")
            print(f"|{f'   +- Comment       : {comm}':<80}|")
            print(f"|{f'   +- State         : {state}':<80}|")
            print(f"|{f'   +- Start Date    : {strd}':<80}|")
            print(f"|{f'   +- Due Date      : {dued}':<80}|")
            print(f"|{f'   +- Delivery Date : {deld}':<80}|")
            print(f"|{f'   +- Price         : {price}':<80}|")
            print(f"|{f'   +- Currency      : {curr}':<80}|")
            print(f"+{'-'*80}+")

    def add_project():
        pid     = int(input("ID          : "))
        cid     = int(input("Client ID   : "))
        title   = input("Title       : ")
        price   = float(input("Price       : "))
        curreny = input("Currency    : ")
        startd  = input("Start Date  : ")
        dued    = input("Due Date    : ")
        desc    = input("Description : ")
        
        Project.db.projects.insert({
            'id': pid,
            'client_id': cid,
            'state': 'started',
            'start_date': startd,
            'due_date': dued,
            'delivery_date': None,
            'price': price,
            'currency': curreny,
            'title': title,
            'description': desc,
            'comment': ''
        })

    def update_project():
        pid = int(input("ID : "))

        print(f"+{'-'*80}+")
        print(f"|{f'  Project [PRJ{pid:04d}]':<80}|")
        print(f"|{f'   1. Update Title':<80}|")
        print(f"|{f'   2. Update Description':<80}|")
        print(f"|{f'   3. Update Comment':<80}|")
        print(f"|{f'   4. Update State':<80}|")
        print(f"|{f'   5. Update Start Date':<80}|")
        print(f"|{f'   6. Update Due Date':<80}|")
        print(f"|{f'   7. Update Delivery Date':<80}|")
        print(f"|{f'   8. Update Price':<80}|")
        print(f"|{f'   9. Update Currency':<80}|")
        print(f"+{'-'*80}+")

        cm = input('>>> ')
        if cm == '1':
            inp = input("Title : ")
            Project.db.projects.update({'title': inp}, Project.query.id == pid)
        if cm == '2':
            inp = input("Description : ")
            Project.db.projects.update({'description': inp}, Project.query.id == pid)
        if cm == '3':
            inp = input("Comment : ")
            Project.db.projects.update({'comment': inp}, Project.query.id == pid)
        if cm == '4':
            inp = input("State : ")
            Project.db.projects.update({'state': inp}, Project.query.id == pid)
        if cm == '5':
            inp = input("Start Date : ")
            Project.db.projects.update({'start_date': inp}, Project.query.id == pid)
        if cm == '6':
            inp = input("Due Date : ")
            Project.db.projects.update({'due_date': inp}, Project.query.id == pid)
        if cm == '7':
            inp = input("DElivery Date : ")
            Project.db.projects.update({'delivery_date': inp}, Project.query.id == pid)
        if cm == '8':
            inp = float(input("Price : "))
            Project.db.projects.update({'price': inp}, Project.query.id == pid)
        if cm == '9':
            inp = input("Currency : ")
            Project.db.projects.update({'currency': inp}, Project.query.id == pid)

    def remove_project():
        pid = int(input("ID : "))
        Project.db.projects.remove(Project.query.id == pid)
