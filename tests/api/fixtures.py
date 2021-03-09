import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine

from app.api import app
from app.database.database import connection_str, DBSession, BaseModel
from settings import settings


def test_config():
    return {**settings.dict(), **{'db_name': 'test'}}


@pytest.fixture
def test_client():
    return TestClient(app)


@pytest.fixture(scope='session', autouse=True)
def fake_db():
    db_engine = create_engine(connection_str.format(**test_config()))
    DBSession.configure(bind=db_engine)
    BaseModel.metadata.create_all(db_engine)
    yield
    BaseModel.metadata.drop_all(db_engine)
