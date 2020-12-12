#!/usr/bin/python3
"""This module ceates the state California with the City San Francisco in
the database passed as argument"""


if __name__ == "__main__":
    from relationship_city import City
    from relationship_state import Base, State
    from sys import argv
    from sqlalchemy import create_engine
    from sqlalchemy.orm import sessionmaker

    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        argv[1], argv[2], argv[3], pool_pre_ping=True
    ))
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    newState = State(name="California")
    newCity = City(name="San Francisco")
    newState.cities = [newCity]
    session.add(newState)
    session.commit()
    session.close()
