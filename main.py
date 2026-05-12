from peewee import *
dtbs = SqliteDatabase('data/tsks.db')

class Task(Model):
    tl = CharField()
    class Meta:
        database = dtbs


dtbs.connect()
dtbs.create_tables([Task])

def addtsk(nm):
    try:
        Task.create(tl=nm)
        return 1
    except:
        return 0

def gettsks():
    if len(list(Task.select())) != 0:
        return list(Task.select())
    else: return 2

def dlttsk(tskid):
    dltcnt = Task.delete().where(Task.id == tskid).execute()
    if dltcnt !=0 : return 1
    return 0
print("допустимые команды: add; viewlist; delete; C. БЕЗ ПРОБЕЛОВ")
if __name__ == "__main__":
    while 1:
        cmd = input("ввод команды: ")
        if cmd == 'add':
            name = input("имя задачи: ")
            addtsk(name)
        elif cmd == 'viewlist' and gettsks()!=2:
            tasks = gettsks()
            for t in tasks:
                print(f"id: {t.id} titlegit: {t.tl}")
        elif cmd == 'viewlist': print(f"код ошибки: {gettsks()}. Задач нет")
        elif cmd == 'delete':
            tid = input("задачу под каким id требуется удалить: ")
            if tid.isdigit():
                dlttsk(int(tid))
        elif cmd == 'C':
            break