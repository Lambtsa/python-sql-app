# import models file
from models import Base, session, Book, engine
# main menu - add, search, analysis, exit and view options
# add books to the database
# edit books
# delete books
# search function
# data cleaning
# loop running the program


if __name__ == '__main__':
    Base.metadata.create_all(engine)
