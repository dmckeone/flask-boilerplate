# -*- coding: utf-8 -*-

# ----------------------------------------------------------------------
# Getting Started
# ----------------------------------------------------------------------
from sqlalchemy import create_engine, Column, Integer, Unicode, select
from sqlalchemy.dialects.postgresql import JSONB

engine = create_engine("postgresql://postgres@127.0.0.1/flask_example", echo=True)

conn = engine.connect()

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
        return u"User #{}".format(self.id)

    def __str__(self):
        return self.__unicode__().encode('utf8')

    def __repr__(self):
        return self.__str__()


# Boil down to Core select
select_query = User.__table__.select()

# Fetch all
result_proxy = conn.execute(select_query)
print 'All Declarative Schema __table__', result_proxy.fetchall()

# Fetch one
result_proxy = conn.execute(select_query)
print 'One Declarative Schema __table__', result_proxy.fetchone()


# Alternate syntax for Core select
select_query = select([User])

# Fetch all
result_proxy = conn.execute(select_query)
print 'All Declarative Schema select()', result_proxy.fetchall()

# Fetch one
result_proxy = conn.execute(select_query)
print 'One Declarative Schema select()', result_proxy.fetchone()