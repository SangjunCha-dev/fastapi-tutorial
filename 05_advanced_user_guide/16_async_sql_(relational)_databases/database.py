import databases
import sqlalchemy
from sqlalchemy import Table, Boolean, Column, String, Integer

# SQLAlchemy specific code, as with any other app
# Import and set up databases
DATABASE_URL = "sqlite:///./test.db"
#DATABASE_URL = "postgresql://user:password@postgresserver/db"

database = databases.Database(DATABASE_URL)

metadata = sqlalchemy.MetaData()

# Import and set up SQLAlchemy
notes = Table(
    "notes",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("text", String),
    Column("completed", Boolean),
)

# Create the tables
engine = sqlalchemy.create_engine(
    DATABASE_URL,
    connect_args={"check_same_thread": False},
)
metadata.create_all(engine)