# interact_with_database.py

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy import inspect  
from sqlalchemy_utils import database_exists, create_database
from models import Base, Person, Face, Image

# Initialize Database Connection
engine = create_engine('sqlite:///database.db')
if not database_exists(engine.url):
    create_database(engine.url)

Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()

# Function to show tables
def show_tables():
    inspector = inspect(engine)
    tables = inspector.get_table_names()
    print("Tables in the database:")
    for table in tables:
        print(table)
        # Function to create tables
def create_all_tables():
    Base.metadata.create_all(engine)
    print("Tables created successfully.")
create_all_tables()

# Call the show_tables function
show_tables()


# Add New Person
new_person = Person(name='charity', age=30)
session.add(new_person)
session.commit()

# Add New Face
person = session.query(Person).filter_by(id=1).first()
new_face = Face(encoding='encoded_face_data', person=person)
session.add(new_face)
session.commit()

# Add New Image
new_image = Image(url='https://example.com/image.jpg', timestamp='2022-03-17 12:00:00')
session.add(new_image)
session.commit()

# Query Persons
persons = session.query(Person).all()
for person in persons:
    print(person)

# Query Faces
faces = session.query(Face).all()
for face in faces:
    print(face)

# Query Images
images = session.query(Image).all()
for image in images:
    print(image)
