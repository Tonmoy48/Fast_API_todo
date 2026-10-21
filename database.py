from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
import urllib.parse

#SQLALCHEMY_DATABASE_URL = 'sqlite:///./todosapp.db' #use this for sqlite
#SQLALCHEMY_DATABASE_URL = ("postgresql+psycopg2://postgres:123@localhost/TodoApplicationDatabase") #for postgresql
SQLALCHEMY_DATABASE_URL = 'postgresql://postgres.puzqiiuuzjsrmxhkdoey:L1QU1D49783r@aws-0-ap-southeast-1.pooler.supabase.com:5432/postgres'
#SQLALCHEMY_DATABASE_URL = f"mysql+pymysql://root:L1QU1D49783r@127.0.0.1:3306/todoapplicationdatabase"

engine = create_engine(SQLALCHEMY_DATABASE_URL)

SessionLocal = sessionmaker(autoflush=False, autocommit=False, bind=engine)

Base = declarative_base()