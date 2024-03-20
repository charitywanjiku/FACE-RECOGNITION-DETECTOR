# models.py

from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, Table
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship

Base = declarative_base()

class Person(Base):
    __tablename__ = 'persons'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    age = Column(Integer, nullable=False)
    faces = relationship("Face", back_populates="person")

    def __repr__(self):
        return f"<Person(name='{self.name}', age={self.age})>"

class Face(Base):
    __tablename__ = 'faces'
    id = Column(Integer, primary_key=True)
    encoding = Column(String, nullable=False)
    person_id = Column(Integer, ForeignKey('persons.id'))
    person = relationship("Person", back_populates="faces")
    images = relationship("Image", secondary="faces_images")

    def __repr__(self):
        return f"<Face(id={self.id}, person_id={self.person_id})>"

class Image(Base):
    __tablename__ = 'images'
    id = Column(Integer, primary_key=True)
    url = Column(String, nullable=False)
    timestamp = Column(String, nullable=False)

    def __repr__(self):
        return f"<Image(id={self.id}, url='{self.url}', timestamp='{self.timestamp}')>"

faces_images = Table('faces_images', Base.metadata,
    Column('face_id', Integer, ForeignKey('faces.id')),
    Column('image_id', Integer, ForeignKey('images.id'))
)
