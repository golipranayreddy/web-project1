import csv
import os

# from sqlalchemy import create_engine
# from sqlalchemy.orm import scoped_session, sessionmaker

# engine = create_engine(os.getenv("DATABASE_URL"))
# //db = scoped_session(sessionmaker(bind = engine))

def main():
    f = open("users.csv")
    reader = csv.reader(f)
    for name, username, mail_id in reader:
        # db.execute("INSERT INTO flights (name, username, mail_id) VALUES (:name, :username, :mail_id)
        #            {"name": name, "username": username, "mail_id": mail_id })
        print(f" added user where name = {name} and username = {username} and mail_id = {mail_id}")
    # db.commit()

if __name__ == "__main__":
    main()