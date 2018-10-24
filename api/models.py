from sqlalchemy import (
    Column, String, ForeignKey, Integer
    )
from sqlalchemy.orm import relationship
from helpers.database import Base
from helpers.utility import Utility

class Category(Base, Utility):
    __tablename__ = "categories"
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    description = Column(String, nullable=True)
    products = relationship('Product', cascade="all, delete-orphan")    

class Product(Base, Utility):
    __tablename__ = "products"
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    description = Column(String, nullable=False)
    desplay_image = Column(String, nullable=False)
    category_id = Column(Integer, ForeignKey('categories.id'))
    price = Column(Integer, nullable=False)