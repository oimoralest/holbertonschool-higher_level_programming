#!/usr/bin/python3
"""This module makes a query from MySQL"""


if __name__ == "__main__":
    from sqlalchemy import create_engine, text
    from sqlalchemy.orm import sessionmaker
    from sys import argv
    from model_state import State, Base
    from model_city import City
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        argv[1], argv[2], argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    query = session.query(State, City).filter(City.state_id == State.id)\
                                      .order_by(City.id).all()
    for state, city in query:
        print("{:s}: ({:d}) {:s}".format(state.name, city.id, city.name))
    session.close()
