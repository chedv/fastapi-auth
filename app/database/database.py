from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

from settings import settings as s


connection_str = f'postgresql+psycopg2://{s.db_user}:{s.db_pwd}@{s.db_host}:{s.db_port}/{s.db_name}'

db_engine = create_engine(connection_str, echo=s.db_echo)

DBSession = sessionmaker(bind=db_engine, autocommit=False)

BaseModel = declarative_base()
