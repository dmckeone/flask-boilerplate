# -*- coding: utf-8 -*-

# ----------------------------------------------------------------------
# Getting Started
# ----------------------------------------------------------------------
from sqlalchemy import create_engine, select

engine = create_engine("postgresql://postgres@127.0.0.1/flask_example", echo=True)
conn = engine.connect()


# ----------------------------------------------------------------------
# Formalizing
# ----------------------------------------------------------------------
# More imports!
from sqlalchemy import MetaData, Table, Integer, Column, Unicode
from sqlalchemy.dialects.postgresql import JSONB

metadata = MetaData()

user_table = Table(
    'users',
    metadata,
    Column('id', Integer, primary_key=True),
    Column('first_name', Unicode),
    Column('last_name', Unicode),
    Column('data', JSONB)
)

select_query = user_table.select()

# Fetch all
result_proxy = conn.execute(select_query)
print 'All Schema', result_proxy.fetchall()

# Fetch one
result_proxy = conn.execute(select_query)
print 'One Schema', result_proxy.fetchone()
