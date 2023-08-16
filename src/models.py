import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class FavoritesPerson(Base):
    __tablename__ = 'favoritesperson'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'))
    person_id = Column(Integer, ForeignKey('person.id'))
    rating = Column(Integer, nullable = True) 

class FavoritesPlanet(Base):
      __tablename__ = 'favoritesplanet'
      id = Column(Integer, primary_key=True)
      user_id = Column(Integer, ForeignKey('user.id'))
      planet_id = Column(Integer, ForeignKey('planet.id'))

class FavoritesVehicles(Base):
     __tablename__ = 'favoritesvehicles'
     id = Column(Integer, primary_key=True)
     user_id = Column(Integer, ForeignKey('user.id'))
     vehicles_id = Column(Integer, ForeignKey('vehicles.id'))



class Person(Base):
    __tablename__ = 'person'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    gender = Column(String(20), nullable=False)
    eyes_color = Column(String(20), nullable = True) #nullable = True es que se puede dejar vacía la información
    age = Column(Integer, nullable = False)
    favorites_person = relationship(FavoritesPerson, backref='person', lazy=True) #backref es una autoreferencia

class Planets(Base):
    __tablename__ = 'planet'
    id = Column(Integer, primary_key=True)
    name = Column(String(200), nullable = False)
    rotation_period = Column(String(200), nullable = True)
    orbital_period = Column(String(200), nullable = True)
    population = Column(Integer, nullable = False)
    terrain = Column(Integer, nullable = False)
    climate = Column(String(250), nullable = False)
    favorites_planet = relationship(FavoritesPlanet, backref='user', lazy=True)

class Vehicles(Base):
    __tablename__ = 'vehicles'
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable = False)
    model = Column(String(250), nullable = False)
    length = Column(String(250), nullable = True)
    cargo_capacity = Column(String(250), nullable = True)
    favorites_vehicles = relationship(FavoritesVehicles, backref='user', lazy=True)


class User(Base):
    __tablename__ = 'user'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    last_name = Column(String(250), nullable=False)
    email = Column(String(100), nullable=False)
    username = Column(String(100), nullable=False)
    age = Column(Integer, nullable = False)
    favorites_person = relationship(FavoritesPerson, backref='user', lazy=True)
    favorites_planet = relationship(FavoritesPlanet, backref='user', lazy=True)
    favorites_vehicles = relationship(FavoritesVehicles, backref='user',lazy=True)

    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
