#!/usr/bin/python3
"""This module list all the States objects, and corresponding City object,
contained in the database passed as argument"""


if __name__ == "__main__":
    from relationship_city import City
    from relationship_state import Base, State
    from sys import argv
    from sqlalchemy import create_engine
    from sqlalchemy.orm import sessionmaker, joinedload

    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        argv[1], argv[2], argv[3], pool_pre_ping=True
    ))
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    cities = session.query(City).all()
    for city in cities:
        print("{:d}: {:s} -> {:s}".format(city.id, city.name, city.state.name))
    session.close()
