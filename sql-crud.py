from sqlalchemy import (
    create_engine, Column, Integer, String,  
)


#from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, declarative_base

# Create a connection to the database
db = create_engine("postgresql:///chinook")  #/// indicate the default database hosted locally
Base = declarative_base()

# create a class-based model for the "Programmer" table
class Programmer(Base):
    __tablename__ = 'Programmer'
    id = Column(Integer, primary_key=True)
    first_name = Column(String)
    last_name = Column(String)
    gender = Column(String)
    nationality = Column(String)
    famous_for = Column(String)



# instead of connecting to the databse we are creating a session
# create a new instance of sessionmaker, then point it to the engine (the db)
Session = sessionmaker(bind=db)
#opens an actual session by calling the Session() subclass defined above
session = Session()

# create the database using declarative_base subclass
Base.metadata.create_all(db)

# creating records on our Programmer table
ada_lovelace = Programmer(
    first_name='Ada',
    last_name = 'Lovelace',
    gender = 'F',
    nationality = 'British',
    famous_for = 'First Programmer'
)

alan_turing = Programmer(
    first_name='Alan',
    last_name = 'Turing',
    gender = 'M',
    nationality = 'British',
    famous_for = 'Modern Computing'
)

grace_hopper = Programmer(
    first_name='Grace',
    last_name='Hopper',
    gender='F',
    nationality='American',
    famous_for='COBOL Language'
)

margaret_hamilton = Programmer(
    first_name='Margaret',
    last_name='Hamilton',
    gender='F',
    nationality='American',
    famous_for='Apollo 11'
)

bill_gates = Programmer(
    first_name='Bill',
    last_name='Gates',
    gender='M',
    nationality='American',
    famous_for='Microsoft'
)

time_burners_lee = Programmer(
    first_name='Tim',
    last_name='Burners-Lee',
    gender='M',
    nationality='British',
    famous_for='World Wide Web'
)

Chien_Chou_Chen = Programmer(
    first_name='Chien-Chou',
    last_name='Chen',
    gender='M',
    nationality='Taiwanese',
    famous_for='Python'
)



# add the record to the session object
#session.add(ada_lovelace)
#session.add(alan_turing)
#session.add(grace_hopper)
#session.add(margaret_hamilton)
#session.add(bill_gates)
#session.add(time_burners_lee)
#session.add(Chien_Chou_Chen)


# commit the record to the database
#session.commit()

# programmer = session.query(Programmer).filter_by(id=14).first()
# programmer.famous_for = 'World President'

# updating multiple records
# people = session.query(Programmer)
# for person in people:
#     if person.gender == 'F':
#         person.gender = "Female"
#     elif person.gender == 'M':
#         person.gender = "Male"
#     else:
#         print("Gender not defined")

# session.commit()

# delete a record
fname = input("Enter first name: ")
lname = input("Enter last name: ")
programmer = session.query(Programmer).filter_by(first_name=fname, last_name=lname).first()
#defensive programming
if programmer is not None:
    print("Programmer found: ", programmer.first_name + " " + programmer.last_name)
    confirmation = input("Are you sure you want to delete this record? (y/n): ") 
    if confirmation.lower() == 'y':
        session.delete(programmer)
        session.commit()
        print("Programmer has been deleted")
    else:
        print("Programmer not deleted")
        
else:
    print("No record found")
    
# query the database
programmers = session.query(Programmer)
for programmer in programmers:
    print(
        programmer.id,
        programmer.first_name + " " + programmer.last_name,
        programmer.gender,
        programmer.nationality,
        programmer.famous_for,
        sep=" | "
    )