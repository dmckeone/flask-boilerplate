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

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    first_name = Column(Unicode)
    last_name = Column(Unicode)
    data = Column(JSONB)

    def __unicode__(self):
        return u"User #{} - {} {}".format(self.id, self.first_name, self.last_name)

    def __str__(self):
        return self.__unicode__().encode('utf8')

    def __repr__(self):
        return self.__str__()


# ----------------------------------------------------------------------
# Execute
# ----------------------------------------------------------------------
# Fetch all
print 'All Declarative Schema Session All', session.query(User).all()

# Fetch first
print 'One Declarative Schema Session First', session.query(User).first()


# ----------------------------------------------------------------------
# Queries
# ----------------------------------------------------------------------
# Fetch a single unique ID
print 'ID #1', session.query(User).get(1)

# All Davids
print 'All Kurts', session.query(User).filter(User.first_name == u'Kurt').all()
