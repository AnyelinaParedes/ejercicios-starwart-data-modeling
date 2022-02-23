import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    email = Column(String(250), nullable=False)
    pasaword = Column(String(250), nullable=False)

class Species(Base):
    __tablename__ = 'species'
    id = Column(Integer, primary_key=True)
    name = Column(String(250))
    clasificaction= Column(String(250))
    language = Column(String(250), nullable=False)
    eye_color = Column(String(250), nullable=False)

class Vehicles(Base):
    __tablename__ = 'vehicles'
    id = Column(Integer, primary_key=True)
    name = Column(String(250))
    model= Column(String(250))
    passenger = Column(String(250), nullable=False)
    
class People(Base):
    __tablename__ = 'people'
    id = Column(Integer, primary_key=True)
    name = Column(String(250))
    height= Column(String(250))
    skin_color = Column(String(250), nullable=False)
    gender= Column(String(250), nullable=False)
    
class Starships(Base):
    __tablename__ = 'starships'
    id = Column(Integer, primary_key=True)
    model = Column(String(250))
    cargo_capacity= Column(String(250))
    hyperdrive_rating = Column(String(250), nullable=False)
    manufacturer= Column(String(250), nullable=False)
    
class UserFavoritesSpecies(Base):
    __tablename__ = 'userFavoritesSpecies'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'))
    user = relationship('User')
    species_id = Column(Integer, ForeignKey('species.id'))
    species = relationship('Species')

class UserFavoritesVehicles(Base):
    __tablename__ = 'userFavoritesVehicles'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'))
    user = relationship('User')
    vehicles_id = Column(Integer, ForeignKey('vehicles.id'))
    vehicles = relationship('Vehicles')

class UserFavoritesPeople(Base):
    __tablename__ = 'userFavoritesPeople'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'))
    user = relationship('User')
    people_id = Column(Integer, ForeignKey('people.id'))
    people = relationship('People')

class UserFavoritesStarships(Base):
    __tablename__ = 'userFavoritesStarships'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'))
    user = relationship('User')
    starships_id = Column(Integer, ForeignKey('starships.id'))
    starships = relationship('Starships')

    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')