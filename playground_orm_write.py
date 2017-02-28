# -*- coding: utf-8 -*-

# ----------------------------------------------------------------------
# Getting Started
# ----------------------------------------------------------------------
from sqlalchemy import create_engine, Column, Integer, Unicode
from sqlalchemy.dialects.postgresql import JSONB


engine = create_engine("postgresql://postgres@127.0.0.1/flask_example", echo=True)

# Build the session maker (thread safe connections)
from sqlalchemy.orm import sessionmaker
session_factory = sessionmaker(bind=engine)
session = session_factory()

# ----------------------------------------------------------------------
# Formalizing into objects (a.k.a Declarative ORM)
# ----------------------------------------------------------------------
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.ext.mutable import MutableDict

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    first_name = Column(Unicode)
    last_name = Column(Unicode)
    data = Column(MutableDict.as_mutable(JSONB), default=MutableDict())

    def __unicode__(self):
        return u"User #{}".format(self.id)

    def __str__(self):
        return self.__unicode__().encode('utf8')

    def __repr__(self):
        return self.__str__()


# Create a new record - a.k.a INSERT
new_user = User(first_name=u"John", last_name=u"Doe")
session.add(new_user)

# Write to the database
session.flush()

# Make a change to the JSON  - a.k.a UPDATE
new_user.first_name = u"Jane"

# Write to the database
session.flush()

# Make a change to the JSON   - a.k.a UPDATE complex field
new_user.data[u"test_key"] = u"Something"

# Write to the database
session.flush()

# Delete the new user - a.k.a DELETE
session.delete(new_user)

# Write to the database
session.flush()


