from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

from settings import settings as s


connection_str = 'postgresql+psycopg2://{db_user}:{db_pwd}@{db_host}:{db_port}/{db_name}'

db_engine = create_engine(connection_str.format(**s.dict()), echo=s.db_echo)

DBSession = sessionmaker(bind=db_engine, autocommit=False)

BaseModel = declarative_base()
