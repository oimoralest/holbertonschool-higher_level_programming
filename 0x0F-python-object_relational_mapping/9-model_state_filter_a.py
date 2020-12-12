#!/usr/bin/python3
"""This module makes a query to MySQL"""


if __name__ == "__main__":
    from sqlalchemy import create_engine, text
    from sqlalchemy.orm import sessionmaker
    from sys import argv
    from model_state import State, Base
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        argv[1], argv[2], argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    rows = session.query(State.id, State.name).from_statement(text(
        "SELECT id, name "
        "FROM states "
        "WHERE name REGEXP '^.*a.*' "
    )).all()
    for id, name in rows:
        print("{:d}: {:s}".format(id, name))
    session.close()
