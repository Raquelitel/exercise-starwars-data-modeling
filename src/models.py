import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy import render_er

Base = declarative_base()

class User(Base):
    __tablename__= "user"
    id = Column(Integer, primary_key=True)
    name = Column(String(30), nullable=False)
    email = Column(String(60), nullable=False)
    password = Column(String(20), nullable= False)
    favorites = relationship('Favorites', backref='User', lazy=True)
   # is_active = Column(Boolean(), nullable=False) 

    def __repr__(self):
        return '<User %r>' % self.id

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "email": self.email,
            
            # do not serialize the password, its a security breach
        }

class Favorites(Base):
    __tablename__ = "favorites"
    id= Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("user.id"))
    people_id = Column(Integer, ForeignKey("people.id"))
    planet_id = Column(Integer, ForeignKey("planet.id"))


    def __repr__(self):
        return f"<Favorites id={self.id}>"
    
    def serialize(self):
        return {
            "id": self.id,
            "user_id": self.user_id,
            "user_name": self.user_name,
            "people_id": self.people_id,
            "people_name": self.people_name,
            "planet_id": self.planet_id,
            "planet_name": self.planet_name
        }

class People(Base):
    __tablename__ = 'people'
    id = Column(Integer, primary_key=True)
    name = Column(String(60), nullable=False)
    gender = Column(String(10))
    birthday_year = Column(String(10))
    color_eyes = Column(String(10))
    height = Column(String(5))
    mass = Column(String(5))
    favorites = relationship('Favorites', backref='People', lazy=True)


    def __repr__(self):
        return f"<People id={self.id} name= {self.name}>"

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "gender": self.gender,
            "birthday_year": self.birthday_year,
            "color_eyes": self.color_eyes,
            "height": self.height,
            "mass": self.mass

        }


class Planet(Base):
    __tablename__ = "planet"
    id = Column(Integer, primary_key=True)
    name = Column(String(60), nullable=False)
    gravity = Column(String(10))
    terrain = Column(String(10))
    diametrer = Column(String(10))
    rotation_period = Column(String(10))
    orbital_period = Column(String(10))
    favorites = relationship('Favorites', backref='Planet', lazy=True)

    def __repr__(self):
        return f"<Planet id={self.id} name= {self.name}"


    









## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')