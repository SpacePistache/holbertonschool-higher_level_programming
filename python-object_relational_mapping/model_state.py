#!/usr/bin/python3
"""
Defines a State class and an instance of Base for SQLAlchemy ORM.
"""

from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class State(Base):
    """
    Represents a state in a MySQL database.
    
    Attributes:
        id (int): Auto-generated primary key.
        name (str): Name of the state, with max length of 128 characters.
    """
    __tablename__ = 'states'
    
    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    name = Column(String(128), nullable=False)