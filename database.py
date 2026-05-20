import sqlalchemy as sa
import databases as dbs

DATABASE_URL = 'sqlite:///./blog.db'

database = dbs.Database(DATABASE_URL)
metadata = sa.MetaData()

engine = sa.create_engine(DATABASE_URL, connect_args={"check_same_thread": False})