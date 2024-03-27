# to connect to db lets use
# sqlalchemy lib (2mb)
# but this lib cannot async, so
# we will use it inly for request generation
# in other cases - use core libs

# another lib "databases" (1.6mb)
# for async work with dbases

# and wrapper for postgresql
# "databases[postgresql]" (2.6mb)

# and lib-adapter to connect to postgresql
# "psycopg2-binary" (3mb)

from databases import Database
from sqlalchemy import create_engine, MetaData
# create_engite used for connection to db
# MetaData - object-Container which contains
# all nessesary information for arm (tables etc) work

# variable that used for connection to db 
# whith contains database_url
from core.config import DATABASE_URL

# create connection to the db
database = Database(DATABASE_URL)
# class exemplar, used for creating tables
metadata = MetaData()
# engine that used only for sync requests
engine = create_engine(
    DATABASE_URL,
)

# (1)
# now app needs to connect to the db
# move to main.py
