import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

# NEED TO DECLARE __repr__ AND __serialize functions

class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    name = Column(Integer, nullable=False)
    display_name = Column(String(50), nullable=False)
    email = Column(String(250), nullable=False)
    password = Column(String(100), nullable=False)
    avatar = Column(String(250), nullable=True)

# THIS NEED TO BE A SINGLE CLASS
# class User_Like_Planets(Base):
#     __tablename__ = "user_like_planets"
#     id = Column(Integer, primary_key=True)
#     user_id = Column(Integer, ForeignKey("user.id"))
#     user = relationship(User)
#     planet_id = Column(Integer, ForeignKey("planet.id"))
#     planet = relationship(User)

# class User_Like_Character(Base):
#     __tablename__ = "user_like_character"
#     id = Column(Integer, primary_key=True)
#     user_id = Column(Integer, ForeignKey("user.id"))
#     user = relationship(User)
#     character_id = Column(Integer, ForeignKey("character.id"))
#     character = relationship(User)

class Planet(Base):
    __tablename__ = 'planet'
    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)
    rotation_period = Column(String(50), nullable=True)
    diameter = Column(String(50), nullable=True)
    terrain = Column(String(50), nullable=True)
    population = Column(String(50), nullable=True)
    image = Column(String(200), nullable=True)


class Character(Base):
    __tablename__ = "character"
    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)
    height = Column(String(50), nullable=True)
    hair_color = Column(String(50), nullable=True)
    eye_color = Column(String(20), nullable=True)
    birth_year = Column(String(20), nullable=True)
    gender =Column(String(50), nullable=True)
    homeworld = Column(String(50), ForeignKey("planet.id"))
    homeworld = relationship(Planet)



    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')