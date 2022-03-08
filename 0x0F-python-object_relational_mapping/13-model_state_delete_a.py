#!/usr/bin/python3
"""
deletes all State objects with a name
containing the letter a from the database hbtn_0e_6_usa
"""

import sys
from venv import create
from sqlalchemy import create_engine, true
from sqlalchemy.orm import sessionmaker
from model_state import State

if __name__ == "__main__":
    engine = create_engine("mysql+mysqldb://{}:{}@localhost/{}".format(
        sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)
    session_maker = sessionmaker(bind=engine)
    session = session_maker()

    for state in session.query(State):
        if "a" in state.name:
            session.delete(state)
        session.commit()
