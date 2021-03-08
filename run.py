import uvicorn

from app.api import app
from settings import settings


if __name__ == '__main__':
    uvicorn.run(app, host=settings.app_host, port=settings.app_port)
