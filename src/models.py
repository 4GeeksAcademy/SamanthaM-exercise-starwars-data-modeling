from __future__ import annotations

import os
import sys
from typing import List
from sqlalchemy import Column, ForeignKey, Integer, String, Float, Table
from sqlalchemy.orm import relationship, declarative_base, Mapped
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()


#favorites
user_character_favorite = Table(
    "user_character_favorite",
    Base.metadata,

    Column("user_id", ForeignKey("User.id"), primary_key=True),
    Column("character_id", ForeignKey("Character.id"), primary_key=True),
)

user_planet_favorite = Table(
    "user_planet_favorite",
    Base.metadata,

    Column("user_id", ForeignKey("User.id"), primary_key=True),
    Column("planet_id", ForeignKey("Planet.id"), primary_key=True),
)

user_vehicle_favorite = Table(
    "user_vehicle_favorite",
    Base.metadata,

    Column("user_id", ForeignKey("User.id"), primary_key=True),
    Column("vehicle_id", ForeignKey("Vehicle.id"), primary_key=True),
)


#users
class User (Base):
    __tablename__ = "User"

    ID = Column(Integer, primary_key=True)
    email = Column(String, nullable=False)
    password = Column(String, nullable=False)
    character_favorites: Mapped[List[Planet]] = relationship("Character", secondary=user_character_favorite)
    planet_favorites: Mapped[List[Planet]] = relationship("Planet", secondary=user_planet_favorite)
    vehicle_favorites: Mapped[List[Planet]] = relationship("Vehicle", secondary=user_vehicle_favorite)


#characters
class Character(Base):
    __tablename__ = "Character"

    ID = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    gender = Column(String, nullable=False)
    hair_color = Column(String, nullable=False)
    eye_color = Column(String, nullable=False)
    homeworld = Column(String, nullable=False)
    character_favorites: Mapped[List[User]] = relationship("Character", secondary=user_character_favorite)


#planets
class Planet(Base):
    __tablename__ = "Planet"

    ID = Column(Integer, primary_key=True)
    population = Column(Integer, nullable=False)
    climate = Column(String, nullable=False)
    surface_water_percentage = Column(String, nullable=False)
    radius = Column(Float, nullable=False)
    gravity = Column(Float, nullable=False)
    planet_favorites: Mapped[List[User]] = relationship("Planet", secondary=user_planet_favorite)


#vehicles
class Vehicle(Base):
    __tablename__ = "Vehicle"

    ID = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    cost_in_credits = Column(Integer, nullable=False)
    length_in_meters = Column(Float, nullable=False)
    passenger_capacity = Column(Integer, nullable=False)
    vehicle_favorites: Mapped[List[User]] = relationship("Vehicle", secondary=user_vehicle_favorite)



    ## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
