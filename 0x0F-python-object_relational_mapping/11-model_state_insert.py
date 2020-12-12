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
    newState = State(name="Louisiana")
    session.add(newState)
    session.commit()
    print(newState.id)
    session.close()
