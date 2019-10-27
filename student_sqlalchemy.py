from sqlalchemy import create_engine, MetaData, Integer, String, Table, Column


engine = create_engine("sqlite:///student.db", echo = True)
""" 
Create a database named student.db and connect python to sql via the engine.
Create a table named student which has the columns id and name and store it in the meta.
"""

meta = MetaData()
student = Table('student', 
                meta,
                Column('id', Integer, primary_key = True),
                Column('first_name', String)
                )

conn = engine.connect()
meta.create_all(engine)


def main(command):
    """
    Create a function that will have the commands insert, select, update, delete and quit.
    User can select any function to perform an action.
    1 = insert, 2 = select, 3 = update, 4 = delete, 5 = quit
    """
    case = {
        1 : insert,
        2 : select,
        3 : update,
        4 : delete
        }
    db_func = case.get(command)

    while command != 5:
        db_func()
        print("1 = Insert, 2 = Select, 3 = Update, 4 = Delete, 5 = Quit")
        command = int(input("Input new command: "))
        db_func = case.get(command)
    else:
        print("End")
    

def insert():
    insert_id = int(input("Insert id: "))
    insert_first_name = str(input("Insert name: "))
    insert_record = student.insert().values(id = insert_id, first_name = insert_first_name)
    conn.execute(insert_record)


def select():
    select_id = int(input("Select id: "))
    select_record = student.select().where(student.c.id == select_id)
    result = conn.execute(select_record)
    for row in result:
        print(row)


def update():
    update_id = int(input("Update id: "))
    update_first_name = str(input("Enter new first name: "))
    update_record = student.update().where(student.c.id == update_id).values(first_name = update_first_name)
    conn.execute(update_record)


def delete():
    delete_id = int(input("Delete id: "))
    delete_record = student.delete().where(student.c.id == delete_id)
    conn.execute(delete_record)


print("1 = Insert, 2 = Select, 3 = Update, 4 = Delete, 5 = Quit")
command = int(input("Input command: "))
main(command)