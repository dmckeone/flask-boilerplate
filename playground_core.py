# -*- coding: utf-8 -*-

# ----------------------------------------------------------------------
# Getting Started
# ----------------------------------------------------------------------
from sqlalchemy import create_engine, select

engine = create_engine("postgresql://postgres@127.0.0.1/flask_example", echo=True)

conn = engine.connect()

select_query = select([1])

# Fetch all
result_proxy = conn.execute(select_query)
print 'All', result_proxy.fetchall()

# Fetch one
result_proxy = conn.execute(select_query)
print 'One', result_proxy.fetchone()

# Fetch scalar
result_proxy = conn.execute(select_query)
print 'Scalar', result_proxy.scalar()


# ----------------------------------------------------------------------
# SELECTing directly
# ----------------------------------------------------------------------
result_proxy = conn.execute("SELECT id, first_name, last_name FROM users")
print 'All', result_proxy.fetchall()

result_proxy = conn.execute("SELECT id, first_name, last_name FROM users")
print 'One', result_proxy.fetchone()


# ----------------------------------------------------------------------
# SELECTing directly with WHERE clause
# ----------------------------------------------------------------------
result_proxy = conn.execute("SELECT id, first_name, last_name FROM users WHERE first_name = 'David'")
print 'All', result_proxy.fetchall()

result_proxy = conn.execute("SELECT id, first_name, last_name FROM users WHERE first_name = 'David'")
print 'One', result_proxy.fetchone()

# ----------------------------------------------------------------------
# SELECTing directly with WHERE clause and bindparams
# ----------------------------------------------------------------------
from sqlalchemy import text

result_proxy = conn.execute(
    text("SELECT id, first_name, last_name FROM users WHERE first_name = :first_name"),
    first_name="David"
)
print 'All', result_proxy.fetchall()

result_proxy = conn.execute(
    text("SELECT id, first_name, last_name FROM users WHERE first_name = :first_name"),
    first_name="David"
)
print 'One', result_proxy.fetchone()

# ----------------------------------------------------------------------
# SELECTing With A Schema
# ----------------------------------------------------------------------
from sqlalchemy import literal_column, table

select_query = select([
    literal_column('first_name'),
    literal_column('last_name')
]).select_from(table('users'))

# Fetch all
result_proxy = conn.execute(select_query)
print 'All Literal', result_proxy.fetchall()

# Fetch one
result_proxy = conn.execute(select_query)
print 'One Literal', result_proxy.fetchone()
