#!/usr/bin/python3
"""
Script that deletes all states with name containing a from database
"""


if __name__ == "__main__":
    from sys import argv
    from model_state import Base, State
    from sqlalchemy import create_engine
    from sqlalchemy.orm import sessionmaker

    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        argv[1], argv[2], argv[3]), pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()
    Base.metadata.create_all(engine)
    st = session.query(State).filter(State.name.like('%a%')).all()
    if st:
        for states in st:
            session.delete(states)
        session.commit()
    session.close()
