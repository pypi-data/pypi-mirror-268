# pylint: disable=missing-module-docstring,missing-function-docstring,missing-class-docstring
from fastapi import FastAPI

from saur.settings import DBSettings
from saur.app.fastapi import attach_sessionmaker

from .auth import auth_router
from .routes import notes_router

def create_app(env: str=None):
    app = FastAPI()
    if env:
        env_file = env
        settings = DBSettings(_env_file=env_file)
    else:
        settings = DBSettings()
    attach_sessionmaker(app, settings)

    app.include_router(auth_router)
    app.include_router(notes_router)

    return app
