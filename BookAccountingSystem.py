import os
from datetime import datetime, timedelta

from sqlalchemy import Column, Boolean, DateTime, String, Integer, func
from sqlalchemy import create_engine

from sqlalchemy.sql import text
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()


class User(Base):
    """ Represents the User table """
    __tablename__ = 'users'

    username = Column(String(32), primary_key=True)
    full_name = Column(String(32), nullable=False, index=True)
    create_time = Column(DateTime, default=datetime.utcnow)
    update_time = Column(DateTime, default=datetime.utcnow, index=True)


class Book(Base):
    """ Represents the Books table """
    __tablename__ = 'books'

    name = Column(String(32), primary_key=True, nullable=False)
    author = Column(String(32), primary_key=True, nullable=False)
    create_time = Column(DateTime, default=datetime.utcnow)


class Order(Base):
    """ Represents the Orders table """
    __tablename__ = 'orders'

    username = Column(String(128), primary_key=True, nullable=False)
    bookname = Column(String(32), primary_key=True, nullable=False)
    order_time = Column(DateTime, default=datetime.utcnow)
    expiry_period_in_days = Column(Integer, default=30)


class SQLiteBackend(object):
    """ The SQLite backend that manages database connections, sessions and bootstraping. """
    def __init__(self, db_string):
        self.engine = None
        self.Session = sessionmaker(
            autocommit=False,
            expire_on_commit=False
        )
        self.setup_session(db_string)

    def setup_session(self, db_string=None):
        """ Setup the engine and session. If the engine is already setup, then return. """
        if self.engine:
            return
        self.engine = create_engine(db_string, echo=False, pool_recycle=3600)
        self.Session.configure(bind=self.engine)

    def reset(self):
        """ Reset the entire database """
        Base.metadata.drop_all(bind=self.engine)
        Base.metadata.create_all(bind=self.engine)

    def ping(self):
        """ Check to see if a connection to the database is possible """
        session = self.Session()
        pong = session.execute('select 1').fetchall()
        session.close()
        return pong

    def bootstrap(self):
        """ Does bootstraping i.e. creates database and tables.
        Assumes no databases have been setup. Retries until connection is established. """
        connection = None
        for i in range(10):  # retries
            try:
                connection = self.engine.connect()
            except:
                print("DBServer is probably not up yet, Retrying ...")
                time.sleep(i * 5)
                continue
        if not connection:
            raise Exception("Couldn't connect to DBServer even after retries!")

        Base.metadata.create_all(bind=self.engine)
        connection.close()


class BookAccountingSystem(SQLiteBackend):
    """ This class keeps account of all users and books and the orders made for book requests. """
    def __init__(self, db_url):
        super(BookAccountingSystem, self).__init__(db_url)

    def reset(self):
        super(BookAccounting, self).reset()

    def create_user(self, username, full_name):
        """ Inserts a new user into the database. """
        user = User(username=username, full_name=full_name)
        session = self.Session()
        session.add(user)
        try:
            session.commit()
            return user
        except IntegrityError:
            session.rollback()
            raise Exception("User exists")
        finally:
            session.expunge_all()
            session.close()

    def get_user(self, username):
        session = self.Session()
        try:
            user = session.query(User).filter_by(username=username).first()
        except Exception as ex:
            print("Error getting user, error={}".format(str(ex)))
        finally:
            session.close()
        return user

    def create_author(self, name, author):
        """ Inserts a new book and auther into the database. """
        author = Book(name=name, author=author)
        session = self.Session()
        session.add(author)
        try:
            session.commit()
            return author
        except IntegrityError:
            session.rollback()
            raise Exception("Author exists")
        finally:
            session.expunge_all()
            session.close()

    def get_books_of_author(self, author):
        session = self.Session()
        try:
            books = session.query(Book).filter_by(name=author).first()
        except Exception as ex:
            print("Error getting book, error={}".format(str(ex)))
        finally:
            session.close()
        return books    

    def place_order(self, username, bookname):
        order = Order(username=username, bookname=bookname)
        session = self.Session()
        session.add(order)
        try:
            session.commit()
            return order
        except IntegrityError:
            session.rollback()
            raise Exception("Order already placed")
        finally:
            session.expunge_all()
            session.close()

    def get_orders_of_user(self, username):
        session = self.Session()
        try:
            orders = session.query(Order, User, Book).filter(Order.username == User.username).filter(Order.bookname == Book.name).filter(User.username == username)
            return orders
        except Exception as ex:
            print("Error getting order, error={}".format(str(ex)))
        finally:
            session.close()

    def get_orders_of_book(self, bookname):
        session = self.Session()
        try:
            orders = session.query(Order, User, Book).filter(Order.username == User.username).filter(Order.bookname == Book.name).filter(Book.name == bookname)
            return orders
        except Exception as ex:
            print("Error getting order, error={}".format(str(ex)))
        finally:
            session.close()

    def get_top_n_most_recent_orders(self, n):
        session = self.Session()
        try:
            recent_orders = session.query(Order).order_by(Order.order_time.desc()).limit(n).all()
            return recent_orders
        except Exception as ex:
            print("Error getting order, error={}".format(str(ex)))
        finally:
            session.close()
        
    def get_top_n_most_oldest_orders(self, n):
        session = self.Session()
        try:
            recent_orders = session.query(Order).order_by(Order.order_time.asc()).limit(n).all()
            return recent_orders
        except Exception as ex:
            print("Error getting order, error={}".format(str(ex)))
        finally:
            session.close()

    def get_orders_expired(self):
        session = self.Session()
        conn = session.connection()
        try:
            t = text("SELECT username, o.order_time, o.bookname, datetime(o.order_time,'+'||o.expiry_period_in_days||' days') AS ex FROM orders o WHERE ex < CURRENT_DATE;")
            result = conn.execute(t).fetchall()
            return result
        except Exception as ex:
            print("Error getting order, error={}".format(str(ex)))
        finally:
            session.close()

    def delete_book(self, book):
        session = self.Session()
        session.query(Book).filter_by(name=book).delete()
        try:
            session.commit()
        except IntegrityError:
            session.rollback()
            raise Exception("Delete not done")
        finally:
            session.expunge_all()
            session.close()

    def update_book_author(self, book, updated_book, updated_author):
        session = self.Session()
        update = session.query(Book).filter_by(name=book).first()
        update.name = updated_book
        update.author = updated_author
        try:
            session.commit()
            return update
        except IntegrityError:
            session.rollback()
            raise Exception("Update not done")
        finally:
            session.expunge_all()
            session.close()


### The Controller Program
def main():
    """ The user interface class which users will use to perform actions on the Book Accounting System. """
    print("Main program starting ...")
    # db_url = os.environ['DB_URL'] # getting the DB url \ $Env:DB_URL"sqlite:///new.db"
    db_url = "sqlite:///new.db" # Hard code - BD Name
    print("Connecting to DB={}".format(db_url)) 

    bas = BookAccountingSystem(db_url) # setting up the engine and session
    bas.bootstrap()
    if not bas.ping():
        raise Exception("Unable to ping the database!")
    print("Connected.")

    # Wait endlessly for input to perform actions
    welcome_message = """
    Welcome to the Book Accounting System. To interact with the system
    please press the following options:

    0. Quit
    1. Create user
    2. Get user
    3. Create author
    4. Books of author
    5. Place an Order
    6. Get orders of a user
    7. Get orders of a book
    8. Get top 3 recent orders
    9. Get top 3 oldest orders
    10. Get orders expired
    11. Delete book
    12. Update book

    Your Option:\t
    """

    option = int(input(welcome_message))
    print("\n\n")
    while option != 0:

        if option == 1:
            username = input("Enter username: ")
            full_name = input("Enter Full name: ")
            u = bas.create_user(username, full_name)
            print("\nUser has been created \nUser name: {} \nFull name: {}".format(u.username, u.full_name))

        elif option == 2:
            username = input("Enter username: ")
            u = bas.get_user(username)
            if u:
                print("\nUser name: {} \nFull name: {}".format(u.username, u.full_name))
            else:
                print("\nUser with username={} does not exist".format(username))
        
        elif option == 3:
            name = input("Enter book name: ")
            author = input("Enter author name: ")
            a = bas.create_author(name, author)
            print("\nBook has been enetered into the database \nBook name: {} \nAuthor name: {}".format(a.name, a.author))

        elif option == 4:
            book = input("Enter book's name: ")
            b = bas.get_books_of_author(book)
            if b:
                print("\nAuthor's name: {} \nBook' s name: {}".format(b.author, b.name))
            else:
                print("\nAuthor's with books {} does not exist".format(name))

        elif option == 5:
            username = input("Enter username: ")
            bookname = input("Enter book name: ")
            o = bas.place_order(username, bookname)
            print("\nUser name: {} \nBook ordered: {}".format(o.username, o.bookname))
            
        elif option == 6:
            username = input("Enter username: ")
            order = bas.get_orders_of_user(username)
            for o, u, b in order:
                print("Full name: {} \nAuthor's book: {} \nOrdered time: {}".format(u.full_name, b.author, o.order_time))

        elif option == 7:
            bookname = input("Enter book name: ")
            order = bas.get_orders_of_book(bookname)
            for o, u, b in order:
                print("Full name: {} \nBook ordered: {} \nDate & Time of Order: {}".format(u.full_name, b.author, o.order_time))

        elif option == 8:
            display_orders = int(input("Display number of recent orders: "))
            recent_order = bas.get_top_n_most_recent_orders(display_orders)
            for o in recent_order:
                print("\nMost recenet orders: \nUser name: {} \nBook name: {} \nOrder time: {}".format(o.username, o.bookname, o.order_time))

        elif option == 9:
            display_orders = int(input("Display number of recent orders: "))
            recent_order = bas.get_top_n_most_oldest_orders(display_orders)
            for o in recent_order:
                print("\nMost recenet orders: \nUser name: {} \nBook name: {} \nOrder time: {}".format(o.username, o.bookname, o.order_time))

        elif option == 10:
            exp = bas.get_orders_expired()
            if exp:
                for ex in exp:
                    print("\nUser name: {} \nOrdered date & time: {} \n Book name: {} \nExpired date & time: {}".format(ex.username, ex.order_time, ex.bookname, ex.ex))
            else:
                print("No orders are expired yet")

        elif option == 11:
            name = input("Delete book name: ")
            d = bas.delete_book(name)
            print("\nBook deleted: {} ".format(name))

        elif option == 12:
            name = input("Enter book name: ")
            update_name = input("Update book name: ")
            update_author = input("Update author name: ")
            u = bas.update_book_author(name, update_name, update_author)
            print("\nBook name={} and author={} have been updated".format(u.name, u.author))

        option = int(input("\nYour option: "))

### Start the main program
main()

#orders can be updated but did not get updated in the orders table.